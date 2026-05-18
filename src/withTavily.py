import os

from dotenv import load_dotenv

load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain.agents import create_react_agent, initialize_agent, AgentType
# from  langchain.agents import create_agent
##we going to use HumanMessage to invoke agent
from langchain_core.messages import HumanMessage
# import tool for agent
from langchain.tools import tool
# from langchain.agents import initialize_agent, AgentType
from langchain.agents import AgentExecutor
##search from web use tavily
from tavily import TavilyClient

tavily = TavilyClient()


## define search function
@tool
def search(query: str) -> str:
    """
    Tools that searches over the internet
    Args:
    query: the query to search for
    Returns: The search result
    :return:
    """
    print(f"searching for a {query}")
    # return "Tokyo weather is cold"
    return tavily.search(query=query)


def searchagent():
    ## llm = ChatOpenAI(model="gpt-5", temperature=0.7)
    llm = ChatOpenAI()
    # llm=ChatOllama(model="gemma3:270m")
    tools = [search]
    ## create_agent is old version in langchain using to create_react_agent
    # agent = create_react_agent(llm,tools)

    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    response = agent.invoke({"input": "what is the weather tokyo ?"});


# print(response.content)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    searchagent()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
