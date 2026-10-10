from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt = ChatPromptTemplate([

    ("system","you are a helpful assistant that answers users queries based on given text"),

    ("human", "Answer the question \n{question}\n from the given text\n{text}")
    
])

parser = StrOutputParser()

url = "https://medium.com/@adityak11g/unlocking-the-art-of-prompt-design-in-vertex-ai-insights-and-techniques-9cf02d51ad1a"

loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

result = chain.invoke({
    "question":"who is the author of the article?",
    "text": docs[0].page_content
})

print(result)
