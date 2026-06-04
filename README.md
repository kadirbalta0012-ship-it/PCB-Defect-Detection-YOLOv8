# 🔬 YOLOv8 ile Yapay Zeka Tabanlı PCB Hasar Tespit Sistemi

Bu proje, Baskılı Devre Kartları (PCB) üzerindeki üretim hatalarını (Açık devre, kısa devre, eksik delik, bakır kemirmesi vb.) YOLOv8 nesne tespiti mimarisi kullanarak otomatik olarak tespit eder.

## 🚀 Proje Bileşenleri
* **Canlı Web Sitesi (Streamlit):** [Buraya Bir Önceki Adımda Açtığımız Streamlit Canlı İnternet Linkini Yapıştır Kanka]
* **Model Doğruluk Oranı (mAP50):** %89.50 (50 Epoch Eğitim Sonucu)

## 📸 Test ve Tahmin Görselleri (Sistem Nasıl Çalışıyor?)
Sistemin başarıyla tespit ettiği örnek hasarlı PCB test görselleri aşağıda listelenmiştir:

| Orijinal Hasarlı Kart | Yapay Zeka Hasar Tespiti (Prediction) |
| :---: | :---: |
| <img src="https://raw.githubusercontent.com/kadirbalta0012-ship-it/PCB-Defect-Detection-YOLOv8/main/testpcb.jpg" width="350"> | <img src="https://raw.githubusercontent.com/kadirbalta0012-ship-it/PCB-Defect-Detection-YOLOv8/main/foto1_pred.jpg" width="350"> |

> ⚠️ **Not:** Yukarıdaki tablonun çalışması için yüklediğin fotoğrafların isimlerini `foto1.jpg` ve `foto1_pred.jpg` şeklinde değiştirebilir veya koddaki isimleri kendi yüklediğin fotoğrafların tam isimleriyle değiştirebilirsin kanka.
