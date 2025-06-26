# 🧠 Cohere Text Completion Chatbot

A simple command-line chatbot interface using the [Cohere API](https://cohere.com/) that allows dynamic adjustment of creativity during a session.

## Features

* Chat with Cohere's `command` model via the terminal
* Dynamically adjust creativity (temperature) between 0–1 during the session
* Handles both default and user-provided API keys
* Limits token response to avoid crashing

## Getting Started

### Prerequisites

* Python 3.7+
* Cohere API key ([get one here](https://dashboard.cohere.com/api-keys))

### Installation

1. Clone this repository:

```bash
git clone https://github.com/anveetha/ai-text-completion-project.git
cd cohere-cli-chat
```

2. Install dependencies:

```bash
pip install cohere
```

3. Edit the `config.py` file in the project directory with your API key:

```python
# config.py
COHERE_API_KEY = 'your-default-api-key-here'
```

### Usage

Run the script:

```bash
python text_completion_app.py
```

* Input your own Cohere API key either via `config.py` or directly through the terminal upon startup. 
* Type `CREATIVITY` to change the creativity level (0–10).
* Type `END` to exit the chat session.

