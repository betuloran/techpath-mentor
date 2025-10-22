"""
TechPath Mentor - Ana Uygulama Dosyası
"""

import os
import streamlit as st
from dotenv import load_dotenv

from config import APP_TITLE, APP_CAPTION, APP_VERSION, GEMINI_API_KEY
from data_processing import load_documents
from rag_pipeline import setup_rag_pipeline, get_pipeline_info

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ""
load_dotenv()


# ============================================================================
# CUSTOM CSS 🎨
# ============================================================================
def load_custom_css():
    st.markdown("""
    <style>
    /* Ana tema renkleri */
    :root {
        --primary-color: #667eea;
        --secondary-color: #764ba2;
        --background-color: #f7f9fc;
        --card-background: #ffffff;
        --text-primary: #1e293b;
        --text-secondary: #64748b;
    }
    
    /* Ana başlık */
    h1 {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 2.5rem !important;
        margin-bottom: 0.5rem;
    }
    
    /* Chat mesajları */
    .stChatMessage {
        background-color: var(--card-background);
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        border: 1px solid #e2e8f0;
    }
    
    /* Kullanıcı mesajı */
    .stChatMessage[data-testid="user-message"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    /* Bot mesajı */
    .stChatMessage[data-testid="assistant-message"] {
        background-color: #f8fafc;
        border-left: 4px solid #667eea;
    }
    
    /* Chat input */
    .stChatInputContainer {
        border-radius: 24px;
        border: 2px solid #e2e8f0;
        padding: 0.5rem;
        background-color: white;
    }
    
    .stChatInputContainer:focus-within {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    [data-testid="stSidebar"] .stMarkdown {
        color: white;
    }
    
    [data-testid="stSidebar"] h2 {
        color: white !important;
        font-weight: 700;
    }
    
    /* Info box */
    .stAlert {
        border-radius: 12px;
        border: none;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    
    /* Butonlar */
    .stButton button {
        border-radius: 20px;
        font-weight: 600;
        transition: all 0.3s ease;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
    }
    
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
    }
    
    /* Spinner */
    .stSpinner > div {
        border-top-color: #667eea !important;
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #5a67d8;
    }
    
    /* Caption */
    .stCaption {
        color: var(--text-secondary);
        font-size: 0.95rem;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        font-weight: 600;
        color: var(--text-primary);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem 0;
        color: var(--text-secondary);
        border-top: 1px solid #e2e8f0;
        margin-top: 3rem;
    }
    </style>
    """, unsafe_allow_html=True)

# ============================================================================
# CHATBOT BAŞLATMA
# ============================================================================
@st.cache_resource
def initialize_chatbot():
    if not GEMINI_API_KEY:
        st.error("❌ GEMINI_API_KEY .env dosyasında bulunmalıdır.")
        return None
    
    os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY
    
    # Session için benzersiz ID oluştur (sadece ilk çağrıda)
    if 'session_id' not in st.session_state:
        import time
        st.session_state.session_id = f"session_{int(time.time())}"
    
    try:
        with st.spinner("🚀 Chatbot hazırlanıyor..."):
            documents = load_documents()
            if not documents:
                return None
            # Session ID'yi pipeline'a gönder
            qa_chain = setup_rag_pipeline(documents, st.session_state.session_id)
        st.success("✅ Chatbot hazır! Sorularınızı sorabilirsiniz.")
        return qa_chain
    except Exception as e:
        st.error(f"❌ Hata: {e}")
        return None

