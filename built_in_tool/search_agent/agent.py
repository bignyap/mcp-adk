from google.adk.agents import Agent 
from google.adk.tools import google_search

root_agent = Agent(
    model="gemini-2.0-flash-exp", # Required: Specify the LLM 
    name="search_agent", # Requdired: Unique agent name
    description="A helpful assistant to answer user query from google search",
    instruction="""Respond to the query via google search""",
    tools=[google_search], # Provide an instance of the tool
)