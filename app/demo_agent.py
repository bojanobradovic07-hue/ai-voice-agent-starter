import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_with_agent(user_input):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional AI sales agent for toner products."},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content


def main():
    print("AI Sales Agent started. Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "quit":
            print("Call ended.")
            break

        reply = chat_with_agent(user_input)
        print(f"Agent: {reply}\n")


if __name__ == "__main__":
    main()