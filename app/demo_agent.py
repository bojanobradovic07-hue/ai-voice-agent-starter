import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are a professional German-speaking AI sales agent specialized in toner products for businesses.

Your goals:
1. Greet the customer naturally
2. Identify printer model / setup
3. Understand customer needs
4. Suggest a suitable toner option
5. Move the conversation toward a next step

Style:
- concise
- natural
- polite
- sales-oriented
- practical, not pushy
"""

def chat_with_agent(conversation_history):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation_history,
    )
    return response.choices[0].message.content


def main():
    print("AI Sales Agent started. Type 'quit' to exit.\n")

    conversation_history = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    while True:
        user_input = input("You: ")

        if user_input.lower().strip() == "quit":
            print("Call ended.")
            break

        conversation_history.append({"role": "user", "content": user_input})
        reply = chat_with_agent(conversation_history)
        conversation_history.append({"role": "assistant", "content": reply})

        print(f"Agent: {reply}\n")


if __name__ == "__main__":
    main()