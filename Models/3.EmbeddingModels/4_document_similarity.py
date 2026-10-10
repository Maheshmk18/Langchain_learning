from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting style and leadership qualities.",
    "Sachin Tendulkar, often referred to as the 'God of Cricket', is one of the greatest batsmen in the history of cricket.",
    "M.S. Dhoni is a former Indian cricket team captain, renowned for his calm demeanor and finishing abilities.",
    "Rohit Sharma is an Indian cricketer famous for his elegant batting and multiple double centuries in One Day Internationals.",
    "Jasprit Bumrah is an Indian fast bowler known for his unique bowling action and ability to bowl yorkers at will."
]

query = "Who is known as the M.S.D?"

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

similarity = cosine_similarity([query_embedding], doc_embeddings) # since both the inputs need to be 2D arrays

# to see similarity scores
print(similarity)

# but we do not need complete 2D array we just need the first row
scores = similarity[0]

#to view what we are taking/storing in scores variable
print(scores)

Score_list = list(enumerate(scores))
# to view what we are taking/storing in Score_list variable
print(Score_list)

# sorting the scores in ascending order
sorted_scores = sorted(Score_list, key=lambda x:x[1])
print(sorted_scores)
# we need only the largest score
highest_score = sorted_scores[-1]

print("\nUser Query:")
print(query)
print(f"The most similar document is: \n'{documents[highest_score[0]]}'\nIt has a similarity score of {highest_score[1]}\n")