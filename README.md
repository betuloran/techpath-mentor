# 🎯 TechPath Mentor: Kariyer Yolu Asistanı

Generative AI Bootcamp (2025) için hazırlanmış, IT ve Bilgisayar Mühendisliği kariyer yollarına odaklanan, Türkçe RAG (Retrieval-Augmented Generation) tabanlı bir chatbot projesidir.

## 📋 Proje Hakkında

Bu proje, öğrencilere ve kariyer değiştirenlere yönelik, **özel olarak hazırlanmış Türkçe IT bilgi setlerine** dayanarak rehberlik eden bir yapay zeka asistanı sunar. Gelişmiş RAG mimarisi sayesinde, chatbot, sadece genel model bilgisi yerine, IT dünyasının güncel ve Türkiye ekosistemine özgü terimleri (DevOps, Cloud, Backend, UI/UX, QA, Oyun Geliştirme vb.) içeren yerel veri setlerinden bilgi çekerek, yüksek doğrulukta ve bağlama dayalı yanıtlar üretir.

## 🎓 Projenin Amacı
Modern yazılım dünyasında yüzlerce farklı teknoloji, framework ve kariyer yolu bulunmaktadır. Bu proje:

Öğrencilerin hangi teknolojileri öğrenmeleri gerektiği konusunda bilinçli kararlar almalarını sağlar. <br>
Yeni mezunların kariyer hedeflerine uygun sektörleri ve rolleri keşfetmelerine yardımcı olur. <br>
Güncel bilgiye dayalı, spesifik ve uygulanabilir tavsiyeler sunar. <br>
Sektör trendlerini ve iş ilanlarını analiz ederek gerçekçi kariyer önerileri verir. <br>

### Ana Özellikler

* **Özel Türkçe Veri Setleri:** Global terimlerin yanı sıra, Türkiye IT ekosistemine özel bilgileri içeren JSON veri setleri kullanılır.
* **Bağlamsal Doğruluk:** Kullanıcı sorularına, sadece ilgili bilgi parçalarını (chunks) kullanarak cevap verir, böylece tutarsızlık (hallucination) riski en aza iner.
* **Kolay Kullanım:** Streamlit tabanlı web arayüzü ile hızlı ve etkileşimli bir sohbet deneyimi sunar.
* **Kaynak Gösterimi:** Yanıtların hangi veri setlerine dayandığı gösterilerek güvenilirlik artırılır.

## 🌐 Web Arayüzü & Deployment

#### 1. 💬 Örnek Kullanım Senaryosu: Web Geliştirme Sorgusu <br>

#### Kullanıcı Sorusu:<br>
"Web geliştirmede hangi frameworkler var ve hangisini öğrenmeliyim?" <br>

#### Beklenen Yanıt:<br>
- Backend ve Frontend analizi <br>
- Framework karşılaştırması <br>
- Her birinin kullanım alanları <br>

#### 2. Sidebar'da Tıklanabilir Örnek Sorular

- "Web geliştirmede hangi frameworkler var?"
- "React nedir ve nerede kullanılır?"
- "Siber güvenlik için hangi sertifikalar?"
- "Data Science için Python'da ne öğrenmeliyim?"

#### 3. Basit selamlamalar için (merhaba, selam, hey) RAG pipeline'ı kullanmadan hızlı yanıt

```bash
👋 Merhaba! Bugün ne öğrenmek istersin? 🚀
```

🔗 Canlı Demo Linki


## 📊 Veri Seti Metodolojisi (Derleme ve Kaynaklandırma)

### 🗂️ Veri Kaynağı ve Yapısı
- Proje, 157 adet JSON dokümanı içeren özenle hazırlanmış bir bilgi bankası kullanmaktadır.
- Veri seti 14 ana kategori altında yapılandırılmıştır.
- Veri seti, aşağıdaki kaynaklardan derlenerek oluşturulmuştur:

#### İş İlanları Analizi (LinkedIn, Kariyer.net, Indeed)

- Sektör bazında aranan teknolojiler
- Beklenen beceriler ve sertifikalar
- Maaş aralıkları ve iş tanımları

#### Sektör Raporları

- StackOverflow Developer Survey
- GitHub State of the Octoverse

#### Akademik ve Kurumsal Kaynaklar

- Üniversite müfredatları
- Bootcamp programları
- Sertifika kuruluşları
  
## 🛠️ Kullanılan Teknolojiler & Metodoloji

- Frontend: Streamlit <br>
- GenAI: Gemini 2.0 Flash, Google Embedding, LangChain <br>
- Vector Database: FAISS <br>

## 📁 Proje Dosya Yapısı

```bash
techpath-mentor/
│
├── app.py                      # Ana Streamlit uygulaması
├── config.py                   # Yapılandırma sabitleri
├── data_processing.py          # Veri yükleme ve işleme
├── rag_pipeline.py             # RAG pipeline oluşturma
├── requirements.txt            # Python bağımlılıkları
│
├── data/                       # JSON veri dosyaları 
│   ├── 01_AI_ML.json
│   ├── 02_Web_Development.json
│   ├── 03_CyberSec.json
│   └── ...
│
└── README.md                   
```

## ⚙️ Proje Çalışma Kılavuzu

1. Depoyu klonlayın:

```bash
git clone https://github.com/betuloran/techpath-mentor.git
cd techpath-mentor
```

2. Sanal bir ortam oluşturun ve etkinleştirin: 

```bash
 python -m venv venv
 source venv/bin/activate  # Linux/Mac
 venv\Scripts\activate     # Windows
```

3. Gerekli paketleri kurun:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. Bir .env dosyası oluşturun ve Gemini API anahtarınızı ekleyin:

```bash
GEMINI_API_KEY=your_api_key_here
```

5. Uygulamayı çalıştırın:

```bash
streamlit run app.py
```

6. Tarayıcınızda http://localhost:8501 adresine gidin.

## 📧 İletişim
Projeyle ilgili herhangi bir sorunuz varsa lütfen bizimle iletişime geçin.

- E-posta: betul.oran2@gmail.com
- LinkedIn: linkedin.com/in/betüloran
- GitHub: github.com/betuloran




