from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="YOUR_MODEL_NAME", dimensions=32)

result = embedding.embed_query("What is the GDP Rate of India?")

print(str(result))