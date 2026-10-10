from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("ABOUT PROJECT.pdf")

docs = loader.load()

print(docs)

print(len(docs))

print(docs[0].page_content)

print(docs[1].metadata)

"""
For 
        simple and clean pdfs -> PyPDFLoader
        scanned/image pdfs -> UnstructuredPDFLoader or AmazonTextractPDFLoader
        pdfs with tables/columns -> PDFPlumberLoader
        need layout or image data -> PyMuPDFLoader
        for structure extraction -> UnstructuredPDFLoader
"""