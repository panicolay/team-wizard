from analysis.analyzer import MeetingAnalyzer

def main():
    # Notes de test
    test_notes = """
    DK du 20 mars 2024

    Présents : Pierre-Antoine, Marie, Thomas

    1. Revue des maquettes du projet X
    - Discussion sur la navigation mobile
    - Marie propose une nouvelle approche pour le menu
    - @Thomas doit finaliser les animations pour la semaine prochaine
    - Validation du système de filtres

    2. Planning Q2
    - Présentation du roadmap par Pierre-Antoine
    - Priorité sur les features A, B et C
    - @Marie prépare le deck pour le COMEX avant fin mars
    - Point bloquant sur la feature D, à rediscuter

    3. Points divers
    - Mise à jour des outils de design
    - Formation Figma à planifier
    - @Tous : mettre à jour la documentation avant fin du mois
    """

    # Créer l'analyseur
    analyzer = MeetingAnalyzer()

    # Analyser les notes
    meeting = analyzer.analyze_notes(test_notes)

    # Afficher les résultats
    print("\n=== Résumé de la réunion ===")
    print(meeting.summary)

    print("\n=== Sujets discutés ===")
    for topic in meeting.topics:
        print(f"\nSujet : {topic.title}")
        print(f"Résumé : {topic.summary}")
        if topic.tags:
            print(f"Tags : {', '.join(topic.tags)}")
        
        if topic.actions:
            print("\nActions :")
            for action in topic.actions:
                owner = f" (@{action.owner})" if action.owner else ""
                due_date = f" pour le {action.due_date}" if action.due_date else ""
                print(f"- {action.description}{owner}{due_date}")

if __name__ == "__main__":
    main() 