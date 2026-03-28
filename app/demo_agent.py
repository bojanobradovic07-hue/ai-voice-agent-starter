import random

class VoiceAgent:
    def __init__(self, name="AI Sales Agent"):
        self.name = name

    def respond(self, user_input):
        responses = [
            "Interesting, can you tell me more about your current setup?",
            "That makes sense. Many of our clients had the same issue.",
            "We usually help reduce costs by optimizing supply processes.",
            "Would you be open to a short demo call this week?"
        ]
        return random.choice(responses)


def simulate_call():
    agent = VoiceAgent()
    print(f"{agent.name}: Hello, this is an AI assistant calling regarding your toner supply.")

    while True:
        user_input = input("User: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Call ended.")
            break

        response = agent.respond(user_input)
        print(f"{agent.name}: {response}")


if __name__ == "__main__":
    simulate_call()
