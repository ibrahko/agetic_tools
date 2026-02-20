import React, { useMemo, useState } from 'react';
import { Alert, SafeAreaView, ScrollView, StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import { Save } from 'lucide-react-native';
import { MeasurementField } from '../components/MeasurementField';
import { colors } from '../theme/colors';
import { ChampMesure } from '../types/domain';

const MEASURE_FIELDS: ChampMesure[] = [
  { key: 'tour_poitrine', label: 'Tour de poitrine', unit: 'cm', required: true },
  { key: 'tour_taille', label: 'Tour de taille', unit: 'cm', required: true },
  { key: 'tour_hanches', label: 'Tour de hanches', unit: 'cm', required: true },
  { key: 'longueur_bras', label: 'Longueur bras', unit: 'cm', required: true },
  { key: 'largeur_epaules', label: 'Largeur épaules', unit: 'cm' },
  { key: 'longueur_tenue', label: 'Longueur tenue', unit: 'cm' },
  { key: 'tour_cou', label: 'Tour de cou', unit: 'cm' },
  { key: 'tour_poignet', label: 'Tour de poignet', unit: 'cm' },
];

export default function MeasurementsScreen() {
  const [values, setValues] = useState<Record<string, string>>({});

  const isValid = useMemo(
    () => MEASURE_FIELDS.filter((f) => f.required).every((f) => Number(values[f.key]) > 0),
    [values],
  );

  const setFieldValue = (key: string, value: string) => {
    const safeNumeric = value.replace(/[^0-9.]/g, '');
    setValues((prev) => ({ ...prev, [key]: safeNumeric }));
  };

  const handleSave = async () => {
    if (!isValid) {
      Alert.alert('Validation', 'Veuillez renseigner toutes les mesures obligatoires.');
      return;
    }

    // Exemple : await supabase.from('mesures').insert(...)
    Alert.alert('Succès', 'La fiche de mesures a été sauvegardée.');
  };

  return (
    <SafeAreaView style={styles.safeArea}>
      <ScrollView contentContainerStyle={styles.container}>
        <Text style={styles.title}>Fiche de Mesures</Text>
        <Text style={styles.subtitle}>Coffre à mesures client — historique prêt pour validation atelier.</Text>

        <View style={styles.formCard}>
          {MEASURE_FIELDS.map((field) => (
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
