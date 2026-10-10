from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate # for using the Prompt Template
from langchain_core.prompts import load_prompt # for loading the prompt from json file

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
 
st.header("Research Paper Summarization Tool")

paper_input = st.selectbox("Select the Research Paper Name",["Attention is all you need",
                        "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
                        "GPT-3: Language Models are Few-Shot Learners",
                        "Diffusion Models Beats Gans on Image Synthesis"])

style_input = st.selectbox("Select the explaination Style",["Beginner Friendly","Technical",
                            "Code-Oriented","Mathematical"])

length_input = st.selectbox("Select the Explaination length",["Short(1-2 paragraphs)",
                            "Medium(3-5 paragraphs)",
                            "Long(detailed Explaination)"])

# Template

template = load_prompt("research_summary_template.json")


# fill the palaceholders
prompt = template.invoke({
    "paper_input":paper_input,
    "style_input":style_input,
    "length_input":length_input
})

if st.button("Let's Dive in"): 
    result = model.invoke(prompt)
    st.write(result.content)


# To Run the files with streamlit we use the command (  streamlit run <file_name/file_relative_path>  ) in the terminal