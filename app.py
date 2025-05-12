import random
from datetime import datetime

class PythonChatbot:
    def __init__(self):
        self.responses = {
            "greet": ["Hey! I'm your Python Bot", "Hi there!", "Hello!"],
            "time": [f"It's {datetime.now().strftime('%I:%M %p')}"],
            "date": [f"Today is {datetime.now().strftime('%d %B, %Y')}"],
            "help": ["I can tell time/date", "Ask me anything!"],
            "default": ["Sorry, didn't get that", "Try asking differently"]
        }
    
    def reply(self, user_input):
        user_input = user_input.lower().strip()
        
        if any(w in user_input for w in ["hi", "hello", "hey"]):
            return random.choice(self.responses["greet"])
        
        elif "time" in user_input:
            return random.choice(self.responses["time"])
        
        elif "date" in user_input:
            return random.choice(self.responses["date"])
        
        elif "help" in user_input:
            return random.choice(self.responses["help"])
        
        else:
            return random.choice(self.responses["default"])

# Run the bot
if __name__ == "__main__":
    bot = PythonChatbot()
    print("Bot: Type 'exit' to quit\n" + bot.reply("hi"))
    
    while True:
        user_msg = input("You: ")
        if user_msg.lower() == "exit":
            print("Bot: Goodbye!")
            break
        print("Bot:", bot.reply(user_msg))


"""
Chatbot Project
Developer: Umema Sultan
Created Date: 12-05-2025
Description: A rule-based chatbot implemented in Python.
"""