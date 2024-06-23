import openai
import os

openai.api_key = ""

def chat_with_openai(prompt):
    try:
        # Create a chat completion with OpenAI API
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )

        # Extract the content of the message from the response
        response_content = response.choices[0].message.content

        # Strip any leading or trailing whitespace from the response content
        response_content_stripped = response_content.strip()

        return response_content_stripped

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return "Sorry, something went wrong. Please try again."


if __name__ == "__main__":
    while True:
        user_input = input("ASK ANYTHING >> ")

        if user_input.lower() in ["bye", "quit", "exit"]:
            break

        # Get a response from the OpenAI model
        response = chat_with_openai(user_input)
        print("RESPONSE: ", response)

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load the API key from an environment variable

# def chat_with_the_gpt(prompt):
#     response = client.completions.create(model="davinci-002",
#     prompt=prompt)
#     return response.choices[0].text.strip()

# if __name__ == "__main__":
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ["quit", "exit", "bye"]:
#             break

#         response = chat_with_the_gpt(user_input)
#         print("Chatbot: ", response)

# Review the payment plan on https://platform.openai.com/settings/organization/limits !