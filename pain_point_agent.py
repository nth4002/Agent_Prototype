import json

class PainPointAgent:
    """
    An agent that takes a business pain point and suggests solutions from a knowledge base"""
    def __init__(self, knowledge_base_path: str):
        """Initialize the agent by loading the knowledge base"""
        try:
            with open('filum_knowledge_base.json', 'r') as f:
                self.knowledge_base = json.load(f)
        except FileNotFoundError as err:
            print(f"Error: Knowledge Base file not found at {knowledge_base_path}")
            self.knowledge_base = []
        except json.JSONDecodeError as err:
            print(f"Erorr: Could not decode JSON from {knowledge_base_path}")
            self.knowledge_base = []

    def _normalize_text(self, text: str) -> str:
        """Cleans and standardizes the input text for matching
        """
        # convert to lowercase and remove common punctuation
        return text.lower().replace(',', '').replace('.', '').replace('!','')
    
    def suggest_solutions(self, pain_point_text: str, top_n: int = 3):
        """Analyzes a pain point and returns the top N ranked solutions"""
        if not self.knowledge_base:
            return []
        
        normalized_pain_point = self._normalize_text(pain_point_text)
        scored_features = []

        # scoring loop
        for feature in self.knowledge_base:
            relevance_score = 0
            matching_keywords = []

            # iterate through the feature's keywords to calculate score
            for keyword in feature.get('pain_point_keywords', []):
                if keyword in normalized_pain_point:
                    # apply weighted scoring: phrases are move valuable
                    if ' ' in keyword: # multi-word phease
                        relevance_score += 3
                    else:
                        relevance_score += 1# lower score for single-word match
                    matching_keywords.append(keyword)
            
            # only consider features with a non-zero score
            if relevance_score > 0:
                scored_features.append({
                    "feature_data": feature,
                    "score": relevance_score,
                    "match_reason": f"Matched on keywords: {', '.join(matching_keywords)}"
                })
        
        # ranking and selection ---
        # sort features by score in descending order
        sorted_suggestions = sorted(scored_features, key=lambda x: x['score'], reverse=True)
        return sorted_suggestions[:top_n]

if __name__ == "__main__":
    ppa = PainPointAgent('filum_knowledge_base.json')
    text = "Our Support Agents are totally overwhelmed by the ticket backlog and our response times are terrible."
    print(ppa.suggest_solutions(text)[0].keys())