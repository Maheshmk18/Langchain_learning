from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="Reviews.csv",encoding = "utf-8")

docs = loader.load()

print(docs)