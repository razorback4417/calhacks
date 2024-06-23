import openai

openai.api_key = ""



def chat_with_the_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]

    )

    return response.choices[0].message['content'].strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_the_gpt(user_input)
        print("Chatbot: ", response)

# Review the payment plan on https://platform.openai.com/settings/organization/limits !
# this file already uploaded on github. Thats why green?
