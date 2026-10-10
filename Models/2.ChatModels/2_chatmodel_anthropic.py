from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

#declaring a model and creating an instance of it
model = ChatAnthropic(model="YOUR_MODEL_NAME")

#invoking the model with the required prompt
response = model.invoke("What is the GDP Rate of India?")

#printing the response of the model
# print(response) # prints the entire response object along with metadata
print(response.content)