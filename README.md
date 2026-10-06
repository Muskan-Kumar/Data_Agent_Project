# Data Agent Project

A work in progress for exploring ride-sharing data with a natural-language SQL agent. The repository currently includes sample CSV data, a PostgreSQL schema and loader, and an early LangChain/Groq question-curation component.

## Repository contents

- `data/` — sample users, vehicles, rides, payments, and ratings CSV files.
- `feed_db.py` — creates PostgreSQL tables and indexes, clears existing rows, then imports all five CSV files.
- `agents/sql_analyst.py` — early question-curation function that uses a Groq chat model.
- `utils/llm_pick.py` — selects a Groq model by level (`low`, `medium`, or `high`).
- `utils/database.py` — reserved for database utilities (currently empty).
- `models/schema.py` — Pydantic state schema for the agent workflow.
- `main.py` — project entry point; currently prints a placeholder greeting.

## Requirements

- Python 3.13 or newer
- PostgreSQL database
- A Groq API key for the LLM component
- `uv` (recommended, because the repository includes `uv.lock`) or `pip`

## Setup

Clone the repository and enter its directory. Create and activate a virtual environment, then install dependencies:

```bash
uv sync
```

Alternatively, with pip:

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate
pip install -r requirements.txt
```

The `requirements.txt` currently lists the LangChain packages only. `pyproject.toml` also declares the project’s PostgreSQL, dotenv, and Pydantic dependencies; `uv sync` installs the declared project dependencies.

## Configure PostgreSQL and Groq

Create a PostgreSQL database, then add a `.env` file in the repository root with the following values:

```dotenv
host=localhost
port=5432
database=your_database_name
user=your_database_user
password=your_database_password
GROQ_API_KEY=your_groq_api_key
```

`feed_db.py` reads the lowercase PostgreSQL variables `host`, `port`, `database`, `user`, and `password`. If `port` is omitted, it defaults to `5432`. The LLM component uses `GROQ_API_KEY` through `langchain-groq`. Keep `.env` private; it is ignored by Git.

## Load the sample data

From the repository root, run:

```bash
python feed_db.py
```

The script creates the `public` schema tables and indexes, truncates the five tables, loads the CSV files from `data/`, prints record counts, and commits the transaction. **Running it again replaces the existing rows in those tables.** Back up any data you need before running it against a database with existing records.

## Current status

This repository is an early-stage project. The SQL agent workflow and database query execution are not yet wired into the project entry point. `main.py` currently prints a greeting, and the installed `data-agent-project` command points to that placeholder. The agent schema also defines fields that callers must provide when constructing its state.

The model picker currently maps levels as follows:

| Level | Groq model |
| --- | --- |
| `low` | `openai/gpt-oss-20b` |
| `medium` | `qwen/qwen3.8-27b` |
| `high` | `openai/gpt-oss-120b` |

Calling `utils/llm_pick.py` directly currently instantiates a model and sends a sample prompt. Importing it also does this, so the module has a demonstration side effect.

## Data model

The sample data and loader cover five related tables:

- `users` — riders and drivers
- `vehicles` — vehicles associated with driver user IDs
- `rides` — rider, driver, trip timing, coordinates, distance, fare, and status
- `payments` — payment details associated with rides and users
- `ratings` — rider feedback and a one-to-five rating for rides and drivers

Foreign keys connect these records, and indexes support common lookups by driver, rider, ride, status, and timestamp.
