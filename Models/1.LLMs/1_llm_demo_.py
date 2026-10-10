from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

#declaring a model and creating an instance of it
llm = OpenAI(model="model-name")

#invoking the model with the required prompt
response = llm.invoke("What is the GDP rate of India?")

#printing the response of the llm
print(response)