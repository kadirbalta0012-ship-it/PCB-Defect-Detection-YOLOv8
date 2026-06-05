import streamlit as st
import urllib.request
import os
from ultralytics import YOLO
from PIL import Image

# Sayfa Yapılandırması
st.set_page_config(page_title="Yapay Zeka Tabanlı PCB Hasar Tespit Sistemi", layout="wide")

# Model İndirme ve Yükleme Fonksiyonu (Önbellekli)
@st.cache_resource
def load_model():
    model_path = "best_clean.pt"
    # Eğer temiz model lokalde yoksa doğrudan senin GitHub Release üzerinden çeker
    if not os.path.exists(model_path):
        with st.spinner("Yapay zeka modeli buluttan indiriliyor, lütfen bekleyin..."):
            url = "https://github.com/kadirbalta0012-ship-it/PCB-Defect-Detection-YOLOv8/releases/download/v1.0/best.pt"
            urllib.request.urlretrieve(url, model_path)
    return YOLO(model_path)

# Modeli Yükle
try:
    model = load_model()
    model_loaded = True
except Exception as e:
    st.error(f"Model yüklenirken bir hata oluştu: {e}")
    model_loaded = False

# Sol Menü (Sidebar) Bilgileri
st.sidebar.header("🛠️ Sistem Bilgileri")
st.sidebar.info(
    "**Model Architecture:** YOLOv8n (YOLOv8 Nano)\n\n"
    "**Framework:** PyTorch & Streamlit\n\n"
    "**Dataset:** 6 Sınıflı PCB Hasar Seti"
)

st.sidebar.header("📊 Doğruluk Metrikleri")
st.sidebar.success("🎯 **Genel mAP50:** %89.50")

# Ana Sayfa İçeriği
st.title("Yapay Zeka Tabanlı PCB Hasar Tespit Sistemi")
st.caption("YOLOv8 Derin Öğrenme Modeli ile Mikroskobik Üretim Hatalarının Gerçek Zamanlı Analizi")
st.write("---")

if model_loaded:
    # Fotoğraf Yükleme Alanı
    uploaded_file = st.file_uploader("Analiz edilecek PCB görselini buraya sürükleyin veya seçin...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Görseli Aç
        image = Image.open(uploaded_file)
        
        # Sayfayı iki kolona böl (Orijinal vs Yapay Zeka Sonucu)
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Orijinal PCB Görseli")
            st.image(image, use_container_width=True)
            
        with col2:
            st.subheader("Yapay Zeka Hasar Analizi")
            with st.spinner("Model görüntüyü işliyor..."):
                # YOLOv8 Tahmini Yap
                results = model(image)
                
                # Sonuçların çizildiği görseli al
                res_plotted = results[0].plot()
                
                # Ekrana bas
                st.image(res_plotted, channels="BGR", use_container_width=True)
                
            # Tespit edilen sınıfları listele
            boxes = results[0].boxes
            if len(boxes) > 0:
                st.warning(f"⚠️ Toplam {len(boxes)} adet üretim hatası tespit edildi!")
            else:
                st.success("✅ Kart temiz! Herhangi bir üretim hatası saptanmadı.")
else:
    st.warning("Model yüklenemediği için analiz fonksiyonu şu an devre dışı.")
