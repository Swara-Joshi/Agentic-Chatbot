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
#Step3: run app and explore swagger ui