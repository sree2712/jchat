import logging

from JochemChat import JochemChat

# Initialize the ChatGPT3 instance
config = {"model": "text-davinci-003",
                  "context": ""}
chatbot = JochemChat(config=config)

# Main program loop
while True:
    # Get user input from the terminal
    user_input = input("User: ")

    # Exit the loop if the user enters 'exit'
    if user_input.lower() == 'exit':
        break

    # Get the response from the ChatGPT3 model
    response = chatbot.chat(user_input)

    # Print the generated response
    print("AI: " + response)

    # Optionally, you can log the response
    logging.info(response)
