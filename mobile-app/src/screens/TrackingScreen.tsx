import React from 'react';
import { SafeAreaView, View, Text, StyleSheet } from 'react-native';
import { Ruler, CalendarClock } from 'lucide-react-native';
import { StatusTimeline } from '../components/StatusTimeline';
import { colors } from '../theme/colors';
import { Commande } from '../types/domain';

type Props = {
  commande: Commande;
};

export default function TrackingScreen({ commande }: Props) {
  return (
    <SafeAreaView style={styles.safeArea}>
      <View style={styles.container}>
        <Text style={styles.title}>Suivi de ma tenue</Text>
        <Text style={styles.reference}>Commande #{commande.reference}</Text>

        <View style={styles.metaRow}>
          <View style={styles.metaCard}>
            <Ruler size={16} color={colors.accentGold} />
            <Text style={styles.metaLabel}>Statut actuel</Text>
            <Text style={styles.metaValue}>{commande.statut.replaceAll('_', ' ')}</Text>
          </View>

          <View style={styles.metaCard}>
            <CalendarClock size={16} color={colors.accentGold} />
            <Text style={styles.metaLabel}>Livraison souhaitée</Text>
            <Text style={styles.metaValue}>{commande.date_livraison_souhaitee ?? 'Non précisée'}</Text>
          </View>
        </View>

        <StatusTimeline currentStatus={commande.statut} />
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: { flex: 1, backgroundColor: colors.background },
  container: { flex: 1, padding: 20 },
  title: {
    color: colors.textPrimary,
    fontSize: 26,
    fontWeight: '700',
    marginBottom: 6,
  },
  reference: {
    color: colors.textSecondary,
    fontSize: 15,
    marginBottom: 20,
  },
  metaRow: {
    flexDirection: 'row',
    gap: 10,
    marginBottom: 16,
  },
  metaCard: {
    flex: 1,
    backgroundColor: colors.surface,
    borderRadius: 14,
    borderWidth: 1,
    borderColor: colors.border,
    padding: 12,
  },
  metaLabel: {
    marginTop: 8,
    color: colors.textSecondary,
    fontSize: 12,
  },
  metaValue: {
    marginTop: 4,
    color: colors.textPrimary,
    fontSize: 14,
    fontWeight: '600',
    textTransform: 'capitalize',
  },
});
