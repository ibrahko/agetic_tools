-- Schéma Supabase/PostgreSQL pour atelier de couture haut de gamme
-- Extension UUID (souvent déjà disponible sur Supabase)
create extension if not exists "pgcrypto";

-- 1) Profils utilisateurs
create table if not exists public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  role text not null check (role in ('client', 'couturiere', 'admin')) default 'client',
  nom_complet text not null,
  telephone text,
  avatar_url text,
  adresse text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

-- 2) Modèles publiés (vitrine + catalogue)
create table if not exists public.modeles (
  id uuid primary key default gen_random_uuid(),
  titre text not null,
  description text,
  categorie text not null,
  prix_base numeric(12,2) not null check (prix_base >= 0),
  image_url text,
  statut_publication text not null check (statut_publication in ('brouillon', 'publie')) default 'publie',
  created_by uuid not null references public.profiles(id),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

-- 3) Commandes clients
create table if not exists public.commandes (
  id uuid primary key default gen_random_uuid(),
  reference text unique not null,
  client_id uuid not null references public.profiles(id),
  couturiere_id uuid references public.profiles(id),
  modele_id uuid references public.modeles(id),
  montant_total numeric(12,2) not null check (montant_total >= 0),
  montant_acompte_requis numeric(12,2) not null check (montant_acompte_requis >= 0),
  montant_acompte_paye numeric(12,2) not null default 0 check (montant_acompte_paye >= 0),
  statut text not null default 'acompte_en_attente' check (
    statut in (
      'acompte_en_attente',
      'mesures_validees',
      'coupe_en_cours',
      'assemblage',
      'finitions',
      'pret_pour_retrait',
      'livree',
      'annulee'
    )
  ),
  date_livraison_souhaitee date,
  notes_client text,
  notes_atelier text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

-- 4) Coffre à mesures (snapshot courant)
create table if not exists public.mesures (
  id uuid primary key default gen_random_uuid(),
  client_id uuid not null references public.profiles(id) on delete cascade,
  commande_id uuid references public.commandes(id) on delete set null,
  tour_poitrine numeric(6,2),
  tour_taille numeric(6,2),
  tour_hanches numeric(6,2),
  longueur_bras numeric(6,2),
  largeur_epaules numeric(6,2),
  longueur_tenue numeric(6,2),
  tour_cou numeric(6,2),
  tour_poignet numeric(6,2),
  notes text,
  prises_par uuid references public.profiles(id),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

-- 5) Historique des mesures (audit trail)
create table if not exists public.mesures_historique (
  id bigserial primary key,
  mesures_id uuid not null references public.mesures(id) on delete cascade,
  version integer not null,
  payload jsonb not null,
  updated_by uuid references public.profiles(id),
  created_at timestamptz not null default now(),
  unique (mesures_id, version)
);

-- 6) Paiements d'acompte/solde
create table if not exists public.paiements (
  id uuid primary key default gen_random_uuid(),
  commande_id uuid not null references public.commandes(id) on delete cascade,
  client_id uuid not null references public.profiles(id),
  montant numeric(12,2) not null check (montant > 0),
  canal text not null check (canal in ('wave', 'orange_money', 'especes')),
  statut text not null check (statut in ('en_attente', 'paye', 'echoue', 'rembourse')) default 'en_attente',
  transaction_ref text,
  type_paiement text not null check (type_paiement in ('acompte', 'solde')) default 'acompte',
  paid_at timestamptz,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create index if not exists idx_commandes_client on public.commandes(client_id);
create index if not exists idx_commandes_statut on public.commandes(statut);
create index if not exists idx_paiements_commande on public.paiements(commande_id);
create index if not exists idx_mesures_client on public.mesures(client_id);

-- Trigger helper: updated_at automatique
create or replace function public.set_updated_at()
returns trigger
language plpgsql
as $$
begin
  new.updated_at = now();
  return new;
end;
$$;

create trigger trg_profiles_updated_at
before update on public.profiles
for each row execute function public.set_updated_at();

create trigger trg_modeles_updated_at
before update on public.modeles
for each row execute function public.set_updated_at();

create trigger trg_commandes_updated_at
before update on public.commandes
for each row execute function public.set_updated_at();

create trigger trg_mesures_updated_at
before update on public.mesures
for each row execute function public.set_updated_at();

create trigger trg_paiements_updated_at
before update on public.paiements
for each row execute function public.set_updated_at();

-- Historisation automatique des mesures
create or replace function public.archive_mesures_version()
returns trigger
language plpgsql
as $$
declare
  next_version integer;
begin
  select coalesce(max(version), 0) + 1
    into next_version
  from public.mesures_historique
  where mesures_id = new.id;

  insert into public.mesures_historique (mesures_id, version, payload, updated_by)
  values (
    new.id,
    next_version,
    to_jsonb(new),
    new.prises_par
  );

  return new;
end;
$$;

create trigger trg_mesures_archive
after insert or update on public.mesures
for each row execute function public.archive_mesures_version();

-- Logique métier: auto-transition commande après acompte payé
create or replace function public.on_acompte_paid_update_commande()
returns trigger
language plpgsql
security definer
as $$
declare
  total_acompte_paye numeric(12,2);
begin
  if new.statut = 'paye' and new.type_paiement = 'acompte' then
    select coalesce(sum(montant), 0)
      into total_acompte_paye
    from public.paiements
    where commande_id = new.commande_id
      and type_paiement = 'acompte'
      and statut = 'paye';

    update public.commandes
    set montant_acompte_paye = total_acompte_paye,
        statut = case
          when total_acompte_paye >= montant_acompte_requis
               and statut = 'acompte_en_attente'
            then 'mesures_validees'
          else statut
        end
    where id = new.commande_id;
  end if;

  return new;
end;
$$;

create trigger trg_on_paiement_acompte_paye
after insert or update of statut on public.paiements
for each row
when (new.type_paiement = 'acompte')
execute function public.on_acompte_paid_update_commande();
