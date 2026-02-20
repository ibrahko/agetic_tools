import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { Check, Circle } from 'lucide-react-native';
import { colors } from '../theme/colors';
import { CommandeStatut } from '../types/domain';

const STEPS: { key: CommandeStatut; label: string }[] = [
  { key: 'acompte_en_attente', label: 'Acompte en attente' },
  { key: 'mesures_validees', label: 'Mesures validées' },
  { key: 'coupe_en_cours', label: 'Coupe en cours' },
  { key: 'assemblage', label: 'Assemblage' },
  { key: 'finitions', label: 'Finitions' },
  { key: 'pret_pour_retrait', label: 'Prêt pour retrait' },
];

type Props = {
  currentStatus: CommandeStatut;
};

export function StatusTimeline({ currentStatus }: Props) {
  const currentIndex = STEPS.findIndex((s) => s.key === currentStatus);

  return (
    <View style={styles.container}>
      {STEPS.map((step, index) => {
        const done = index <= currentIndex;
        return (
          <View key={step.key} style={styles.row}>
            <View style={styles.iconAndLine}>
              <View style={[styles.iconCircle, done && styles.iconCircleDone]}>
                {done ? <Check size={14} color={colors.surface} /> : <Circle size={14} color={colors.accentGold} />}
              </View>
              {index < STEPS.length - 1 && (
                <View style={[styles.line, done && styles.lineDone]} />
              )}
            </View>
            <Text style={[styles.label, done && styles.labelDone]}>{step.label}</Text>
          </View>
        );
      })}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: colors.surface,
    borderRadius: 18,
    padding: 16,
    borderWidth: 1,
    borderColor: colors.border,
  },
  row: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    minHeight: 54,
  },
  iconAndLine: {
    width: 28,
    alignItems: 'center',
  },
  iconCircle: {
    width: 24,
    height: 24,
    borderRadius: 12,
    borderWidth: 1,
    borderColor: colors.accentGold,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: colors.surface,
  },
  iconCircleDone: {
    backgroundColor: colors.accentGold,
  },
  line: {
    marginTop: 4,
    width: 2,
    flex: 1,
    backgroundColor: colors.border,
  },
  lineDone: {
    backgroundColor: colors.accentGold,
  },
  label: {
    flex: 1,
    color: colors.textSecondary,
    fontSize: 15,
    paddingTop: 2,
    paddingLeft: 12,
  },
  labelDone: {
    color: colors.textPrimary,
    fontWeight: '600',
  },
});
