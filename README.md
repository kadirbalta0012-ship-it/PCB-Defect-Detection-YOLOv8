# 🔬 YOLOv8 ile Yapay Zeka Tabanlı PCB Hasar Tespit Sistemi

Bu proje, Baskılı Devre Kartları (PCB) üzerindeki üretim hatalarını (Açık devre, kısa devre, eksik delik, bakır kemirmesi vb.) YOLOv8 nesne tespiti mimarisi kullanarak otomatik olarak tespit eder.

## 🚀 Proje Bileşenleri
* **Canlı Web Sitesi (Streamlit):** [Buraya Streamlit Canlı İnternet Linkini Yapıştır Kanka]
* **Model Doğruluk Oranı (mAP50):** %89.50 (50 Epoch Eğitim Sonucu)

## 📸 Örnek Test ve Tahmin Görseli
Sistemin başarıyla tespit ettiği eksik delik (`missing_hole`) hatasına ait orijinal kart ve yapay zeka tahmin sonucu aşağıda yan yana listelenmiştir:

| Orijinal Hasarlı Kart | Yapay Zeka Hasar Tespiti (Prediction) |
| :---: | :---: |
| <img src="https://raw.githubusercontent.com/kadirbalta0012-ship-it/PCB-Defect-Detection-YOLOv8/main/test_images/01_missing_hole_01.jpg" width="380"> | <img src="https://raw.githubusercontent.com/kadirbalta0012-ship-it/PCB-Defect-Detection-YOLOv8/main/test_images/01_missing_hole_01_pred.jpg" width="380"> |
