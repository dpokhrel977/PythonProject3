import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f"Hi, {name}")
    print(os.environ.get("SERVER.PORT"))  # Press ⌘F8 to toggle the breakpoint.


def main1():
    print("hello from my lanchain")
    information = """
    Born into a wealthy family in Pretoria, South Africa, Musk emigrated in 1989 to Canada; he has Canadian citizenship s
ince his mother was born there. He received bachelor's degrees in 1997 from the University of Pennsylvania before moving
 to California to pursue business ventures. In 1995, Musk co-founded the 
software company Zip2. Following its sale in 1999, he co-founded X.com, an online payment company that later merged to 
form PayPal, which was acquired by eBay in 2002. Musk also became an American citizen in 2002."""

    summary_template = f"""
    Given the information {information} about person I want to create
    1. A short summary of person
    2. Two interesting facts about person
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    llm = ChatOpenAI(temperature=0, model="gpt-5.4-mini")
    # define chain.
    chain = summary_prompt_template | llm
    # create response object
    response = chain.invoke(input={information: information})
    print(response.content)
    # print(summary_prompt_template)
    print_hi(information)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print_hi("PyCharm")
    main1()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
