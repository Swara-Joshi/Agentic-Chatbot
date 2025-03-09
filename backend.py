from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from ai_agent import get_response_from_ai_agent  # Ensure this function is correct!

# Define allowed AI models
ALLOWED_MODEL_NAMES = ["mixtral-8x7b-32768", "llama-3.3-70b-versatile", "gpt-4o-mini"]

# Define Pydantic model for validation
class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool

# Initialize FastAPI app
app = FastAPI(title="LangGraph AI Agent")

# Enable CORS (IMPORTANT for frontend access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change "*" to frontend URL for security (e.g., "https://your-streamlit-app.com")
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    API Endpoint to interact with the chatbot using LangGraph and search tools.
    """
    if request.model_name not in ALLOWED_MODEL_NAMES:
        raise HTTPException(status_code=400, detail="Invalid model name. Select a valid AI model.")

    # Extract request parameters
    llm_id = request.model_name
    query = request.messages
    allow_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider

    try:
        # Get AI response
        response = get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

# Run FastAPI server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9999)
