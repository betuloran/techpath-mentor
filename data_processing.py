"""
TechPath Mentor - Veri İşleme Modülü
Kariyer rehberi dökümanlarını yükleme ve işleme fonksiyonları
"""

import os
import streamlit as st
from langchain_community.document_loaders import TextLoader
from config import DATA_PATH


def load_documents(data_path=DATA_PATH):
    """
    Veri klasöründeki tüm .txt dosyalarını yükler.
    
    Args:
        data_path (str): Veri dosyalarının bulunduğu klasör yolu
        
    Returns:
        list: Yüklenen Document nesnelerinin listesi
    """
    docs = []
    
    if not os.path.exists(data_path):
        st.error(f"❌ Hata: '{data_path}' klasörü bulunamadı.")
        return []

    # Klasördeki tüm .txt dosyalarını yükle
    txt_files = [f for f in os.listdir(data_path) if f.endswith(".txt")]
    
    if not txt_files:
        st.error(f"❌ Hata: '{data_path}' klasöründe .txt dosyası bulunamadı.")
        return []
    
    # Her dosyayı yükle
    for file_name in txt_files:
        file_path = os.path.join(data_path, file_name)
        try:
            loader = TextLoader(file_path, encoding='utf-8')
            loaded_docs = loader.load()
            
            # Her belgeye kaynak dosya adını ekle
            for doc in loaded_docs:
                doc.metadata['source_file'] = file_name
            
            docs.extend(loaded_docs)
            
        except Exception as e:
            st.error(f"❌ {file_name} yüklenemedi: {e}")
    
    return docs


def get_document_stats(documents):
    """
    Yüklenen dökümanlar hakkında istatistik bilgisi verir.
    
    Args:
        documents (list): Document nesnelerinin listesi
        
    Returns:
        dict: İstatistik bilgileri içeren dictionary
    """
    if not documents:
        return None
    
    total_chars = sum(len(doc.page_content) for doc in documents)
    source_files = set(doc.metadata.get('source_file', 'Unknown') for doc in documents)
    
    return {
        'total_documents': len(documents),
        'total_characters': total_chars,
        'source_files': list(source_files),
        'avg_doc_length': total_chars // len(documents) if documents else 0
    }