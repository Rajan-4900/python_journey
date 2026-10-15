# Rule Based Chat Bot

# Adding Time Zone with Greeting

import datetime
import time

name = input("Enter Your Name: ")
presentH = datetime.datetime.now().hour

if 4 <= presentH < 12:
    print("Good Morning", name)
elif 12 <= presentH < 16:
    print("Good Afternoon: ", name)
elif 16 <= presentH < 20:
    print("Good Evening: ", name)
else:
    print("Good Night: ",name)


# Instructions
print("Welcome to Your Chat Bot! How can I assist you today?")
print("Type 'bye' to end the chat.")

# Chatbot Memory Creation [Dictionary of responce]

responses = {
    "hello":"hi, welcome. How can I help you?",
    "how are you":"I am fine. Thank You",
    "who are you":"I am smart AI ChatBot",
    "happy": "Greate to hear that",
    "what is function": "go to chapter 7 to learn about Functions"
}

# Method/function to get responce of chatbot
def getBotResponse(userQuestion):
    userQuestion = userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]
    return "I am Still In Learning Mode."


# take user input
while True:
    userInput = input("me: ").strip()       # Removes unnecessary spaces from the user input
    reply = getBotResponse(userInput)
    print("Bot response: ", reply)

    if "bye" in userInput.lower():
        print("Bot response: Bye! Have a nice day.")
        break