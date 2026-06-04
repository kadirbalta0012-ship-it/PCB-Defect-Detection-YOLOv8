# 🔬 YOLOv8 ile Yapay Zeka Tabanlı PCB Hasar Tespit Sistemi

Bu proje, Baskılı Devre Kartları (PCB) üzerindeki üretim hatalarını (Açık devre, kısa devre, eksik delik, bakır kemirmesi vb.) YOLOv8 nesne tespiti mimarisi kullanarak otomatik olarak tespit eder.

## 🚀 Proje Bileşenleri
* **Canlı Web Sitesi (Streamlit):** [https://pcb-defect-detection-yolov8-dwarvklhgvgy5agzt4ffjo.streamlit.app/](https://pcb-defect-detection-yolov8-dwarvklhgvgy5agzt4ffjo.streamlit.app/)
* **Model Doğruluk Oranı (mAP50):** %89.50 (50 Epoch Eğitim Sonucu)

## 📸 Örnek Test Görselleri Galerisi
Sistemin test edilmesi için depoya yüklenen hasarlı PCB fotoğrafları aşağıda listelenmiştir:

| Test Görseli 1 (Açık Devre) | Test Görseli 2 (Bakır Oyuğu) | Test Görseli 3 (Açık Devre) |
| :---: | :---: | :---: |
| <img src="https://raw.githubusercontent.com/kadirbalta0012-ship-it/PCB-Defect-Detection-YOLOv8/main/testpcb" width="240"> | <img src="https://raw.githubusercontent.com/kadirbalta0012-ship-it/PCB-Defect-Detection-YOLOv8/main/testpcb1" width="240"> | <img src="https://raw.githubusercontent.com/kadirbalta0012-ship-it/PCB-Defect-Detection-YOLOv8/main/testpcb2" width="240"> |

| Test Görseli 4 (Fazla Bakır) | Test Görseli 5 (Bakır Oyuğu) | Test Görseli 6 (Bakır Oyuğu) |
| :---: | :---: | :---: |
| <img src="https://raw.githubusercontent.com/kadirbalta0012-ship-it/PCB-Defect-Detection-YOLOv8/main/testpcb3" width="240"> | <img src="https://raw.githubusercontent.com/kadirbalta0012-ship-it/PCB-Defect-Detection-YOLOv8/main/testpcb4" width="240"> | <img src="https://raw.githubusercontent.com/kadirbalta0012-ship-it/PCB-Defect-Detection-YOLOv8/main/testpcb5" width="240"> |

---
