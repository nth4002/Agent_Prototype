# Filum.ai Pain Point to Solution Agent

## Overview

This project provides an API that analyzes business pain points and suggests relevant Filum.ai solutions using a knowledge base. It leverages FastAPI for the web interface and Pydantic for data validation.

## Features

- Accepts business pain point descriptions via API
- Returns ranked solution suggestions from a JSON knowledge base
- Extensible knowledge base for new features and solutions

## Project Structure

```
Agent_Prototype/
├── main.py                   # The FastAPI application entry point. Defines the API endpoints and handles incoming requests.
├── pain_point_agent.py       # ontains the logic for analyzing pain points and suggesting solutions from the knowledge base.
├── filum_knowledge_base.json # knowledge_base used for testing
├── knowledge_base.json       # main knowledge_base used by the agent to match pain points to solutions
├── example.txt               # Contains example API requests for testing or demonstration purposes.
├── requirements.txt          # requirements package
└── README.md
Contains example API requests for testing or demonstration purposes.
```

## Getting Started

### Prerequisites

- Python 3.8+ (my version is 3.13.2)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Pydantic](https://docs.pydantic.dev/)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/nth4002/Agent_Prototype.git
   cd Agent_Prototype
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv agent
   source agent/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the API

Start the FastAPI server with Uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at [http://localhost:8000](http://localhost:8000).

### Example Usage

Send a POST request to `/suggest-solutions` with a JSON payload:

```json
{
  "text": "Our support agents are overwhelmed by ticket backlog and response times are terrible.",
  "top_n": 3
}
```

#### Sample Response

```json
[
  {
    "score": 4,
    "match_reason": "Matched on keywords: ticket backlog, overwhelmed",
    "solution": {
      "solution_title": "AI Agent for FAQ & First Response",
      "feature_name": "AI Inbox",
      "product_category": "AI Customer Service",
      "how_it_helps": "Streamlines your contact center by using AI agents to handle repetitive questions 24/7, deflecting a high volume of tickets and freeing up your human agents to focus on complex, high-value issues."
    }
  }
]
```

For example:
<img width="1421" height="351" alt="image" src="https://github.com/user-attachments/assets/13002cc4-4a2f-420f-ab88-d2e6816b4331" />

## Customizing the Knowledge Base

Edit `filum_knowledge_base.json` or `knowledge_base.json` to add new features, solutions, or pain point keywords. The `knowledge_base.json` is the completed version of knowledge base for this prototype
