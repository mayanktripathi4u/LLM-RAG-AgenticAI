from google.adk.agents import Agent

root_agent = Agent(
    name="Cat_Dog_Assistant",
    model = "gemini-2.0-flash",
    description="The first agent that someone speaks to before being redirected to the cat or dog assistannt (agent).",
)