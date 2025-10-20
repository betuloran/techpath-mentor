# 🎯 TechPath Mentor: Kariyer Yolu Asistanı

Generative AI Bootcamp (2025) için hazırlanmış, IT ve Bilgisayar Mühendisliği kariyer yollarına odaklanan, Türkçe RAG (Retrieval-Augmented Generation) tabanlı bir chatbot projesidir.

## 📋 Proje Hakkında

Bu proje, öğrencilere ve kariyer değiştirenlere yönelik, **özel olarak hazırlanmış Türkçe IT bilgi setlerine** dayanarak rehberlik eden bir yapay zeka asistanı sunar. Gelişmiş RAG mimarisi sayesinde, chatbot, sadece genel model bilgisi yerine, IT dünyasının güncel ve Türkiye ekosistemine özgü terimleri (DevOps, Cloud, Backend, UI/UX, QA, Oyun Geliştirme vb.) içeren yerel veri setlerinden bilgi çekerek, yüksek doğrulukta ve bağlama dayalı yanıtlar üretir.

### Ana Özellikler

* **Özel Türkçe Veri Setleri:** Global terimlerin yanı sıra, Türkiye IT ekosistemine özel bilgileri içeren JSON veri setleri kullanılır.
* **Bağlamsal Doğruluk:** Kullanıcı sorularına, sadece ilgili bilgi parçalarını (chunks) kullanarak cevap verir, böylece tutarsızlık (hallucination) riski en aza iner.
* **Kolay Kullanım:** Streamlit tabanlı web arayüzü ile hızlı ve etkileşimli bir sohbet deneyimi sunar.
* **Kaynak Gösterimi:** Yanıtların hangi veri setlerine dayandığı gösterilerek güvenilirlik artırılır.

## 🛠️ Kullanılan Teknolojiler

| Kategori | Teknoloji | Açıklama |
| :--- | :--- | :--- |
| **GenAI/LLM** | Google Gemini (gemini-2.0-flash-exp) | Yanıt üretimi için kullanılan üretken model. (Not: Bu model, Gemini 2.5 Flash'ın eski, deneysel bir versiyonudur.) |
| **Embedding** | Google `text-embedding-004` | Metinleri vektöre dönüştürme modeli. |
| **RAG Çatısı** | LangChain | RAG pipeline bileşenlerini (Loader, Splitter, DB, Chain) yönetme. |
| **Arayüz** | Streamlit | Hızlı prototipleme ve web arayüzü oluşturma. |
| **Veritabanı** | ChromaDB (In-Memory) | Vektörlerin hızlı erişim için bellekte depolanması. |
| **Veri İşleme** | JQ Syntax | JSON dosyalarından sadece `icerik` alanını çekme. |

## 📁 Proje Yapısı
