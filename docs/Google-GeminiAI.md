# Google



# `from google import genai` vs `import google.generativeai`
The two imports look similar but they’re actually different Python client libraries for Google’s Generative AI:

1. from google import genai

* This refers to the newer Google AI Python SDK (often just called google-genai).

* It’s a more modern, consolidated library that Google introduced in mid-2024, meant to unify access to Gemini and other AI services.

* Example usage:
```python
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")
response = client.models.generate_content(
    model="gemini-1.5-flash",
    contents="Write a haiku about healthcare data"
)
print(response.output_text)
```
* Advantage: Cleaner API, consistent client object (genai.Client), closer to Google’s future direction.


2. import google.generativeai

* This is the older library (google-generativeai) released when Gemini (then Bard) APIs first became public.

* Example usage:
```python
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

response = genai.generate_text(
    model="models/text-bison-001",
    prompt="Write a haiku about healthcare data"
)
print(response.result)
```
* Advantage: Widely used in early tutorials and still works, but being phased out in favor of google.genai.

**✅ Which one should you use?**
* Use from google import genai for new projects, since it’s the official, supported SDK moving forward.

* Only use google.generativeai if you’re maintaining older code that hasn’t migrated yet.