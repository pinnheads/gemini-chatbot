import os
import argparse
from google import genai
from google.genai import types
from config import SYSTEM_PROMPT
from functions.get_files_info import schema_get_files_info

from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key is None:
    raise RuntimeError(
        "ERROR: Couldn't load api_key!. Please check the .env file."
    )

client = genai.Client(api_key=api_key)
parser = argparse.ArgumentParser(description='Chatbot')
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true",
                    help="Enable verbose output")
args = parser.parse_args()
messages = [types.Content(
    role="user", parts=[types.Part(text=args.user_prompt)])]

available_functions = types.Tool(
    function_declarations=[schema_get_files_info],
)

answer = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=messages,
    config=types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=SYSTEM_PROMPT
    ),
)

if answer.usage_metadata is None:
    raise RuntimeError(
        "ERROR: There was an error when connecting to gemini api!. Please try again in some time."
    )


if args.verbose is True:
    print(f"User prompt: {args.user_prompt}")
    print(f"Prompt tokens: {answer.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {answer.usage_metadata.candidates_token_count}")

print(f"Response: {answer.text}")
if answer.function_calls is not None:
    for function_call in answer.function_calls:
        print(f"Calling function: {function_call.name}({function_call.args})")
