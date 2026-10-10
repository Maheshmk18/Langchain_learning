from langchain_core.prompts import PromptTemplate

# Template

template = PromptTemplate(
    input_variables = ["paper_input","style_input","length_input"],
    template = """ Please Summarize the research paper named "{paper_input} with the following specifications:
    Explaination style : {style_input}
    Explaination Length : {length_input}
    1.Mathematical Details:
    - Include relevant mathematical eqations if present in the paper.
    - Include the mathematical concepts using simple, intutive code Snippets where applicable.
    2.Analogies
    - Use relatable analogies to simplify the complex ideas.
    If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.
    Ensure the summary is clear, consise ,accurate and aligned with the provided style and length.""",
    validate_template = True
)

template.save("research_summary_template.json")