# ============================================================================
# ANA UYGULAMA
# ============================================================================
def main():
    # Sayfa yapılandırması
    st.set_page_config(
        page_title="TechPath Mentor",
        page_icon="🎯",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS yükle
    load_custom_css()
    
    # Header
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title("TechPath Mentor")
        st.caption("🌟 Bilgisayar Mühendisliği Kariyer Rehberi | Yapay Zeka Destekli Asistan 🌟")
    
    # CHATBOT'U BAŞLAT  
    qa_chain = initialize_chatbot()
    if qa_chain is None:
        st.warning("⚠️ Chatbot başlatılamadı. Lütfen hata mesajlarını kontrol edin.")
        return

    # Sidebar
    with st.sidebar:
        st.markdown("""
        <div style='text-align: center; padding: 2rem 0;'>
            <div style='font-size: 4rem;'>🎯</div>
            <h2 style='margin-top: 1rem; color: white;'>TechPath Mentor</h2>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Kapsam
        st.markdown("### 📚 Kapsam Alanlarından Örnekler")
        areas = [
            ("🤖", "AI & Veri Bilimi", "Python, TensorFlow, PyTorch"),
            ("🌐", "Web Geliştirme", "React, Node.js, Django"),
            ("🔒", "Siber Güvenlik", "Pentesting, SOC, Sertifikalar"),
            ("🏢", "Kurumsal IT", "Banka, Telekom Rolleri"),
            ("☁️", "Bulut Bilişim", "AWS, Azure, GCP"),
            ("📱", "Mobil Geliştirme", "iOS, Android, Flutter"),
            ("🛠️", "DevOps & Altyapı", "CI/CD, Docker, Kubernetes"),
            ("🎮", "Oyun Geliştirme", "Unity, Unreal Engine, C#"),
            ("📊", "Veri Analitiği", "SQL, Tableau, Power BI"),
            ("🧠", "Makine Öğrenimi", "Scikit-learn, XGBoost, ML Ops")
            

        ]
        
        for emoji, title, desc in areas:
            st.markdown(f"""
            <div style='background: rgba(255,255,255,0.1); 
                        padding: 1rem; 
                        border-radius: 12px; 
                        margin: 0.5rem 0;
                        border-left: 3px solid white;'>
                <strong>{emoji} {title}</strong><br>
                <small style='opacity: 0.8;'>{desc}</small>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Örnek sorular
        st.markdown("### 💡 Örnek Sorular")
        example_questions = [
            "Web geliştirmede hangi frameworkler var?",
            "React nedir ve nerede kullanılır?",
            "Siber güvenlik için hangi sertifikalar?",
            "Data Science için Python'da ne öğrenmeliyim?"
        ]
        
        for i, q in enumerate(example_questions, 1):
            if st.button(f"💬 {q[:30]}...", key=f"example_{i}", use_container_width=True):
                st.session_state.example_query = q
                st.rerun()
        
        st.markdown("---")
        
        # Teknik detaylar
        with st.expander("⚙️ Teknik Bilgiler"):
            pipeline_info = get_pipeline_info()
            for key, value in pipeline_info.items():
                st.text(f"{key}: {value}")
        
        st.markdown("---")
        st.markdown(f"""
        <div style='text-align: center; color: rgba(255,255,255,0.7);'>
            <small>Version {APP_VERSION}</small><br>
            <small>Akbank GenAI Bootcamp 2025</small>
        </div>
        """, unsafe_allow_html=True)

    # Ana chat alanı
    st.markdown("---")
    
    # Session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # ⭐ ÖRNEK SORU İŞLEME - ARTIK qa_chain ERİŞİLEBİLİR! ⭐
    if hasattr(st.session_state, 'example_query'):
        example_prompt = st.session_state.example_query
        delattr(st.session_state, 'example_query')
        
        # Kullanıcı mesajını ekle
        st.session_state.messages.append({"role": "user", "content": example_prompt})
        
        # Bot yanıtını oluştur
        with st.spinner("🤔 Düşünüyorum..."):
            try:
                response = qa_chain.invoke(example_prompt)  # ← ARTIK ÇALIŞIR!
                answer = response['result']
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                error_msg = f"😔 Üzgünüm, bir hata oluştu: {str(e)}"
                st.session_state.messages.append({"role": "assistant", "content": error_msg})
        
        st.rerun()
    
    # Chat geçmişi
    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar="👤" if message["role"] == "user" else "🤖"):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("💬 Kariyer hakkında merak ettiğin bir şey sor..."):
        # Kullanıcı mesajı
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar="👤"):
            st.markdown(prompt)
        
        # Bot yanıtı
        with st.chat_message("assistant", avatar="🤖"):
            # Basit selamlamaları kontrol et
            simple_greetings = [
                "merhaba", "selam", "hey", "hi", "hello", 
                "günaydın", "iyi günler", "selamlar", "slm"
            ]
            prompt_lower = prompt.lower().strip().rstrip("!?.,:;")
            
            # Basit selamlama mı?
            is_greeting = (
                prompt_lower in simple_greetings or 
                len(prompt.split()) <= 2 and any(g in prompt_lower for g in simple_greetings)
            )
            
            if is_greeting:
                # Kısa karşılama mesajı
                welcome_msg = """👋 **Merhaba!** Bugün ne öğrenmek istersin? 🚀"""
                
                st.markdown(welcome_msg)
                st.session_state.messages.append({"role": "assistant", "content": welcome_msg})
            
            else:
                # Normal RAG sorgusu
                with st.spinner("🤔 Düşünüyorum..."):
                    try:
                        response = qa_chain.invoke(prompt)
                        answer = response['result']
                        st.markdown(answer)
                        st.session_state.messages.append({"role": "assistant", "content": answer})
                    except Exception as e:
                        error_msg = f"😔 Üzgünüm, bir hata oluştu: {str(e)}"
                        st.error(error_msg)
                        st.session_state.messages.append({"role": "assistant", "content": error_msg})
    
    # Welcome message (ilk açılışta)
    if len(st.session_state.messages) == 0:
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown("""
            👋 **Merhaba! Ben TechPath Mentor.**
            
            Sana bilgisayar mühendisliği kariyeri hakkında yardımcı olabilirim. 
            
            🎯 **Sorabilecekleriniz:**
            - Hangi teknolojileri öğrenmeliyim?
            - Kariyer yolları nelerdir?
            - Frameworkler, araçlar, sertifikalar...
            
            Hadi başlayalım! Merak ettiğin bir şey sor 👇
            """)


if __name__ == "__main__":
    main()