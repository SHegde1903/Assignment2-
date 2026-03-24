import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Hugging Face Router API
API_URL = "https://router.huggingface.co/v1/chat/completions"

# Get API key from .env
HF_TOKEN = os.getenv("HUGGINGFACE_API_KEY")

# Request headers
headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}


# Function to send query to Hugging Face
def query_api(prompt):
    try:
        data = {
            "model": "meta-llama/Meta-Llama-3-8B-Instruct",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 200
        }

        response = requests.post(API_URL, headers=headers, json=data)
        result = response.json()

        # Return chatbot response
        if "choices" in result:
            return result["choices"][0]["message"]["content"].strip()
        else:
            return f"API Error: {result}"

    except Exception as e:
        return f"Error: {str(e)}"


# Main chatbot loop
def main():
    print("Hugging Face Chat App (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break

        reply = query_api(user_input)
        print("Bot:", reply)


# Run program
if __name__ == "__main__":
    main()