import argparse
import json
import os
import sys

from dotenv import load_dotenv
from openai import OpenAI

from call_function import available_functions, call_function
from prompts import system_prompt

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if not api_key:
    raise RuntimeError("Issue with api_key, check .env")


def main():
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    # Creates the arguments for the program. The parser creates an instance of the argument parser
    # The parser.add_argument is a method on that object, which is named parser
    # args is what we assigned the parser.parse_args() method to
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="Provide user prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]

    for _ in range(1, 21):
        # print(messages)

        # Creates instance of API responses from API call create() makes the API request
        # and returns a response object.
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
            tools=available_functions,
        )

        message = response.choices[0].message

        messages.append(message)

        if message.tool_calls:
            for tool_call in message.tool_calls:
                function_args = json.loads(tool_call.function.arguments or "{}")
                result_message = call_function(tool_call)

                if result_message["content"] == None:
                    raise Exception("the content of the result is None")
                    break

                if args.verbose == True:
                    print(f"-> {result_message['content']}")

                messages.append(result_message)

        if not response.usage:
            raise RuntimeError("token usage is None")

        prompt_tokens = response.usage.prompt_tokens
        response_tokens = response.usage.completion_tokens

        if args.verbose == True:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {prompt_tokens}")
            print(f"Response tokens: {response_tokens}")

        if not message.tool_calls:
            print(response.choices[0].message.content)
            break
        elif _ == 20:
            sys.exit("finished loop without finishing task")

        # if not message.tool_calls:
        #     break


if __name__ == "__main__":
    main()
