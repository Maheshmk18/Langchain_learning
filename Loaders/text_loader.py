from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt = ChatPromptTemplate([

    ("system","you are a helpful assistant"),

    ("human", "Summarize the text given in about 50 words\n{text}")
    
])

parser = StrOutputParser()

loader = TextLoader("rambo.txt", encoding="utf-8")

doc = loader.load()

print(doc[0].page_content)

print(len(doc))

print(type(doc))

print(type(doc[0]))

chain = prompt | model | parser

prompt1 = chain.invoke({"text": doc[0].page_content})

print(prompt1)