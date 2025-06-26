Sure! Here's a short and clean GitHub `README.md` for your Cohere chat script:

---

# 🧠 Cohere CLI Chatbot

A simple command-line chatbot interface using the [Cohere API](https://cohere.com/) that allows dynamic adjustment of creativity during a session.

## ✨ Features

* Chat with Cohere's `command` model via the terminal
* Dynamically adjust creativity (temperature) between 0–1 during the session
* Handles both default and user-provided API keys
* Limits token response to avoid crashing

## 🚀 Getting Started

### Prerequisites

* Python 3.7+
* Cohere API key ([get one here](https://dashboard.cohere.com/api-keys))

### Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/cohere-cli-chat.git
cd cohere-cli-chat
```

2. Install dependencies:

```bash
pip install cohere
```

3. Create a `config.py` file in the project directory with your API key:

```python
# config.py
COHERE_API_KEY = "your-default-api-key-here"
```

### Usage

Run the script:

```bash
python chat.py
```

* Press `ENTER` to use the default API key from `config.py` or input your own.
* Type `CREATIVITY` to change the creativity level (0–10).
* Type `END` to exit the chat session.

## 🛠 Example

```
>> Hello!
Cohere: Hi there! How can I help you today?

>> CREATIVITY
>> 7
Creativity set to 0.7.

>> Tell me a joke.
Cohere: Why did the computer show up late to work? It had a hard drive!
```

