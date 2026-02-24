from google.cloud import generativeai as genai

# Subagent for general knowledge Q&A
knowledge_agent = genai.Agent(
    name="knowledge_agent",
    instructions="You are a helpful assistant for general knowledge questions. "
                 "If asked something general (e.g., world knowledge, current events), answer directly."
)
