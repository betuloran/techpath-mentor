# 🎯 TechPath Mentor: Kariyer Yolu Asistanı

Generative AI Bootcamp (2025) için hazırlanmış, IT ve Bilgisayar Mühendisliği kariyer yollarına odaklanan, Türkçe RAG (Retrieval-Augmented Generation) tabanlı bir chatbot projesidir.

## 📋 Proje Hakkında

Bu proje, öğrencilere ve kariyer değiştirenlere yönelik, **özel olarak hazırlanmış Türkçe IT bilgi setlerine** dayanarak rehberlik eden bir yapay zeka asistanı sunar. Gelişmiş RAG mimarisi sayesinde, chatbot, sadece genel model bilgisi yerine, IT dünyasının güncel ve Türkiye ekosistemine özgü terimleri (DevOps, Cloud, Backend, UI/UX, QA, Oyun Geliştirme vb.) içeren yerel veri setlerinden bilgi çekerek, yüksek doğrulukta ve bağlama dayalı yanıtlar üretir.

### Ana Özellikler

* **Özel Türkçe Veri Setleri:** Global terimlerin yanı sıra, Türkiye IT ekosistemine özel bilgileri içeren JSON veri setleri kullanılır.
* **Bağlamsal Doğruluk:** Kullanıcı sorularına, sadece ilgili bilgi parçalarını (chunks) kullanarak cevap verir, böylece tutarsızlık (hallucination) riski en aza iner.
* **Kolay Kullanım:** Streamlit tabanlı web arayüzü ile hızlı ve etkileşimli bir sohbet deneyimi sunar.
* **Kaynak Gösterimi:** Yanıtların hangi veri setlerine dayandığı gösterilerek güvenilirlik artırılır.

## 📚 Veri Seti

### Veri Seti Metodolojisi (Derleme ve Kaynaklandırma)

Hazır bir kurumsal veri seti bulunmadığından, veri setimiz şu şekilde yapay zeka destekli derleme ile oluşturulmuştur:

* **Konu Belirleme:** Öğrencilerin en çok merak ettiği 4 ana başlık belirlendi (AI, Web, Siber Güvenlik, Kurumsal IT).

* **Derleme:** Her bir başlık için, sektörel raporlar, uzman blogları ve popüler teknik dokümantasyonlar baz alınarak bir bilgi bankası metni oluşturuldu.

* **Türkçe/Jargon Dengelemesi:** Metinler genel olarak Türkçe kalırken; REST API, Cloud, IaaS, Deployment gibi IT dünyasında yaygın kullanılan teknik İngilizce jargonlar, öğrencinin sektöre adapte olması amacıyla bilerek metin içinde korunmuştur.

* **Format ve Metadata:** Veri seti JSON formatına çevrilmiş ve her içeriğe kaynak ("Mentor Bilgi Bankası - Yapay Zeka Destekli Derleme"), konu ve id gibi metadata bilgileri eklenmiştir.

### Veri Seti İçeriği

Veri seti, her biri JSON formatında tutulan 14 ana dosyadan oluşmaktadır.

## 🛠️ Kullanılan Teknolojiler

| Kategori | Teknoloji | Açıklama |
| :--- | :--- | :--- |
| **GenAI/LLM** | Google Gemini (gemini-2.0-flash-exp) | Yanıt üretimi için kullanılan üretken model. (Not: Bu model, Gemini 2.5 Flash'ın eski, deneysel bir versiyonudur.) |
| **Embedding** | Google `text-embedding-004` | Metinleri vektöre dönüştürme modeli. |
| **RAG Çatısı** | LangChain | RAG pipeline bileşenlerini (Loader, Splitter, DB, Chain) yönetme. |
| **Arayüz** | Streamlit | Hızlı prototipleme ve web arayüzü oluşturma. |
| **Veritabanı** | ChromaDB (In-Memory) | Vektörlerin hızlı erişim için bellekte depolanması. |
| **Veri İşleme** | JQ Syntax | JSON dosyalarından sadece `icerik` alanını çekme. |

### ⚙️ Proje Çalışma Kılavuzu

## 1. Ortam Kurulumu

Proje, Anaconda/Miniforge gibi harici Python ortamlarından kaynaklanan çakışmaları önlemek için özel bir sanal ortamda (venv) çalıştırılmalıdır.


