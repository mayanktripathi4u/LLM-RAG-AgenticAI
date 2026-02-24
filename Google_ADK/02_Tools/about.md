This will be a toy example where:

- The root agent orchestrates.

- A math tool is used directly.

- A knowledge subagent answers general questions.

```sh
mini_handsOn/
│── main.py                 # Entry point
│── agents/
│    ├── root_agent.py       # Root agent (orchestrator)
│    ├── knowledge_agent.py  # Subagent
│── tools/
│    ├── math_tool.py        # Custom math tool
│── requirements.txt
│── README.md
```