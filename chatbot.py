import random
import re
from datetime import datetime

class RuleBasedChatbot:
    def __init__(self):
        self.name = "CodBot"
        self.responses = {
            "greeting": ["Hello! How can I help you today?", "Hi there! What would you like to talk about?", "Hey! I'm here to chat."],
            "goodbye": ["Goodbye! Have a great day!", "See you soon!", "Take care!"],
            "thanks": ["You're welcome!", "Happy to help!", "Anytime!"],
            "help": ["You can ask me about my name, time, date, hobbies, or simply chat with me."],
            "name": ["I'm CodBot, a simple rule-based chatbot created with Python."],
            "hobby": ["I enjoy helping people and answering simple questions."],
            "how_are_you": ["I'm doing well, thanks for asking! How are you?"],
            "default": ["I'm not sure I understand. Could you try asking in a different way?", "Interesting! Tell me more.", "I don't know that yet, but I'm learning."]
        }
        self.rules = [
            (r"\b(hi|hello|hey|good morning|good afternoon|good evening)\b", "greeting"),
            (r"\b(bye|goodbye|see you|exit|quit)\b", "goodbye"),
            (r"\b(thanks|thank you|thx)\b", "thanks"),
            (r"\b(help|what can you do)\b", "help"),
            (r"\b(your name|who are you|what are you called)\b", "name"),
            (r"\b(hobby|hobbies|what do you like)\b", "hobby"),
            (r"\b(how are you|how's it going)\b", "how_are_you")
        ]

    def get_response(self, user_input):
        text = user_input.lower().strip()

        if re.search(r"\b(time|current time)\b", text):
            return "The current time is " + datetime.now().strftime("%I:%M %p") + "."
        if re.search(r"\b(date|today's date|today date)\b", text):
            return "Today's date is " + datetime.now().strftime("%d %B %Y") + "."

        for pattern, intent in self.rules:
            if re.search(pattern, text):
                return random.choice(self.responses[intent])

        if "?" in text:
            return "That's a good question. I can answer only a limited set of predefined questions."
        return random.choice(self.responses["default"])

    def chat(self):
        print("=" * 48)
        print("CodBot - Rule-Based Chatbot")
        print("Type 'exit' or 'bye' to end the conversation.")
        print("=" * 48)

        while True:
            user_input = input("You: ").strip()

            if not user_input:
                print("CodBot: Please type something so we can chat.")
                continue

            response = self.get_response(user_input)
            print(f"CodBot: {response}")

            if re.search(r"\b(bye|goodbye|see you|exit|quit)\b", user_input.lower()):
                break

if __name__ == "__main__":
    RuleBasedChatbot().chat()
