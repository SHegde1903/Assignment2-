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
1. Visit [Groq Console](https://console.groq.com)
2. Create an Account and generate the API key.

Set Environment Variable: 
``` bash
setx GROQ_API_KEY "your_groq_api_key"
```
---
### 3. Huggingface API Key
1. Visit [Huggingface.co](https://huggingface.co)
2. Create Acoount and login.
3. Go to **Settings -> Access Tokens** 
3. Provide necessary permissions and Generate Token

Set Environment Variable: 

```bash

setx HUGGINGFACE_API_KEY "your_huggingface_token"
```
---
### 4. Cohere API Keys
1. visit [Cohere Dashboard](https://dashboard.cohere.com)
2. Create Account ang generate API for rquierem purpose.


Set Environment Variable: 
```bash
setx COHERE_API_KEY "your_cohere_api_key"
```
---
### 5. Ollama Setup
Download Ollama from:  [ollama official website ](https://ollama.com)

Start the Ollama Server:
```bash
ollama serve
```
Install the model:
```bash
ollama pull llama2
```
---
## Execution Instruction of the programs.

Navigate to the folder **AI_API_Chatbot ->Activate the Virtual Environment**.
---
### 1. Run Gemini Cahtbot Programm.
```bash 
pythom gemini_chatbot.py 
```
---
### 2. Run Cohere Cahtbot Programm.
```bash 
pythom cohere_chatbot.py 
```
---
### 3. Run Groq Cahtbot Programm.
```bash 
pythom groq_chatbot.py 
```
---
### 4. Run huggingface Cahtbot Programm.
```bash 
pythom huggingface_chatbot.py 
```
---
### 5. Run Gemini Cahtbot Programm.
```bash 
pythom ollama_chatbot.py 
```
---
### 6. Run Gemini Cahtbot Programm.
```bash 
pythom multiple_api_chatbot.py 

```
This program Allow the user to select the AI provider between :
1. Gemini
2. Cohere
3. Groq
4. Huggingface
5. Ollama

once the option selected the user can interact with the chatbot and recieve the generated response. 

If user wants to exit from the program need to type **exit**.

---

## Result Screens of the programs 
### 1. Gemini chatbot program 
![gemini cahtbot result](AI_API_Chatbot\results\gemini.jpeg)
---
### 2. Cohere chatbot program 
![Cohere cahtbot result](E:\campuspe-ai\AI_API_Chatbot\AI_API_Chatbot\results\cohere.png)
---
### 3. Groq chatbot program 
![Groq chatbot result](AI_API_Chatbot\results\groq result.png)
---
### 4. Ollama chatbot program 
![Ollama chatbot result]()
---

### 5. Huggingface chatbot program 
![huggingface chatbot result](AI_API_Chatbot\results\huggingface.png)
---
### 6. Multiple API  chatbot program 
![multiple API query chatbot result](AI_API_Chatbot\results\multiple api.png)
---

