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

### 💡 Neden RAG?
Geleneksel chatbot'ların aksine, RAG mimarisi:

✅ Güncel ve spesifik bilgilere erişim sağlar. <br>
✅ Halüsinasyon riskini minimize eder. <br>
✅ Kaynak doğrulanabilir yanıtlar üretir. <br>
✅ Domain-specific (alan-odaklı) uzmanlık sunar. <br>

### Ana Özellikler

* **Özel Türkçe Veri Setleri:** Global terimlerin yanı sıra, Türkiye IT ekosistemine özel bilgileri içeren JSON veri setleri kullanılır.
* **Bağlamsal Doğruluk:** Kullanıcı sorularına, sadece ilgili bilgi parçalarını (chunks) kullanarak cevap verir, böylece tutarsızlık (hallucination) riski en aza iner.
* **Kolay Kullanım:** Streamlit tabanlı web arayüzü ile hızlı ve etkileşimli bir sohbet deneyimi sunar.
* **Kaynak Gösterimi:** Yanıtların hangi veri setlerine dayandığı gösterilerek güvenilirlik artırılır.

## Veri Seti Metodolojisi (Derleme ve Kaynaklandırma)

### 🗂️ Veri Kaynağı ve Yapısı
Proje, 157 adet JSON dokümanı içeren özenle hazırlanmış bir bilgi bankası kullanmaktadır.
Veri Toplama Metodolojisi
Veri seti, aşağıdaki kaynaklardan derlenerek oluşturulmuştur:

* **İş İlanları Analizi (LinkedIn, Kariyer.net, Indeed)** 

Sektör bazında aranan teknolojiler
Beklenen beceriler ve sertifikalar
Maaş aralıkları ve iş tanımları

* **Sektör Raporları**

StackOverflow Developer Survey
GitHub State of the Octoverse
Gartner Technology Trends

* **Akademik ve Kurumsal Kaynaklar**

Üniversite müfredatları
Bootcamp programları
Sertifika kuruluşları (CompTIA, Cisco, AWS vb.)
### Veri Seti İçeriği

### Veri Seti Kategorileri
Veri seti 14 ana kategori altında yapılandırılmıştır:

| Kategori | Dosya Sayısı | İçerik |
| :--- | :--- | :--- |
| **🤖 AI & Veri Bilimi** | 25 | Yanıt üretimi için kullanılan üretken model. (Not: Bu model, Gemini 2.5 Flash'ın eski, deneysel bir versiyonudur.) |
| **🌐 Web Geliştirme** | 30 | Metinleri vektöre dönüştürme modeli. |
| **🔒 Siber Güvenlik** | 20 | RAG pipeline bileşenlerini (Loader, Splitter, DB, Chain) yönetme. |
| **🎮 Oyun Geliştirme** | 12 | Hızlı prototipleme ve web arayüzü oluşturma. |
| **📱 Mobil Geliştirme** | 15 | Vektörlerin hızlı erişim için bellekte depolanması. |
| **☁️ Cloud & DevOps** | 18 | JSON dosyalarından sadece `icerik` alanını çekme. |
| **🎨 UI/UX Design** | 8 | JSON dosyalarından sadece `icerik` alanını çekme. |
| **🔙 Backend & API** | 10 | JSON dosyalarından sadece `icerik` alanını çekme. |
| **📈 QA & Testing** | 5 | JSON dosyalarından sadece `icerik` alanını çekme. |
| **🏢 Kurumsal IT** | 20 | JSON dosyalarından sadece `icerik` alanını çekme. |
| **💼 Kariyer Geliştirme** | 6 | JSON dosyalarından sadece `icerik` alanını çekme. |
| **🇹🇷 Türkiye IT Ekosistemi** | 4 | JSON dosyalarından sadece `icerik` alanını çekme. |
| **🗣️ Soft Skills** | 3 | JSON dosyalarından sadece `icerik` alanını çekme. |
| **👩🏼‍💼 Mülakat Hazırlığı** | 12 | JSON dosyalarından sadece `icerik` alanını çekme. |

## 🛠️ Kullanılan Teknolojiler & Metodoloji

Frontend: Streamlit
GenAI: Gemini 2.0 Flash, Google Embedding, LangChain
Vector Database: FAISS

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
pip install -r requirements.txt
```

4. Bir .env dosyası oluşturun ve Gemini API anahtarınızı ekleyin:

```bash
GEMİNİ_API_KEY=your_api_key
```

5. Uygulamayı çalıştırın:

```bash
streamlit run app.py
```




