# Livrable — App mobile atelier de couture haut de gamme

Ce dossier contient :

1. **Structure de dossiers recommandée** : `docs/mobile-couture/STRUCTURE.md`
2. **Schéma SQL Supabase complet** : `sql/supabase/couture_schema.sql`
   - Tables métier demandées : `profiles`, `mesures`, `modeles`, `commandes`, `paiements`
   - Tables complémentaires : interactions sociales (`modele_likes`, `modele_commentaires`) + historique (`mesures_historique`)
3. **Logique métier acompte -> statut commande**
   - Fonction SQL : `public.on_acompte_paid_update_commande()`
   - Service client : `mobile-app/src/services/orders.ts` (`markDepositAsPaid`)
4. **Code source des écrans clés** :
   - `mobile-app/src/screens/TrackingScreen.tsx` (Suivi de ma tenue + Progress Bar)
   - `mobile-app/src/screens/MeasurementsScreen.tsx` (Fiche de Mesures dynamique)

## Palette "Luxe & Minimaliste"
- Or : `#C9A86A`
- Blanc cassé : `#F8F5F0`
- Noir : `#111111`
