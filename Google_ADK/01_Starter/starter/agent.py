from google.adk.agents import Agent
# from google.adk.tools import google_search

def morning_greet(name: str) -> str:
    return f"Good morning, {name}! How can I assist you today? I am feeling energetic and ready to help!"

def evening_greet(name: str) -> str:
    return f"Good evening, {name}! As the day is about to end, and got tired and low energy. How can I assist you today?"

root_agent = Agent(
    name="Root_Agent",
    description="An Agent (LLM) that can use tools to answer user's question based on Google Search.",
    model = "gemini-2.0-flash",
    instruction = """
    First ask User Name, and start conversation by greeting based on users greet.
    If User greet is "morning", use morning_greet tool to greet user.
    If User greet is "evening", use evening_greet tool to greet user.
    """,
    tools = [morning_greet, evening_greet],  # Add the custom tool to the agent
)