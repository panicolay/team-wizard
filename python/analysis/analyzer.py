import os
from datetime import datetime, date
from typing import List, Dict, Any
import json
import textwrap

from openai import OpenAI
from dotenv import load_dotenv

from .models import Meeting, Topic, Action, ActionStatus

load_dotenv()

class MeetingAnalyzer:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def analyze_notes(self, notes: str, meeting_date: date = None) -> Meeting:
        """Analyse les notes brutes et retourne une structure Meeting complète."""
        
        if meeting_date is None:
            meeting_date = date.today()

        # 1. Obtenir un résumé général et les sujets
        summary_and_topics = self._analyze_summary_and_topics(notes)
        
        # 2. Pour chaque sujet, analyser les actions
        topics = self._analyze_topics_details(summary_and_topics['topics'])

        # 3. Créer et retourner l'objet Meeting
        return Meeting(
            date=meeting_date,
            raw_notes=notes,
            summary=summary_and_topics['summary'],
            topics=topics
        )

    def _analyze_summary_and_topics(self, notes: str) -> Dict[str, Any]:
        """Première passe : résumé général et identification des sujets."""
        
        prompt = f"""Analyse ces notes de réunion et fournis :
1. Un résumé général concis
2. Une liste des sujets principaux discutés

Format de réponse attendu (JSON) :
{{
    "summary": "résumé de la réunion",
    "topics": [
        {{
            "title": "titre du sujet",
            "summary": "résumé du sujet",
            "tags": ["tag1", "tag2"]
        }}
    ]
}}

Notes à analyser :
---
{notes}
"""

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Tu es un assistant spécialisé dans l'analyse de notes de réunion."},
                {"role": "user", "content": prompt}
            ],
            response_format={ "type": "json_object" }
        )

        return json.loads(response.choices[0].message.content)

    def _analyze_topics_details(self, topics_data: List[Dict[str, Any]]) -> List[Topic]:
        """Deuxième passe : analyse détaillée de chaque sujet pour extraire les actions."""
        
        topics = []
        for topic_data in topics_data:
            # Analyser les actions pour ce sujet
            actions = self._extract_actions(topic_data['summary'])
            
            # Créer l'objet Topic avec ses actions
            topic = Topic(
                title=topic_data['title'],
                summary=topic_data['summary'],
                tags=topic_data.get('tags', []),
                actions=actions
            )
            topics.append(topic)
        
        return topics

    def _extract_actions(self, topic_summary: str) -> List[Action]:
        """Extrait les actions à partir du résumé d'un sujet."""
        
        prompt = f"""Analyse ce résumé et identifie toutes les actions à mener.
Pour chaque action, essaie d'identifier le responsable et la date limite si mentionnés.

Format de réponse attendu (JSON) :
{{
    "actions": [
        {{
            "description": "description de l'action",
            "owner": "responsable ou null",
            "due_date": "YYYY-MM-DD ou null"
        }}
    ]
}}

Résumé à analyser :
---
{topic_summary}
"""

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Tu es un assistant spécialisé dans l'identification d'actions à partir de texte."},
                {"role": "user", "content": prompt}
            ],
            response_format={ "type": "json_object" }
        )

        result = json.loads(response.choices[0].message.content)
        
        actions = []
        for action_data in result['actions']:
            # Convertir la date si elle existe
            due_date = None
            if action_data.get('due_date'):
                try:
                    due_date = datetime.strptime(action_data['due_date'], '%Y-%m-%d').date()
                except ValueError:
                    pass  # Ignorer les dates invalides

            action = Action(
                description=action_data['description'],
                owner=action_data.get('owner'),
                due_date=due_date
            )
            actions.append(action)
        
        return actions 