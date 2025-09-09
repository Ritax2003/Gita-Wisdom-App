from typing import List, Dict

class GitaRetriever:
    def __init__(self, verses_data):
        self.verses_data = verses_data
        self.topic_themes = {
            'stress': ['peace', 'meditation', 'detachment'],
            'depression': ['peace', 'knowledge', 'soul'],
            'anxiety': ['peace', 'meditation', 'detachment'],
            'fear': ['peace', 'knowledge', 'soul'],
            'anger': ['peace', 'detachment', 'duty'],
            'confusion': ['knowledge', 'duty', 'action'],
            'purpose': ['duty', 'action', 'devotion'],
            'death': ['soul', 'knowledge', 'detachment'],
            'suffering': ['peace', 'detachment', 'knowledge'],
            'relationships': ['detachment', 'devotion', 'duty'],
            'work': ['action', 'duty', 'detachment'],
            'success': ['action', 'detachment', 'duty'],
            'failure': ['peace', 'detachment', 'action']
        }

    def extract_theme(self, text: str) -> str:
        text_lower = text.lower()
        themes = {
            'duty': ['duty', 'dharma', 'righteous', 'obligation'],
            'detachment': ['attachment', 'detachment', 'renunciation', 'surrender'],
            'knowledge': ['knowledge', 'wisdom', 'understand', 'realize'],
            'devotion': ['devotion', 'worship', 'love', 'surrender'],
            'action': ['action', 'work', 'perform', 'activity'],
            'soul': ['soul', 'self', 'atman', 'eternal'],
            'peace': ['peace', 'tranquil', 'calm', 'serenity'],
            'meditation': ['meditation', 'yoga', 'mind', 'concentration']
        }
        for theme, keywords in themes.items():
            if any(keyword in text_lower for keyword in keywords):
                return theme
        return 'general'

    def extract_query_themes(self, query: str) -> List[str]:
        query_lower = query.lower()
        relevant_themes = []
        for topic, themes in self.topic_themes.items():
            if topic in query_lower:
                relevant_themes.extend(themes)
        return list(dict.fromkeys(relevant_themes)) if relevant_themes else ['general']

    def find_relevant_verses(self, query: str, max_results: int = 5) -> List[Dict]:
        query_lower = query.lower()
        themes = self.extract_query_themes(query)
        scored_verses = []
        for verse in self.verses_data:
            score = 0
            verse_text_lower = verse['text'].lower()
            verse_theme = self.extract_theme(verse['text'])

            if verse_theme in themes:
                score += 3

            for word in query_lower.split():
                if len(word) > 3 and word in verse_text_lower:
                    score += 2

            if score > 0:
                verse_copy = verse.copy()
                verse_copy['relevance_score'] = score
                verse_copy['theme'] = verse_theme
                scored_verses.append(verse_copy)

        scored_verses.sort(key=lambda x: x['relevance_score'], reverse=True)
        return scored_verses[:max_results]
