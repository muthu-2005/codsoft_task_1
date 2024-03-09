import random
def simple_chatbot(user_input):
    greetings = ["hello", "hi", "hey", "greetings"]
    farewells = ["bye", "goodbye", "see you", "farewell"]
    questions = ["how are you?", "what's up", "how are you doing"]
    jokes = ["Tell me a joke", "Can you make me laugh", "Say something funny"]

    user_input = user_input.lower()
    if any(greeting in user_input for greeting in greetings):
        return random.choice(["Hello!", "Hi there!", "Hey!"])

    elif any(farewell in user_input for farewell in farewells):
        return random.choice(["Goodbye!", "See you later!", "Farewell!"])

    elif any(question in user_input for question in questions):
        return random.choice(["I'm doing well, thanks!", "Everything's good.", "Not bad, you?"])

    else:
        return "I'm a simple chatbot. Feel free to ask me anything!"
print("Chatbot: Hello! I'm a responsive chatbot.")

while True:
    user_query = input("User: ")
    
    if user_query.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    
    response = simple_chatbot(user_query)
    print("Chatbot:", response)
