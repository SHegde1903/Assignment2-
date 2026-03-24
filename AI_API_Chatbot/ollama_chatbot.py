import requests

def query_ollama(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi3",   # ✅ lightweight model
                "prompt": prompt,
                "stream": False
            }
        )
        return response.json().get("response", "No response")
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("🤖 Ollama Chatbot (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break

        print("Bot:", query_ollama(user_input))