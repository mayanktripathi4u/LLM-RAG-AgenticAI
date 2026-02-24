from google.cloud import generativeai as genai

# Example of a custom tool
def add_numbers_tool(a: int, b: int) -> str:
    return f"The sum of {a} and {b} is {a + b}"

math_tool = genai.Tool(
    name="add_numbers",
    description="Add two numbers together",
    func=add_numbers_tool
)

