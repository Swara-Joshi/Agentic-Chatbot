#Step1: Setup of api key with groq, OPEN AI and tavily
import os

GROQ_API_KEY = os.environ.get('GROQ_API_KEY')
TAVILY_API_KEY = os.environ.get('TAVILY_API_KEY')
# OPEN_AI_API_KEY = os.environ.get('OPEN_AI_API_KEY')

#Step2: Setup LLM & Tools 
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

# openai_llm=ChatOpenAI(model="gpt-4o-mini")
groq_llm=ChatGroq(model="llama-3.3-70b-versatile")

search_tool=TavilySearchResults(max_results=2)

#Step3: Setup AI Agent with search functionality
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

system_prompt = "Act as an AI chatbot"
agent = create_react_agent(
    model = groq_llm,
    tools = [search_tool],
    state_modifier = system_prompt
)

query = "What is agentic ai"
state = {"messages": query}
response = agent.invoke(state)
# messages = response.get("messages")
# ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]
messages=response.get("messages")
ai_messages=[message.content for message in messages if isinstance(message, AIMessage)]
print(ai_messages[-1])