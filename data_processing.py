"""
TechPath Mentor - Veri İşleme Modülü
Kariyer rehberi dökümanlarını yükleme ve işleme fonksiyonları
"""

import os
import json
import streamlit as st
from langchain_community.document_loaders import JSONLoader 
from langchain.schema import Document
from config import DATA_PATH


def load_documents(data_path=DATA_PATH):
    """
    Veri klasöründeki tüm .json dosyalarını yükler.
    
    Args:
        data_path (str): Veri dosyalarının bulunduğu klasör yolu
        
    Returns:
        list: Yüklenen Document nesnelerinin listesi
    """
    docs = []
    
    if not os.path.exists(data_path):
        st.error(f"❌ Hata: '{data_path}' klasörü bulunamadı.")
        return []

    # Klasördeki tüm .json dosyalarını bul
    json_files = [f for f in os.listdir(data_path) if f.endswith(".json")]
    
    if not json_files:
        st.error(f"❌ Hata: '{data_path}' klasöründe .json dosyası bulunamadı.")
        return []
    
    # Her dosyayı yükle
    for file_name in json_files:
        file_path = os.path.join(data_path, file_name)
        try:
            # Önce JSON'u okuyup formatını kontrol et
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Liste mi yoksa tek obje mi?
            if isinstance(data, list):
                # Liste ise her elemanı işle
                for item in data:
                    if isinstance(item, dict) and 'icerik' in item:
                        doc = Document(
                            page_content=item['icerik'],
                            metadata={
                                'source_file': file_name,
                                'baslik': item.get('baslik', 'Başlıksız')
                            }
                        )
                        docs.append(doc)
            elif isinstance(data, dict) and 'icerik' in data:
                # Tek obje ise direkt ekle
                doc = Document(
                    page_content=data['icerik'],
                    metadata={
                        'source_file': file_name,
                        'baslik': data.get('baslik', 'Başlıksız')
                    }
                )
                docs.append(doc)
            
        except json.JSONDecodeError as e:
            st.error(f"❌ {file_name} JSON format hatası: {e}")
        except Exception as e:
            st.error(f"❌ {file_name} yüklenemedi: {e}")
    
    if docs:
        st.success(f"✅ {len(docs)} döküman başarıyla yüklendi!")
    
    return docs


def get_document_stats(documents):
    """
    Yüklenen dökümanlar hakkında istatistik bilgisi verir.
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