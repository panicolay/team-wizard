# TEAM WIZARD

Assistant IA pour accompagner les réunions d'équipe.

---

## Objectif

Automatiser la formalisation des réunions DK :

- Générer une synthèse à partir de notes brutes
- Extraire les sujets abordés, décisions prises, actions à suivre
- Stocker les informations dans une base de données
- Permettre une consultation facile des CR passés
- Faciliter la recherche d'informations par sujet

---

## Stack Technique

- **Frontend :**
  - Next.js (framework React)
  - TypeScript (pour plus de robustesse)
  - TailwindCSS (styling)

- **Backend :**
  - Python (analyse IA et traitement des notes)
  - Supabase (base de données PostgreSQL)
  - GPT-4 (API OpenAI)

- **Déploiement :**
  - Vercel (hébergement)

---

## Fonctionnement

### 1. Prendre des notes pendant la réunion

Sous forme libre (.txt ou .md)

### 2. Lancer l'analyse

L'IA propose :

- Une synthèse générale
- Une liste des sujets discutés
- Une liste des actions à mener

La proposition peut être modifiée avant validation.

### 3. Enregistrement dans Supabase

Le système insère automatiquement :

- un meeting
- ses topics
- les actions liées

### 4. Consultation

Interface web permettant de :

- consulter les CR par date
- chercher un sujet abordé
- suivre les actions ouvertes

---

## Structure du projet

/
├─ app/                   # Code principal (Next.js)
│  ├─ components/         # Composants React réutilisables
│  ├─ pages/              # Pages principales
│  └─ utils/              # Fonctions utilitaires
├─ python/                # Scripts Python
│  ├─ analysis/           # Analyse des notes
│  └─ database/           # Gestion Supabase
├─ prompts/               # Prompts système pour GPT
└─ notes/                 # Notes brutes

---

## Roadmap

- [x] Structure des tables Supabase
- [ ] Mise en place de Next.js + TypeScript
- [ ] Intégration de l'analyse IA
- [ ] Interface de consultation basique
- [ ] Système de tags
- [ ] Export PDF

---

## Auteur

Pierre-Antoine (Design Lead @ Sewan)
Projet personnel pour fluidifier le partage de connaissance et l'intelligence collective dans une équipe design.
