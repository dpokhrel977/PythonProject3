from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage

from dotenv import load_dotenv

load_dotenv()
# --- LLM ---
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# --- Tool (mock weather tool) ---
@tool
def get_weather(city: str) -> str:
    """Get current weather for a given city."""
    if "tokyo" in city.lower():
        return "Tokyo weather: 14°C, rainy"
    return f"No weather data available for {city}"

tools = [get_weather]

# --- LangGraph Agent ---
agent = create_react_agent(
    model=llm,
    tools=tools
)

# --- Run with messages ---
response = agent.invoke({
    "messages": [
        HumanMessage(content="What is the weather in Tokyo?")
    ]
})

print(response)