from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

#declaring a model and creating an instance of it
model = ChatOpenAI(model="YOUR_MODEL_NAME",temperature=0.5, max_completion_tokens=100)

'''
    max_completion_tokens -> This parameter controls the maximum length of the generated response in terms of tokens.
    temperature -> This parameter controls the randomness of the model's output.

    For Factual Answers such as Math, Code, Facts 
        use the range of temperature -> 0 to 0.3
    For Balanced Responses such as general QA and explainations
        use the range of temperature -> 0.5 to 0.7
    For Creative Answers such as stories, poems, etc
        use the range of temperature -> 0.9 to 1.2
    For maximum randomness (wild ideas, brainstorming)
        use the range of temperature -> 1.5+'''

#invoking the model with the required prompt
response = model.invoke("What is the GDP Rate of India?")

#printing the response of the model
# print(response) # prints the entire response object along with metadata

print(response.content)