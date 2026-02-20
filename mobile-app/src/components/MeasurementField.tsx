import React from 'react';
import { View, Text, TextInput, StyleSheet } from 'react-native';
import { colors } from '../theme/colors';

type Props = {
  label: string;
  value: string;
  onChangeText: (value: string) => void;
  required?: boolean;
  unit?: string;
};

export function MeasurementField({ label, value, onChangeText, required, unit = 'cm' }: Props) {
  return (
    <View style={styles.wrapper}>
      <Text style={styles.label}>
        {label} {required ? '*' : ''}
      </Text>
      <View style={styles.inputRow}>
        <TextInput
          keyboardType="numeric"
          value={value}
          onChangeText={onChangeText}
          placeholder="0"
          placeholderTextColor={colors.textSecondary}
          style={styles.input}
        />
        <Text style={styles.unit}>{unit}</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  wrapper: { marginBottom: 14 },
  label: {
    color: colors.textPrimary,
    fontSize: 14,
    marginBottom: 6,
    fontWeight: '500',
  },
  inputRow: {
    flexDirection: 'row',
    borderWidth: 1,
    borderColor: colors.border,
    borderRadius: 12,
    backgroundColor: colors.surface,
    alignItems: 'center',
    paddingHorizontal: 12,
  },
  input: {
    flex: 1,
    paddingVertical: 12,
    color: colors.textPrimary,
    fontSize: 16,
  },
  unit: {
    color: colors.textSecondary,
    fontWeight: '600',
  },
});
