from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.7,max_completion_tokens=100)

st.header("Research Tool with Google Gemini")

user_input = st.text_input("Enter the Research topic")

if st.button("Let's Research"):
    result = model.invoke(user_input)
    # st.text("Some random text")
    st.write(result.content)


# To Run the files with streamlit we use the command (  streamlit run <file_name/file_relative_path>  ) in the terminal