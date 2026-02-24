from .tools.add_data import add_data
from .tools.create_corpus import create_corpus
from .tools.delete_corpus import delete_corpus
from .tools.delete_document import delete_document
from .tools.get_corpus_info import get_corpus_info
from .tools.list_corpora import list_corpora
from .tools.rag_query import rag_query

root_agent = Agent{
    name = "RAG_Agent",
    # Using Gemini 2.5 Flash for best performance with RAG operations
    model = "gemini-2.5-flash-preview-04-17",
    description = "An agent that uses Retrieval-Augmented Generation (RAG) to answer questions based on custom data corpora.",
    tools = [
        rag_query,
        list_corpora,
        create_corpus,
        add_data,
        get_corpus_info,
        delete_corpus,
        delete_document,
    ],
    instructions = """
    # Vertex AI RAG Agent Instructions
    You are a helpful RAG agent that can interact with Vertex AI's document corpora.
    You can retrieve information from corpora, list available corpora, create new corpora, add new documents to corpora, gete detailed information about specifici corpora, delete specifici documents from corpora,
    and delete entire corpora when they are no londer needed.

    # Your Capabilities
    1. **Query Documents**: You can answer questions by retrieving relevant information from document.
    2. **List Corpora**: You can list all available document corpora to help users understand what 
    3. **Create Corpora**: You can create new document corpora for prgaizing information.
    4. **Add new data**: You can add new documents to existing corpora.
    5. **Get Corpus Info**: You can provide detailed information about.

    """

}