# Application Mobile Couture Luxe — Structure Proposée

```txt
mobile-app/
├── app/
│   ├── (tabs)/
│   │   ├── index.tsx                  # Vitrine sociale + catalogue
│   │   ├── suivi-tenue.tsx            # Écran "Suivi de ma tenue"
│   │   └── profil.tsx                 # Profil client
│   ├── commande/
│   │   ├── [id].tsx                   # Détail commande
│   │   └── paiement-acompte.tsx       # Validation acompte
│   └── mesures/
│       └── fiche.tsx                  # Écran "Fiche de Mesures"
├── src/
│   ├── components/
│   │   ├── StatusTimeline.tsx         # Timeline de production
│   │   ├── MeasurementField.tsx       # Champ dynamique de mesure
│   │   └── LuxeCard.tsx               # Carte UI réutilisable
│   ├── screens/
│   │   ├── TrackingScreen.tsx
│   │   └── MeasurementsScreen.tsx
│   ├── services/
│   │   ├── supabase.ts                # Client Supabase
│   │   └── orders.ts                  # Mutations commandes/paiements
│   ├── theme/
│   │   ├── colors.ts
│   │   └── typography.ts
│   └── types/
│       └── domain.ts                  # Types métier (Commande, Mesures...)
├── assets/
│   └── branding/
│       └── logo-gold.png
├── package.json
└── app.json
```

## Principes d'architecture
- **Domain-driven UI** : séparation des écrans, composants, services, thèmes.
- **Supabase realtime-first** : écoute temps réel sur `commandes` pour rafraîchir le suivi client.
- **Design system luxe** : palette Or / Blanc cassé / Noir et composants homogènes.
