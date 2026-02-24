# Environment Setup

1. Clone the Repo.
```sh
git clone https://github.com/mayanktripathi4u/LLM-RAG-AgenticAI.git
```

2. Virtual Env.
```sh
cd /Users/tripathimachine/Desktop/Apps/GitHub_Repo/LLM-RAG-AgenticAI

python -m venv .llm_rag_venv

source .llm_rag_venv/bin/activate

```

3. Create Alias for Virtual Env. (Optional)
```sh

```

4. Work in Docker Container using VS-Code DevContainer (Optional)
```sh


```

5. Install Dependencies
```sh
# Change Directory based on the Project. Like
cd RAG_Pipeline 

pip install -r requirements.txt

pip install ipykernel
```
`ipykernel` is the Python kernel for Jupyter, allowing Python code execution within Jupyter notebooks. VS Code's Jupyter extension leverages this kernel to provide interactive notebook functionality. By installing `ipykernel` in a specific Python environment and then selecting that environment as the kernel in VS Code, you ensure that your notebook runs using the `ipykernel` installed within that chosen environment.

Adding `ipykernel` to VS Code for use with Jupyter notebooks involves ensuring `ipykernel` is installed in your Python environment and that VS Code is configured to use that environment.

Activate your desired Python environment (e.g., a virtual environment or Conda environment). This is crucial to avoid installing `ipykernel` globally if you prefer isolated environments.


