from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

#declaring a model and creating an instance of it
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.7,max_completion_tokens=100)

#invoking the model with the required prompt
response = model.invoke("What is the GDP Rate of India?")

#printing the response of the model
# print(response) # prints the entire response object along with metadata

print(response.content)