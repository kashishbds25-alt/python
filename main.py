def get_user_input():
    """Take input from the user."""
    return input("You: ").strip().lower()


def get_response(user_input):
    """Find and return the appropriate chatbot response."""

    if user_input in ["hi", "hello", "hey"]:
        return "Hello! How can I help you today?"

    elif user_input == "what is data science":
        return ("Data Science is a field that uses data, programming, "
                "statistics and analytical methods to find useful insights.")

    elif user_input == "what is python":
        return ("Python is a high-level, easy-to-learn programming language "
                "used for web development, data science, automation and AI.")

    elif user_input == "how are you":
        return "I'm doing great! How can I help you?"

    elif user_input in ["bye", "goodbye"]:
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand that question."


def display_response(response):
    """Display the chatbot's response."""
    print("Bot:", response)


def main():
    """Control the complete chatbot flow."""

    print("Bot: Hello! Welcome to the Chatbot.")
    print("Bot: How can I help you?")
    print("Bot: Type 'exit' to end the conversation.")

    while True:
        user_input = get_user_input()

        if user_input == "exit":
            display_response("Thank you for chatting. Goodbye!")
            break

        response = get_response(user_input)
        display_response(response)


# Start the chatbot
if __name__ == "__main__":
    main()