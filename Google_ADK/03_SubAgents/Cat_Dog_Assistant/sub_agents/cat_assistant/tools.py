from google.adk.agents import Agent

root_agent = Agent(
    name = "cat_assistant_agent",
    model = "gemini-2.0-flash",
    description = "The cat assistant agent can help with tasks required to do for your cat.",
    
)