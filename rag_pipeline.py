"""
TechPath Mentor - RAG Pipeline Modülü
Retrieval-Augmented Generation pipeline'ını oluşturma ve yönetme
"""

import streamlit as st
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

from config import (
    EMBEDDING_MODEL, 
    LLM_MODEL, 
    LLM_TEMPERATURE,
    CHUNK_SIZE, 
    CHUNK_OVERLAP,
    TOP_K_RESULTS,
    SEARCH_TYPE,
    PROMPT_TEMPLATE
)


def setup_rag_pipeline(documents, session_id=None):
    """
    RAG Pipeline'ı oluşturur: Chunking, Embedding, VectorDB, Retriever, LLM
    
    Args:
        documents (list): İşlenecek Document nesnelerinin listesi
        session_id (str): Session benzersiz ID'si (FAISS için kullanılmıyor)
        
    Returns:
        RetrievalQA: Sorgulanabilir RAG chain nesnesi
    """
    try:
        # 1. CHUNKING: Dökümanları parçalara ayır
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
            separators=["\n\n", "\n", ". ", " ", ""]
        )
        splits = text_splitter.split_documents(documents)

        # 2. EMBEDDING: Gemini embedding modeli
        embeddings = GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL)

        # 3. VECTOR DATABASE: FAISS
        vectorstore = FAISS.from_documents(
            documents=splits,
            embedding=embeddings
        )

        # 4. RETRIEVER: Benzerlik araması
        retriever = vectorstore.as_retriever(
            search_type=SEARCH_TYPE,
            search_kwargs={"k": TOP_K_RESULTS}
        )

        # 5. LLM: Gemini generative model
        llm = ChatGoogleGenerativeAI(
            model=LLM_MODEL, 
            temperature=LLM_TEMPERATURE
        )

        # 6. PROMPT TEMPLATE: Custom prompt
        prompt = PromptTemplate(
            template=PROMPT_TEMPLATE,
            input_variables=["context", "question"]
        )

        # 7. RAG CHAIN: Tüm bileşenleri birleştir
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=False,
            chain_type_kwargs={"prompt": prompt}
        )
        
        return qa_chain
        
    except Exception as e:
        st.error(f"❌ RAG Pipeline kurulurken hata oluştu: {type(e).__name__}")
        with st.expander("Hata Detayları"):
            st.code(str(e))
        return None


def get_pipeline_info():
    """
    Pipeline yapılandırması hakkında bilgi döndürür.
    
    Returns:
        dict: Pipeline bilgileri
    """
    return {
        'embedding_model': EMBEDDING_MODEL,
        'llm_model': LLM_MODEL,
        'chunk_size': CHUNK_SIZE,
        'chunk_overlap': CHUNK_OVERLAP,
        'top_k_results': TOP_K_RESULTS,
        'vectorstore': 'FAISS'
    }