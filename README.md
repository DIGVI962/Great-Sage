# Great-Sage

**Great-Sage** is an agentic conversational application built with FastAPI, Google ADK, and GenAI, designed to facilitate interactive chat sessions with advanced session management and logging.

---

## Features

- **FastAPI** backend for RESTful chat endpoints
- **Session management** using in-memory storage
- **Google ADK & GenAI** integration for agent orchestration and LLM responses
- **CORS support** for easy frontend integration
- **Structured logging** with configurable log levels
- **Environment variable support** for configuration
- **Interactive CLI conversation loop** (optional, see code)

---

## Requirements

- Python 3.13+
- [Google ADK](https://google.github.io/adk-docs/) and [Google GenAI](https://github.com/google/generative-ai-python)
- FastAPI, Uvicorn, python-dotenv, and other dependencies (see below)

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/DIGVI962/Great-Sage.git
   cd Great-Sage
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   Or, if using `pyproject.toml`:
   ```bash
   pip install .
   ```

4. **Set up environment variables (optional):**
   - Create a `.env` file in the root directory.
   - Example:
     ```
     DEPLOYMENT_PORT=10000
     ```

---

## Usage

### Run the API server

```bash
uvicorn src.main:app --host 0.0.0.0 --port 10000
```

- The API will be available at `http://localhost:10000`
- The main chat endpoint is: `POST /chat`

### Example API Request

```json
POST /chat
Content-Type: application/json

{
  "query": "Hello, Sage!",
  "user_id": "user_1",
  "session_id": "session_123"
}
```

**Response:**
```json
{
  "status": 200,
  "response": "Agent's reply here",
  "events": [ ... ]
}
```

### Interactive CLI (optional)

- The code includes a CLI conversation loop (commented out in `main.py`).
- To use it, uncomment the `asyncio.run(run_conversation())` line in the `__main__` block and run:
  ```bash
  python src/main.py
  ```

---

## Project Structure

```
Great-Sage/
│
├── logs/                      # Log files
│
├── src/
│   ├── agents/
│   │   ├── data_stores/
│   │   │   └── __init__.py
│   │   │
│   │   ├── tools/
│   │   │   ├── __init__.py
│   │   │   ├── os_tools.py
│   │   │   ├── session_tools.py
│   │   │   └── weather_tools.py
│   │   │
│   │   ├── __init__.py
│   │   ├── os_agent.py
│   │   └── weather_agent.py
│   │
│   ├── helpers/               # DTOs and event helpers
│   │   ├── __init__.py
│   │   ├── LlmEvents.py
│   │   ├── request_dto.py
│   │   └── response_dto.py
│   │
│   ├── __init__.py
│   ├── agent.py               # Root agent definition
│   ├── logging_config.py      # Logging configuration
│   └── main.py                # Main FastAPI app and entry point
│
├── tests/                     # Test suite
│
├── .env.example
├── .gitignore
├── LICENSE
├── pyproject.toml             # Project metadata and dependencies
├── requirements.txt           # (If present) Python dependencies
├── README.md                  # This file
└── uv.lock
```

---

## Configuration

- **Logging:** Configured via `src/logging_config.py`
- **Environment:** Set `DEPLOYMENT_PORT` in `.env` or as an environment variable

---

## Development

- Lint, test, and format your code as needed.
- Extend the agent logic in `src/agent.py` and helpers in `src/helpers/`.

---

## License

See [LICENSE](LICENSE) for details.

---
