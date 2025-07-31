from fastapi import FastAPI
from pydantic import BaseModel

from pain_point_agent import PainPointAgent

# app initialization
app = FastAPI(
    title="Filum.ai Pain Point to Solution ASgent",
    description="An API that takes a business pain point and suggests relevant Filum.ai solutions",
    version="1.0.0"
)

# instantiate agent (loaded once on startup)
agent = PainPointAgent(knowledge_base_path="filum_knowledge_base.json")

# API models
class PainPointInput(BaseModel):
    text: str
    top_n: int = 3

class Solution(BaseModel):
    solution_title: str
    feature_name: str
    product_category: str
    how_it_helps: str

class Suggestion(BaseModel):
    score: float
    match_reason: str
    solution: Solution


# api endpoint
@app.post("/suggest-solutions", response_model=list[Suggestion])
async def get_suggestions(payload: PainPointInput):
    """Accepts a pain point text and returns a ranked list of potential solutions.
    """
    suggestions = agent.suggest_solutions(
        pain_point_text=payload.text,
        top_n=payload.top_n
    )

    # format the response to match the pydantic model
    response = []
    for s in suggestions:
        response.append({
            "score": s['score'],
            'match_reason': s['match_reason'],
            "solution": {
                "solution_title": s['feature_data']['solution_title'],
                "feature_name": s['feature_data']['feature_name'],
                "product_category": s['feature_data']['product_category'],
                "how_it_helps": s['feature_data']['how_it_helps']
            }
        })

    return response
    