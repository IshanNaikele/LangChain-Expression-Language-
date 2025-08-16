from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from fastapi import FastAPI
import os
from dotenv import load_dotenv
from langserve import add_routes

load_dotenv()
GROQ_API_KEY=os.getenv("GROQ_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

from langchain_groq import ChatGroq
model=ChatGroq(model="openai/gpt-oss-120b",groq_api_key=GROQ_API_KEY)
 
generic_template="Translate the following into {language}"

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system",generic_template),
        ("user",'{text}')
    ]
)

parser = StrOutputParser()

chain = prompt_template | model | parser

app=FastAPI(title="Langchain Server ",version ="1.0",description="A simple API Server using langchian runnable interface")

add_routes(
      app,
      chain,
      path='/chain'
)

if __name__ =="__main__" :
    import uvicorn 
    uvicorn.run(app,host="localhost",port=8000)