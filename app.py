# ==============================================================================
# PROJE ADIM 4: ÇÖZÜM MİMARİNİZ - RAG Pipeline Kodlaması
# ==============================================================================

import os
from langchain_community.document_loaders import TextLoader # Metin dosyalarımızı yüklemek için
from langchain_text_splitters import RecursiveCharacterTextSplitter # Metni parçalara ayırmak için
from langchain_chroma import Chroma # Vektör veritabanı
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI # Google Embedding ve Generation Modelleri
from langchain.chains import RetrievalQA # RAG Zincirini kurmak için
import streamlit as st # Web Arayüzü için

# ------------------------------------------------------------------------------
# 1. VERİ YÜKLEME VE İŞLEME
# ------------------------------------------------------------------------------
# Tüm veri dosyalarını yükler ve tek bir liste haline getirir.
def load_documents(data_path="data"):
    # Teknik Anlatım: Projemizdeki .txt uzantılı tüm kariyer bilgi dosyaları yüklenir.
    # TextLoader, veri setimizi LangChain'in anlayacağı 'Document' formatına çevirir.
    docs = []
    for file_name in os.listdir(data_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(data_path, file_name)
            loader = TextLoader(file_path, encoding='utf-8')
            docs.extend(loader.load())
    return docs

# ------------------------------------------------------------------------------
# 2. RAG MİMARİSİ HAZIRLIĞI
# ------------------------------------------------------------------------------
# RAG pipeline'ının ana bileşenlerini kurar (Embedding, Vektör DB, Zincir).
def setup_rag_pipeline(documents):
    # a. Bölme (Chunking) - Teknik Anlatım: 
    # Metni küçük ve anlamlı parçalara ayırırız (Chunking). 
    # Bu, LLM'in tek seferde işleyebileceği kadar küçük olmalı ve 
    # bağlamı korumak için yeterince büyük olmalıdır. (Chunk size 1000)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(documents)

    # b. Embedding Modeli - Teknik Anlatım: 
    # GoogleGenerativeAIEmbeddings kullanarak metin parçalarını sayısal vektörlere dönüştürürüz.
    # Bu model, anlamsal karşılaştırma için esastır.
    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

    # c. Vektör Veritabanı - Teknik Anlatım: 
    # Vektörleri depolamak ve hızlıca arama yapmak için lokal bir veritabanı olan Chroma kullanılır.
    # 'splits' listesindeki parçalar vektörleştirilir ve DB'ye kaydedilir.
    vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)

    # d. Geri Çağırma (Retriever) - Teknik Anlatım:
    # Kullanıcının sorusuna en çok benzeyen (en yakın vektörler) ilk 4 belge parçasını 
    # (top_k=4) geri çağırması için retriever nesnesini oluştururuz.
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    # e. Generation Modeli - Teknik Anlatım:
    # Soruyu ve geri çağrılan bağlamı işleyecek ana dil modelimiz Gemini-2.5-flash'i seçiyoruz.
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)

    # f. RAG Zinciri (Chain) - Teknik Anlatım:
    # Retriever ve LLM'i birleştiren ana RAG zincirini kurarız. 
    # Bu zincir, bağlamı LLM'e geçirerek halüsinasyonu engeller.
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm, 
        chain_type="stuff", # Geri çağrılan tüm metni tek bir prompt'a sıkıştırır
        retriever=retriever
    )
    return qa_chain

# ------------------------------------------------------------------------------
# 3. STREAMLIT WEB ARAYÜZÜ (PROJE ADIM 5)
# ------------------------------------------------------------------------------

# Başlangıçta RAG zincirini yükle ve Streamlit'in hafızasına kaydet (bir kere çalışması için)
@st.cache_resource
def initialize_chatbot():
    try:
        documents = load_documents()
        qa_chain = setup_rag_pipeline(documents)
        return qa_chain
    except Exception as e:
        st.error(f"Hata: Gemini API Anahtarı eksik veya geçersiz. Lütfen GEMINI_API_KEY çevre değişkenini ayarlayın. Detay: {e}")
        return None

def main():
    st.title("👨‍💻 Kariyer Yolu Asistanı (RAG Chatbot)")
    st.caption("Bu chatbot, yapay zeka ve web geliştirme gibi ana başlıklardaki IT kariyerleri hakkında derlenmiş verilere dayanarak cevaplar üretir.")

    # RAG zincirini yükle
    qa_chain = initialize_chatbot()
    
    if qa_chain is None:
        return

    # Kullanıcıdan Girdi Alma
    query = st.text_input("Öğrencilerin merak ettiği kariyer sorularını buraya yazın:", placeholder="Web geliştirmede hangi backend framework'ler popülerdir?")

    if query:
        with st.spinner("Cevap aranıyor..."):
            # RAG zincirini çalıştırma (Retrieval ve Generation)
            response = qa_chain.invoke(query)
            
            # Sonucu Ekrana Basma
            st.markdown("---")
            st.subheader("Cevap:")
            st.info(response['result'])
            # Teknik İpucu: RAG'ın çalıştığını göstermek için bazen 'source_documents' da gösterilir, 
            # ancak RetrievalQA ile bunu görmek için zincirin farklı bir versiyonu (return_source_documents=True) gerekir.
            st.caption("Cevap, derlenmiş kariyer bilgileri veri setimize dayanarak üretilmiştir.")


if __name__ == "__main__":
    # Gemini API anahtarının kontrolü
    if not os.environ.get("GEMINI_API_KEY"):
        st.error("Lütfen GEMINI_API_KEY çevre değişkenini ayarlayın ve tekrar deneyin.")
    else:
        main()