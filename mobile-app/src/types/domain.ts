export type CommandeStatut =
  | 'acompte_en_attente'
  | 'mesures_validees'
  | 'coupe_en_cours'
  | 'assemblage'
  | 'finitions'
  | 'pret_pour_retrait';

export type Commande = {
  id: string;
  reference: string;
  statut: CommandeStatut;
  created_at: string;
  date_livraison_souhaitee?: string;
};

export type ChampMesure = {
  key: string;
  label: string;
  unit?: 'cm';
  required?: boolean;
};
