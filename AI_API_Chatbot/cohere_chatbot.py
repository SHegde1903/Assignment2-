import cohere

# Initialize Cohere client
co = cohere.ClientV2(api_key="HuARKGtJ0QXWDWRaAwy4NzyWzLyvCWGhrI5zDo6T")

print("AI Chatbot (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    # Exit condition
    if user_input.lower() == "exit":
        print("Exiting chatbot... Goodbye!")
        break

    try:
        # Send request to Cohere
        res = co.chat(
            model="command-a-03-2025",
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
        )

        # Print response
        print("AI:", res.message.content[0].text)

    except Exception as e:
        print("Error:", str(e))