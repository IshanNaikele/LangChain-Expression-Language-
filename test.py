import os
from dotenv import load_dotenv
load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY:
    print("GEMINI_API_KEY loaded successfully!")
    print(f"Your key starts with: {GEMINI_API_KEY[:4]}...") 
else:
    print("Error: GEMINI_API_KEY not found.")
    
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

try:
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",google_api_key=GEMINI_API_KEY)
    message = HumanMessage(content="Who is Virat Kohli ?")
    response = llm.invoke([message])
    print("API call successful! The model responded with:")
    print(response.content)
except Exception as e:
    print("An error occurred. The API key or configuration might be incorrect.")
    print(f"Error details: {e}")
