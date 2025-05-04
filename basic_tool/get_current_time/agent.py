from google.adk.agents import LlmAgent 
# from google.adk.tools import google_Search

def get_current_time():
    """Get the current time."""
    import datetime
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

root_agent = LlmAgent(
    model="gemini-2.0-flash-exp", # Required: Specify the LLM 
    name="get_current_time", # Requdired: Unique agent name
    description="A helpful assistant agent that can tell current time",
    instruction="""Respond to the query using get_current_time tool.""",
    tools=[get_current_time], # Provide an instance of the tool
)

# you can run this by using adk web
