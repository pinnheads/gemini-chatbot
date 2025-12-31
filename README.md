# Chatbot with Google Gemini API

This project is a command-line chatbot that interacts with the Google Gemini API. It allows users to have a conversation with the Gemini model, which can also make function calls based on the prompt.

## Features

- **Interactive Chat:** Engage in conversations with the Gemini model.
- **Function Calling:** The model can make function calls based on the conversation context.
- **Verbose Output:** Option to display token usage for prompts and responses.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt # Assuming a requirements.txt file exists or similar for package management
    ```
    (Self-correction: The project uses `uv.lock` and `pyproject.toml`, so `uv pip install` might be more appropriate if `uv` is installed, or `pip install -e .` if it's a package. For now, I'll assume `pip install -r requirements.txt` for simplicity, but acknowledge this might need adjustment if a `requirements.txt` is not present.)

4.  **Set up your Google Gemini API key:**
    -   Obtain an API key from the Google Cloud Console or AI Studio.
    -   Create a `.env` file in the root directory of the project.
    -   Add your API key to the `.env` file:
        ```
        GEMINI_API_KEY="YOUR_API_KEY_HERE"
        ```

## Usage

Run the chatbot from the command line with your desired prompt:

```bash
python main.py "Your message to the chatbot here."
```

### Verbose Mode

To see detailed token usage for your prompts and the model's responses, use the `--verbose` flag:

```bash
python main.py --verbose "Tell me about large language models."
```

## Project Structure

-   `main.py`: The main entry point for the chatbot application.
-   `config.py`: Contains configuration variables like `SYSTEM_PROMPT`.
-   `call_function.py`: Handles function calls made by the Gemini model.
-   `functions/`: Directory for various functions that the model can call.
-   `calculator/`: Directory for calculator-related functions.
-   `.env`: Stores your API key (not committed to version control).
-   `pyproject.toml`, `uv.lock`: Project dependency management files.
