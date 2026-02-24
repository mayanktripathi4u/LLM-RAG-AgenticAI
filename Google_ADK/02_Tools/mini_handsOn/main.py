root_agent = genai.Agent(
    name="root_agent",
    instructions="You are the orchestrator. "
                 "If the user asks to add numbers, use the math tool. "
                 "If the user asks general knowledge, delegate to the knowledge agent.",
    tools=[math_tool],         # Direct helper
    subagents=[knowledge_agent] # Delegation option
)
