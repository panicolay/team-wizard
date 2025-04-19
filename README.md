# TEAM WIZARD

Assistant IA pour accompagner les réunions d'équipe.

---

## Objectif

Automatiser la formalisation des réunions DK :

- Générer une synthèse à partir de notes brutes
- Extraire les sujets abordés, décisions prises, actions à suivre
- Stocker les informations dans une base de données
- Permettre une consultation facile des CR passés
- Faciliter la recherche d’informations par sujet

---

## Stack

- GPT-4o (API OpenAI)
- Supabase (PostgreSQL)
- Python (script d’analyse + insertion en base)
- React (interface de consultation – à venir)
- Vercel (déploiement web – à venir)

---

## Fonctionnement

### 1. Prendre des notes pendant la réunion

Sous forme libre (.txt ou .md)

### 2. Lancer le script d’analyse

L'IA propose :

- Une synthèse générale
- Une liste des sujets discutés
- Une liste des actions à mener

La proposition peut être modifiée avant validation.

### 3. Enregistrement dans Supabase

Le script insère automatiquement :

- un meeting
- ses topics
- les actions liées

### 4. Consultation (à venir)

Une interface web permettra à l'équipe de :

- consulter les CR par date
- chercher un sujet abordé
- suivre les actions ouvertes

---

## Structure du projet

/
├─ analyse_dk.py # Script principal d’analyse IA
├─ supabase_config.py # Connexion à Supabase
├─ prompts/ # Prompts système pour GPT
├─ notes/ # Dossier des notes brutes
└─ ui/ # (à venir) interface React

---

## Roadmap

- [x] Structure des tables Supabase
- [ ] Analyse IA et insertion automatique
- [ ] Interface web de consultation
- [ ] Recherche sémantique par sujet
- [ ] Assistant conversationnel (option Discord)

---

## Auteur

Pierre-Antoine (Design Lead @ Sewan)
Projet personnel pour fluidifier le partage de connaissance et l'intelligence collective dans une équipe design.
