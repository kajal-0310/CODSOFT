print("AI Chatbot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you?")

    elif "your name" in user:
        print("Bot: I am a simple AI chatbot created for CodSoft Internship.")

    elif "how are you" in user:
        print("Bot: I am fine! Thank you for asking.")

    elif "course" in user or "internship" in user:
        print("Bot: This is an Artificial Intelligence internship project.")

    elif "help" in user:
        print("Bot: You can ask me about AI, internship or greetings.")

    elif user == "bye":
        print("Bot: Goodbye! Have a great day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")