import { SupabaseClient } from '@supabase/supabase-js';

/**
 * Marque un acompte comme payé.
 * Le trigger SQL `on_acompte_paid_update_commande` met ensuite
 * à jour automatiquement le statut de la commande.
 */
export async function markDepositAsPaid(
  supabase: SupabaseClient,
  paiementId: string,
  transactionRef?: string,
) {
  const { data, error } = await supabase
    .from('paiements')
    .update({
      statut: 'paye',
      transaction_ref: transactionRef ?? null,
      paid_at: new Date().toISOString(),
    })
    .eq('id', paiementId)
    .select('id, commande_id, statut, paid_at')
    .single();

  if (error) {
    throw error;
  }

  return data;
}
