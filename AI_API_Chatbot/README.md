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
## Set up Instructions

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
---
## steps to create API Keys.

### 1.Gemini  API Key
1. Visit [Google AI studio](https://aistudio.google.com)
2. Sign in with Google account
3. Click **Get API Key**

Set Environment Variable: 
``` bash 
setx GEMINI_API_KEY "your_gemini_api_key"
```

### 2. Groq API Key
1. Visit[Groq Console](https://console.groq.com)
2. Create an Account and generate the API key.

Set Environment Variable: 
``` bash
setx GROQ_API_KEY "your_groq_api_key"
```
---
### 3. Huggingface API Key
1. Visit[Huggingface.co](https://huggingface.co)
2. Create Acoount and login.
3. Go to **Settings -> Access Tokens** 
3. Provide necessary permissions and Generate Token

Set Environment Variable: 

```bash

setx HUGGINGFACE_API_KEY "your_huggingface_token"
```
---
### 4. Cohere API Keys
1. visit[Cohere DAshboard](https://dashboard.cohere.com)
2. Create Account ang generate API for rquierem purpose.


Set Environment Variable: 
```bash
setx COHERE_API_KEY "your_cohere_api_key"
```
---
### 5. Ollama Setup
Download Ollama from:  [ollama](https://ollama.com)

Start the Ollama Server:
```bash
ollama serve
```
Install the model:
```bash
ollama pull llama2
```
---