from graph.graph import build_graph
from graph.state import ResearchState

graph = build_graph()

if __name__ == "__main__":
    state = ResearchState(
        user_query="Compare CNN and Vision Transformers for medical image classification"
    )

    final_state = graph.invoke(state)

    print(final_state["research_scope"])
    print(final_state["plan"])







# """Minimal API entrypoint using FastAPI."""
# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "AI Research Agent API"}


# # Run with: uvicorn api.main:app --reload
