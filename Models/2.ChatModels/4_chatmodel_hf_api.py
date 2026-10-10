from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
# Hugging Face Endpoint is used when we want to use a custom deployed model on Hugging Face Inference API
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.1-8B-Instruct",
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the GDP Rate of India?")

print(result.content)