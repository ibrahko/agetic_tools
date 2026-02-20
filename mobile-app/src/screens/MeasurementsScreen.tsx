import React, { useMemo, useState } from 'react';
import { Alert, SafeAreaView, ScrollView, StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import { Save } from 'lucide-react-native';
import { MeasurementField } from '../components/MeasurementField';
import { colors } from '../theme/colors';
import { ChampMesure } from '../types/domain';

type MeasureSection = {
  title: string;
  fields: ChampMesure[];
};

const MEASURE_SECTIONS: MeasureSection[] = [
  {
    title: 'Mensurations principales',
    fields: [
      { key: 'tour_poitrine', label: 'Tour de poitrine', unit: 'cm', required: true },
      { key: 'tour_taille', label: 'Tour de taille', unit: 'cm', required: true },
      { key: 'tour_hanches', label: 'Tour de hanches', unit: 'cm', required: true },
      { key: 'longueur_bras', label: 'Longueur bras', unit: 'cm', required: true },
    ],
  },
  {
    title: 'Ajustements couture',
    fields: [
      { key: 'largeur_epaules', label: 'Largeur épaules', unit: 'cm' },
      { key: 'longueur_tenue', label: 'Longueur tenue', unit: 'cm' },
      { key: 'tour_cou', label: 'Tour de cou', unit: 'cm' },
      { key: 'tour_poignet', label: 'Tour de poignet', unit: 'cm' },
    ],
  },
];

const MOCK_HISTORY = [
  'Version 3 — ajustement longueur bras (+1 cm)',
  'Version 2 — correction tour de taille (-2 cm)',
  'Version 1 — première prise de mesures',
];

export default function MeasurementsScreen() {
  const [values, setValues] = useState<Record<string, string>>({});

  const requiredFields = useMemo(
    () => MEASURE_SECTIONS.flatMap((section) => section.fields.filter((field) => field.required)),
    [],
  );

  const isValid = useMemo(() => requiredFields.every((f) => Number(values[f.key]) > 0), [requiredFields, values]);

  const setFieldValue = (key: string, value: string) => {
    const safeNumeric = value.replace(/[^0-9.]/g, '');
    setValues((prev) => ({ ...prev, [key]: safeNumeric }));
  };

  const handleSave = async () => {
    if (!isValid) {
      Alert.alert('Validation', 'Veuillez renseigner toutes les mesures obligatoires.');
      return;
    }

    // Exemple : await supabase.from('mesures').upsert(...)
    // L'historique est géré côté SQL via le trigger trg_mesures_archive.
    Alert.alert('Succès', 'La fiche de mesures a été sauvegardée.');
  };

  return (
    <SafeAreaView style={styles.safeArea}>
      <ScrollView contentContainerStyle={styles.container}>
        <Text style={styles.title}>Fiche de Mesures</Text>
        <Text style={styles.subtitle}>Coffre à mesures client — suivi versionné pour validation atelier.</Text>

        {MEASURE_SECTIONS.map((section) => (
          <View key={section.title} style={styles.formCard}>
            <Text style={styles.sectionTitle}>{section.title}</Text>
            {section.fields.map((field) => (
              <MeasurementField
                key={field.key}
                label={field.label}
                required={field.required}
                unit={field.unit}
                value={values[field.key] ?? ''}
                onChangeText={(v) => setFieldValue(field.key, v)}
              />
            ))}
          </View>
        ))}

        <View style={styles.historyCard}>
          <Text style={styles.sectionTitle}>Historique des évolutions</Text>
          {MOCK_HISTORY.map((entry) => (
            <Text key={entry} style={styles.historyEntry}>• {entry}</Text>
          ))}
        </View>

        <TouchableOpacity
          style={[styles.button, !isValid && styles.buttonDisabled]}
          onPress={handleSave}
          activeOpacity={0.9}
        >
          <Save size={16} color={colors.surface} />
          <Text style={styles.buttonText}>Sauvegarder les mesures</Text>
        </TouchableOpacity>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: { flex: 1, backgroundColor: colors.background },
  container: { padding: 20, paddingBottom: 34 },
  title: {
    color: colors.textPrimary,
    fontSize: 26,
    fontWeight: '700',
  },
  subtitle: {
    marginTop: 6,
    marginBottom: 18,
    color: colors.textSecondary,
    fontSize: 14,
    lineHeight: 20,
  },
  formCard: {
    backgroundColor: colors.surface,
    borderWidth: 1,
    borderColor: colors.border,
    borderRadius: 16,
    padding: 14,
    marginBottom: 12,
  },
  sectionTitle: {
    color: colors.textPrimary,
    fontSize: 14,
    fontWeight: '700',
    marginBottom: 10,
  },
  historyCard: {
    backgroundColor: colors.surface,
    borderWidth: 1,
    borderColor: colors.border,
    borderRadius: 16,
    padding: 14,
    marginTop: 2,
  },
  historyEntry: {
    color: colors.textSecondary,
    fontSize: 13,
    marginBottom: 6,
  },
  button: {
    marginTop: 18,
    backgroundColor: colors.accentGold,
    borderRadius: 14,
    paddingVertical: 14,
    justifyContent: 'center',
    alignItems: 'center',
    flexDirection: 'row',
    gap: 8,
  },
  buttonDisabled: {
    opacity: 0.5,
  },
  buttonText: {
    color: colors.surface,
    fontSize: 15,
    fontWeight: '700',
  },
});
