from google.cloud import generativeai as genai

def add_numbers_tool(a: int, b: int) -> str:
    """Simple addition tool."""
    return f"The sum of {a} and {b} is {a + b}"

# Register tool with ADK
math_tool = genai.Tool(
    name="add_numbers",
    description="Add two numbers together",
    func=add_numbers_tool
)
