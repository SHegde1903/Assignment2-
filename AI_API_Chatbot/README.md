# AI API Integration Chatbot project using python

## Project Description:
The project demonstrate the usage of AI API's to  create a simple chatbot using python. each program uses different AI providers where the user can use the API key to send request to the AI and get a AI generated response .

### The project Includes the following Programs:
- `gemini_chatbot.py ` - Using google gemini API.
- ` groq_chatbot.py ` - Using Groq API.
- ` huggingface_chatbot.py ` - Using Huggingface API.
- ` Ollama_chatbot.py ` - Using Ollama local model.
- ` cohere_chatbot.py ` - Using Cohere API.
- ` multiple_api_chatbot.py ` - Program using all the above API to interact with the user.

---
## 1. Creating the Virtual Environment.
``` bash
python -m venv venv 
```

### 2. Activate the environment.
``` bash
venv\Scripts\activate
```

### 3. Install required Libraries.

``` bash
pip install requestes
pip install google-generativeai
pip install cohere
pip install groq
pip install python-dotenv
```
### 4. steps to create API Keys.
```markdown
 Gemini  API Key
1. Visit [Google AI studio ] (https://aistudio.google.com)
2. Sign in with Google account
3. Click **Get API Key**