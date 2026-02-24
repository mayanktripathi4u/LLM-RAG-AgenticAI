# Starting with the Google ADK
This is very basic on what are pre-requisit to work with ADK, and a minimal code to start with, and then will add more code to keep making complex.

- Step 1: Check Google ADK Module Available
    ```sh
    # Check Google ADK Module Available
    pip show google-adk
    ```
- Step 2: Install Google-ADK
    ```sh
    pip install google-sdk
    ```
- Step 3: Directory Structure to follow
Google ADK would require a defined folder structure.

    Here a root folder say `01_Starter`, and within this folder, we need atleast two files, first is `agent.py` which is the main file or entry point, and the other file is `__init__` file, which will help in making the whole directory as a Python Package. And `.env` file to set the authentication information. 
    ```sh
    my_root_folder/ (say 01_Starter)
    |-- [agent.py](agent.py)
    |-- [__init__.py](__init__.py)
    |-- [.env](..env)
    ```

    `agent.py`
    
    ```python
    from google.adk.agents import Agent

    root_agent = Agent(
        name="Root Agent",
        description="An Agent (LLM) that can use tools to answer user's question.",
        model = "gemini-2.0-flash",
        tools=[],
        verbose=True,
    #     instruction = """
    #     You are AI Assistant that helps Users with Google Cloud Related queries.
    # """
        instruction = """
        First ask User Name, and start conversation by greeting user with name. You are AI Assistant that helps Users with Google Cloud Related queries.
        """,
    )
    ```

    `__init__.py` will have import statement only.
    ```python
    from . import agent
    ```

- Step 4: Make changes / Coding
- Step 5: Run the Code.
    
    Nows it time to run the code. However, there are multiple ways to run your model or code. Refer [Google Doc to run your agent](https://google.github.io/adk-docs/get-started/quickstart/#run-your-agent).

  - `Web-UI`: Will start with the basic one, where we can have the Web-UI, and we can check all the response, trace session details, flow of the models, etc. MAinly used for Dev purpose.
  
    Run the command `adk web` on the terminal under the root folder, it will open the agent for us.  
  
    Now open the browser, and interacting like we interact with ChatGPT. Ask question (provide prompts).

  - `Terminal`: Another is to use terminal to interact with the Agent. For this we have to use the command `adk run 01_Starter`, it will connect to interactive terminal, and we can start typing our prompt.
  
  - `API-based`: Third way to run the code / agent. Mainly used for Production and to deploy multi-agent system.
  
- Step 6: Authentication credentials to use

    For this we will make use of `.env` file to set credentials. Refer [Google ADK Doc for Authentication](https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model)
    - Option 1: Usign API Key.
        
        To create API key, navigate to *Google AI Studio* > *API Keys* to create API key, which will create a GCP project if creating for the first time, or could select the project if we already have any.

        When using this option, the `.env` file will have below two variables, and then we should be good to run the code.
        ```sh
        GOOGLE_GENAI_USE_VERTEXAI=False
        GOOGLE_API_KEY=<Paste API Key here>
        ```

    - Option 2: Using Vertex AI or User's Credentials

        In here will use the User's Credentials from where the Agent is running. So user should already have gcloud configured. Check the project using `gcloud config list`. 
        Or use `gcloud auth application-default login` to login to Google Cloud Project.

        ```sh
        GOOGLE_GENAI_USE_VERTEXAI=True
        GOOGLE_CLOUD_PROJECT=<gcp-project-id>
        GOOGLE_CLOUD_LOCATION=us-central-1
        ```


# Adding in-built Tool to the existing simple Web Agent
Now lets add [Tool]() to our existing simple web agent. To begin with will use *Google Search* as tool to give search capability to our Agent.

Modify the `agent.py` file. Here will use the inbuilt "google search" tool, we could alsu use custom tools.

```python
from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="Root Agent",
    description="An Agent (LLM) that can use tools to answer user's question based on Google Search.",
    model = "gemini-2.0-flash",
#     instruction = """
#     You are AI Assistant that helps Users with Google Cloud Related queries.
# """
    instruction = """
    First ask User Name, and start conversation by greeting user with name. You are AI Assistant that helps Users with Google Cloud Related queries based on Google Search results.
    """,
    tools = [google_search]  # Add the google_search tool to the agent
)
```


# Adding Custom Tool to the existing simple Web Agent
In here will create two custom functions to greet user based on the users input greet, and call respective function. To this we have Morning Greet and Evening Greet functions. Agent is smart enough to interpret the user input and decide which function to call.

Will modify the `agent.py` with below code.

```python
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
```
