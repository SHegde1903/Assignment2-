import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ ERROR: API key not found. Check your .env file.")
    exit()

print("✅ API key loaded successfully!")

# Create Gemini client
client = genai.Client(api_key=api_key)

print("\n🤖 Gemini Chatbot Started (type 'exit' to quit)\n")

while True:
    user_prompt = input("You: ")

    if user_prompt.lower() in ["exit", "quit", "bye"]:
        print("👋 Exiting... Goodbye!")
        break

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_prompt
        )

        print("Gemini:", response.text)

    except Exception as e:
        print("Error:", e)