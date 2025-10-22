"""
TechPath Mentor - Yapılandırma Dosyası
Proje sabitleri, model isimleri ve yapılandırma ayarları
"""

import os
from dotenv import load_dotenv

# Ortam değişkenlerini yükle
load_dotenv()

# API Anahtarları - Streamlit import ETME!
def get_gemini_api_key():
    """
    API key'i al - Streamlit secrets veya .env'den
    """
    # Önce environment variable'dan dene
    api_key = os.getenv("GEMINI_API_KEY")
    
    # Eğer yoksa ve Streamlit Cloud'daysa secrets'tan al
    if not api_key:
        try:
            import streamlit as st
            if hasattr(st, 'secrets') and "GEMINI_API_KEY" in st.secrets:
                api_key = st.secrets["GEMINI_API_KEY"]
        except:
            pass
    
    return api_key

# API key'i function olarak tut, direkt atama yapma
GEMINI_API_KEY = None  # Bu sonra doldurulacak

# Model Ayarları
EMBEDDING_MODEL = "models/text-embedding-004"
LLM_MODEL = "gemini-2.0-flash-exp"
LLM_TEMPERATURE = 0.4

# Veri İşleme Ayarları
DATA_PATH = "data"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 300

# Retriever Ayarları
TOP_K_RESULTS = 5
SEARCH_TYPE = "similarity"

# Prompt Template
PROMPT_TEMPLATE = """Sen bilgisayar mühendisliği öğrencilerine kariyer rehberliği yapan uzman bir danışmansın.

Aşağıdaki BİLGİ BANKASI belgelerini DİKKATLİCE oku ve soruyu bu belgelere DAYANDIRARAK yanıtla.

BİLGİ BANKASI:
{context}

ÖĞRENCİNİN SORUSU: {question}

YANITLAMA KURALLARI:
1. Yanıtını SADECE yukarıdaki bilgi bankası belgelerine dayandır
2. Eğer belgeler yeterli bilgi içermiyorsa, "Bu konuda veri setimde yeterli detaylı bilgi bulamadım" de
3. Bilgi varsa, DETAYLI, AÇIKLAYICI ve YAPILANDIRICI bir şekilde anlat
4. Framework, araç, dil isimleri sorarsa, belgelerde geçenleri listele
5. Öğrenciye rehberlik eder gibi, samimi ve öğretici bir ton kullan
6. Liste yapacaksan, madde madde yaz
7. Yanıtın en az 3-4 paragraf olsun
8. Türkçe karakter kullan

YANITINIZ:"""

# Uygulama Bilgileri
APP_TITLE = "👨‍💻 Kariyer Yolu Asistanı (RAG Chatbot)"
APP_CAPTION = "Bu chatbot, yapay zeka ve web geliştirme gibi ana başlıklardaki IT kariyerleri hakkında derlenmiş verilere dayanarak cevaplar üretir."
APP_VERSION = "v1.0"