from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.messages import SystemMessage, HumanMessage    #use when using SystemMessage and HumanMessage

chat_template = ChatPromptTemplate([                # here we can also use ChatPromptTemplate.from_messages instead of ChatPromptTemplate
    ("system","You are a helpful {domain} expert."),
    ("human", "Explain in simple terms , what is the {topics}?")

    #The placeholders are not replaced when using this method
    # SystemMessage(content="You are a helpful {domain} expert."),             
    # HumanMessage(content= "Explain in simple terms , what is the {topics}?")
])

prompt = chat_template.invoke({"domain": "Cricket", "topics":"Dusra"})

print(prompt)