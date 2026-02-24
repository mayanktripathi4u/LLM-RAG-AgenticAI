# LangChain

LangChain is the framework that is going to help us build apps using LLMs.

LangChain supports many different language models that we can use interchangebly.

LLMs are advanced Machine Learning Models that excel in a wide range of langugae-related tasks such as text generation, transalation, summarization, question answering, and more without needing task-specific fine tuning for every scenario.

# Chat Model
Modern LLMs are typically accessed through a `chat model` interface that takes alist of messages as input and returns a message as output. Refer [Chat Model](https://python.langchain.com/docs/integrations/chat/) official document.

LangChain has many Chat Models integrations that allow us to use a wide variety of models from different providers.

These integrations are one of two types
1. Official models: These are models that are officially supported by LangChain and / or model provider. We can find these models in the `langchain-<provider>` packages.
2. Community Models: These are models that are mostly contibuted and supported by the community. We can find these models in the `langchain-community` package.

LangChain Chat Models are named with a convention that prefixes `Chat` to their class names, example `ChatOllama`, `ChatAnthropic`, `ChatOpenAI` etc.

# `init_chat_model` Vs `CharGroq`
[init_chat_model](https://python.langchain.com/api_reference/langchain/chat_models/langchain.chat_models.base.init_chat_model.html) and [ChatGroq](https://python.langchain.com/api_reference/groq/chat_models/langchain_groq.chat_models.ChatGroq.html) are not competing alternatives but are used together within the LangChain framework. init_chat_model is a universal helper function for initializing different chat models, while ChatGroq is a specific class for interacting with Groq's high-speed language models.

In short, you can use `init_chat_model` to create a `ChatGroq` instance, or you can create one directly. If you are only ever going to use Groq, `ChatGroq` provides a more explicit and direct approach. If you are building a flexible application that could use `Groq`, `OpenAI`, `Anthropic`, or any other provider interchangeably, `init_chat_model` is the more versatile choice. 

# Messages
- Messsages are the unit of communication in [chat model](#chat-model).
- They are used to represent the input and output of a chat model, as well as any additional context or metadata that may be associated with a conversation.
- Each message has a **role** (eg. user, assistant, system, tool, function) and **content** (eg. text, multimodal data) with additional metadata that varies depending on the chat model provider.
- LangChain provides a unified message format that can be used across chat models, allowing users to work with different chat models without worrying about the specific details of the message format used bu each model provider.
- 

# Prompt Template
- Custom user input in messages.
- [Docs](https://python.langchain.com/docs/tutorials/llm_chain/#prompt-templates)
- Prompt templates are a concept in LangChain designed to assist with this transformation. 
- They take in raw user input and return data (a prompt) that is ready to pass into a language model.
- Usually, it is constructed from a combination of user input and application logic. 
- It will take in two user variables:
  - language: The language to translate text into
  - text: The text to translate 


# Chain in LangChain or Runnable
- [Docs for Runnable Interface](https://python.langchain.com/docs/concepts/runnables/)
- In LangChain, a chain is simply a sequence of steps (or components) that work together to complete a task.
- Instead of calling the LLM (Large Language Model) directly with one input → output, a chain allows you to combine multiple operations like:
  - Preprocessing input
  - Querying an LLM
  - Using tools (search, database, APIs)
  - Formatting/parsing the output
  - Passing the result into another step
- So, a `chain = multiple tasks stitched together`.
- Types of Chains in LangChain
  - Simple Chain – Input → LLM → Output
    Example: User asks → “Explain quantum computing in simple words.”
  - Sequential Chain – Multiple steps, output of one step is fed into the next.
    Example: Summarize → Translate → Generate Quiz.
  - Router Chain – Route a query to different chains depending on input type.
    Example: If query = math → use calculator chain, if query = news → use search chain.
  - Custom Chains – You can build your own logic combining multiple tools, prompts, and LLM calls.
- The `Runnable interface` in LangChain is actually the newer, unified abstraction that makes it easier to define and chain tasks.
- A Runnable is any component that takes an input and produces an output.
- Examples of Runnables:
  - A PromptTemplate (formats user input into a structured prompt)
  - An LLM (takes text prompt → generates response)
  - An OutputParser (takes LLM response → extracts structured data)
  - Even another Chain itself
- Each Runnable implements `.invoke`(input) (for sync execution) or `.ainvoke`(input) (for async).
- Since each step is a Runnable, you can pipe them together. This is very similar to the idea of “chaining tasks,” but more flexible.