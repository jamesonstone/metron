from langchain.agents import Tool
from langchain.chat_models import ChatOpenAI
from langchain.utilities import SQLDatabase, GoogleSearchAPIWrapper
from langchain_experimental.sql import SQLDatabaseChain
import os

from langchain.agents import (
    Tool,
    AgentExecutor,
    LLMSingleActionAgent,
)
from langchain.chains import LLMChain
from langchain.agents import (
    Tool,
    AgentExecutor,
    LLMSingleActionAgent,
)

from rag.custom_output_parser import CustomOutputParser
from rag.custom_prompt_template import CustomPromptTemplate


def init_langchain():
    llm = ChatOpenAI(
        temperature=0, model="gpt-3.5-turbo-1106"
    )  # temp 0 to be deterministic // # "tool not found" error gpt-3.5-turbo-0613 [legacy] to gpt-3.5-turbo-1106
    # create a search tool
    search_chain = GoogleSearchAPIWrapper(k=5)  # use only the first 5 result
    # create database connection
    db = SQLDatabase.from_uri("sqlite:///./dataset/businesses.db")
    # create the database chain
    db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

    tools = [
        Tool(
            name="google_search",
            description="useful for when you need to answer questions about current events, businesses, or context",
            func=search_chain.run,
        ),
        Tool(
            name="businesses_database",
            description="useful for when you need to answer questions about businesses.",
            func=db_chain.run,
        ),
    ]

    # Set up the base template
    template = """Complete the objective as best you can. You have access to the following tools:

    {tools}

    Use the following format:

    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer
    Final Answer: the final answer to the original input question

    These were previous tasks you completed:



    Begin!

    Question: {input}
    {agent_scratchpad}"""

    prompt = CustomPromptTemplate(
        # `agent_scratchpad`, `tools`, and `tool_names` variables are generated dynamically
        template=template,
        tools=tools,
        input_variables=["input", "intermediate_steps"],
    )
    output_parser = CustomOutputParser()

    # LLM chain consisting of the LLM and a prompt
    llm_chain = LLMChain(llm=llm, prompt=prompt)

    tool_names = [tool.name for tool in tools]
    agent = LLMSingleActionAgent(
        llm_chain=llm_chain,
        output_parser=output_parser,
        stop=["\nObservation:"],
        allowed_tools=tool_names,
    )

    return AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True)


def prompt(agent, input):
    agent.run(input)
