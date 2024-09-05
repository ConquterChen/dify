from langchain_community.document_loaders import UnstructuredWordDocumentLoader


def extract_file(url):
    url = '/Users/danika/Desktop/pythonCode/dify/api/storage/' + url
    docs = None

    if url.lower().endswith(".docx"):
        loader = UnstructuredWordDocumentLoader(url, mode="single")
        docs = loader.load()

    return docs
