from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="YOUR_MODEL_NAME", dimensions=32)

docu = [
    "Delhi is the capital of India.",
    "The GDP rate of India is 7.8% as of 2023.",
    "Paris is the capital of France.",
    "The GDP rate of France is 6.5% as of 2023."
]

result = embedding.embed_documents(docu)

print(str(result))