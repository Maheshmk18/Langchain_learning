from langchain_huggingface import HuggingFaceEmbeddings

'''HuggingFaceEmbeddings class needs another package to actually run the models on your machine.

The "HuggingFaceEmbeddings" class is designed to run embedding models locally on your computer.
 To do this, it uses the powerful sentence-transformers library as its engine.

The "langchain-huggingface" package doesn't automatically install "sentence-transformers" for you,
so you have to install it separately.

You just need to install the required package.
Open your terminal (making sure your (venv) is still active) and run this command:
pip install sentence-transformers

Once you do, "HuggingFaceEmbeddings" will be able to download the model you specified (all-MiniLM-L6-v2)
and use it to create the vector for your text.'''

embedding = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

# text = "Delhi is the capital of India."

docu = [
    "Delhi is the capital of India.",
    "The GDP rate of India is 7.8% as of 2023.",
    "Paris is the capital of France.",
    "The GDP rate of France is 6.5% as of 2023."
]

# vector = embedding.embed_query(text)
vector = embedding.embed_documents(docu)

print(str(vector))