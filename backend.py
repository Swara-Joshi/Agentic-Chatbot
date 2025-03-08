#Step 1: Setting up Pydentic model setup

# Importing the necessary components from Pydantic and Python's typing module
from pydantic import BaseModel
from typing import List

# Defining the 'RequestState' class, which inherits from Pydantic's BaseModel.
# This class will be used to structure the incoming data and validate it automatically.
class RequestState(BaseModel):
    
    # Defining the 'model_name' field which should be a string.
    # This will store the name of the AI model being referenced (e.g., 'GPT-3').
    model_name: str
    
    # Defining the 'model_provider' field, which will store the name of the AI model provider.
    # For example, this could be 'OpenAI' or 'Google'.
    model_provider: str
    
    # Defining the 'system_prompt' field, which is a string.
    # It will store the system's prompt or instructions given to the model.
    system_prompt: str
    
    # Defining the 'messages' field, which is a list of strings.
    # This will store the conversation or messages that will be passed to the AI model.
    # The List[str] annotation ensures only a list of strings is allowed.
    messages: List[str]
    
    # Defining the 'allow_search' field, which is a boolean.
    # This field will be used as a flag to allow or disallow search functionality.
    allow_search: bool

#Step2: setup ai agent from frontend
from fastapi import FastAPI

ALLOWED_MODEL_NAMES=["llama3-70b-8192", "mixtral-8x7b-32768", "llama-3.3-70b-versatile", "gpt-4o-mini"] # we have access to all this from groq model


app = FastAPI(title = "LangGraph AI Agent")

@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    API Endpoint to interact with the Chatbot using LangGraph and search tools.
    It dynamically selects the model specified in the request
    """
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return{"error": "Invalid AI model name"}
    
    llm_id = request.model_name
    query = request.messages
    allow_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider

    # Create AI Agent and get response from it! 
    response=get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider)
    return response

#Step3: run app and explore swagger ui
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9999)