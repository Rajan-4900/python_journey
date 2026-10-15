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
    "what is function": "go to chapter 7 to learn about Functions",
    # Adding 3 new questions and responses
    "what is your name":"I am A ChatBot created by Rajan",
    "what is your age": "I am a chatbot, I don't have Age, But Recently I was created in 2026",
    "sad": "I am sorry to hear that. I hope you feel better soon! How can I help You To be Happy?"
}

# Method/function to get responce of chatbot
def getBotResponse(userQuestion):
    userQuestion = userQuestion
    for eachkey in responses:
        if eachkey in userQuestion:
            time.sleep(1)  # Adding a delay of 1 second before responding
            return responses[eachkey]
    return "I am Still In Learning Mode."


# take user input
while True:
    userInput = input("me: ").strip()   # it is used to remove the unnecessary spaces from the user input  
    reply = getBotResponse(userInput)
    print("Bot response: ", reply)

    if "bye" in userInput.lower():
        print("Bot response: Bye! Have a nice day.")
        break

#  1Q. Add at least 3 new questions and responses to the chatbot.
#  2Q. Add logic to respond differently if the user says "sad" or "happy"
#  3Q. Add a delay (1 second) between questions and answer using time.sleep().