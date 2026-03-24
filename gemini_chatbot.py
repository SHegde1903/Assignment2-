import os
from dotenv import load_dotenv
import google.generativeai as genai

# ✅ Load .env file (IMPORTANT)
load_dotenv(dotenv_path=".env")

# ✅ Get API key
api_key = os.getenv("GOOGLE_API_KEY")

# ✅ Debug check (remove later if you want)
if not api_key:
    print("❌ ERROR: API key not found. Check your .env file.")
    exit()
else:
    print("✅ API key loaded successfully!")

# ✅ Configure Gemini
genai.configure(api_key=api_key)

# ✅ Load model
model = genai.GenerativeModel("gemini-2.5-flash")

# ✅ Function to query Gemini
def query_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# ✅ Main chatbot loop
if __name__ == "__main__":
    print("\n🤖 Gemini Chatbot Started (type 'exit' to quit)\n")

    while True:
        user_prompt = input("You: ")

        # ✅ Exit condition
        if user_prompt.lower() in ["exit", "quit", "bye"]:
            print("👋 Exiting... Goodbye!")
            break

        print("Gemini: ", end="")

        result = query_gemini(user_prompt)
        print(result)