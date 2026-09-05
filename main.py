import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv("api.env")

MODEL = "openai/gpt-4o-mini"

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)


def main():
    print("aiBoot chat — type 'exit' to quit")
    messages = []

    while True:
        user_input = input("you> ").strip()
        if user_input.lower() in ("exit", "quit"):
            break
        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
        )
        reply = response.choices[0].message.content
        print(f"ai> {reply}")

        messages.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()
