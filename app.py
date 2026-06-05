import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import urllib.request
import os


st.set_page_config(
    page_title="AI PCB Defect Detector", 
    page_icon="🔍",
    layout="wide"
)


st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stTitle { color: #1E3A8A; font-family: 'Helvetica Neue', sans-serif; font-weight: 800; }
    .hasar-kart { background-color: #ffffff; padding: 15px; border-radius: 10px; border-left: 5px solid #EF4444; margin-bottom: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .basari-kart { background-color: #ffffff; padding: 20px; border-radius: 10px; border-left: 5px solid #10B981; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
""", unsafe_allow_html=True)


with st.sidebar:
    st.markdown("## 🛠️ Sistem Bilgileri")
    st.info("**Model Architecture:** YOLOv8n (YOLOv8 Nano)\n\n**Framework:** PyTorch & Streamlit\n\n**Dataset:** 6 Sınıflı PCB Hasar Seti")
    st.write("---")
    st.markdown("### 📊 Hedef Metrikler")
    st.success("🎯 **Genel mAP50:** %89.50")
    st.write("---")
    st.caption("Computer Engineering Project © 2026")


st.title("🔍 Yapay Zeka Tabanlı PCB Hasar Tespit Sistemi")
st.markdown("##### *YOLOv8 Derin Öğrenme Modeli ile Mikroskobik Üretim Hatalarının Gerçek Zamanlı Analizi*")
st.write("---")


HASAR_SOZLUGU = {
    "missing_hole": {"tr": "Eksik Delik (Missing Hole)", "desc": "PCB üzerinde bulunması gereken montaj veya yol deliğinin delinmediğini gösterir."},
    "mouse_bite": {"tr": "Bakır Kemirmesi (Mouse Bite)", "desc": "Yolların kenarında bakır kaybı nedeniyle oluşan ve akımı daraltan oyuk hatasıdır."},
    "open_circuit": {"tr": "Açık Devre (Open Circuit)", "desc": "İletken yolun kopması sonucu akımın karşıya geçemediği bağlantı kesintisidir."},
    "short": {"tr": "Kısa Devre (Short)", "desc": "İki farklı iletken yolun istenmeyen şekilde birbirine temas etmesi hatasıdır."},
    "spur": {"tr": "Çıkıntı / Kıymık (Spur)", "desc": "Bakır yoldan dışarı doğru uzanan ve başka yollara yaklaşan küçük bakır çıkıntısıdır."},
    "spurious_copper": {"tr": "Gereksiz Bakır (Spurious Copper)", "desc": "PCB yüzeyinde kalmaması gereken, kısa devre riski oluşturan başıboş bakır kalıntılarıdır."}
}


@st.cache_resource
def load_model():
    model_path = "best_clean.pt"
    if not os.path.exists(model_path):
        with st.spinner("Yapay zeka modeli buluttan indiriliyor, lütfen bekleyin..."):
            url = "https://github.com/kadirbalta0012-ship-it/PCB-Defect-Detection-YOLOv8/releases/download/v1.0/best.pt"
            urllib.request.urlretrieve(url, model_path)
    return YOLO(model_path)


model_loaded = False
try:
    model = load_model()
    model_loaded = True
except Exception as e:
    st.error(f"Model yüklenirken bir hata oluştu: {e}")

if model_loaded:
    # File uploader field
    uploaded_file = st.file_uploader("Analiz edilecek PCB görselini buraya sürükleyin veya seçin...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        
        # Dual column layout
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📷 Giriş Görseli")
            st.image(image, use_container_width=True)
            
        with col2:
            st.markdown("### ⚡ Yapay Zeka Çıktısı")
            with st.spinner("Model tahmin yürütüyor, lütfen bekleyin..."):
                results = model(image)
                res_plotted = results[0].plot()
                predicted_image = Image.fromarray(res_plotted[..., ::-1])
                st.image(predicted_image, use_container_width=True)
                
        st.write("---")
        st.markdown("### 📈 Detaylı Hasar Teşhis Raporu")
        
        boxes = results[0].boxes
        if len(boxes) == 0:
            st.markdown("""
                <div class='basari-kart'>
                    <h4 style='color: #10B981; margin-top:0;'>✅ Temiz Kart Raporu</h4>
                    <p>YOLOv8 modeli tarafından yapılan derinlemesine tarama sonucunda PCB yüzeyinde herhangi bir mikroskobik üretim hatasına rastlanmamıştır. Kart üretime uygundur.</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            class_names = results[0].names
            
            # Render defect details with custom CSS cards
            for box in boxes:
                cls_id = int(box.cls[0])
                conf_score = float(box.conf[0]) * 100
                ingilizce_etiket = class_names[cls_id]
                
                if ingilizce_etiket in HASAR_SOZLUGU:
                    hasar_tr = HASAR_SOZLUGU[ingilizce_etiket]["tr"]
                    hasar_aciklama = HASAR_SOZLUGU[ingilizce_etiket]["desc"]
                    
                    st.markdown(f"""
                        <div class='hasar-kart'>
                            <h5 style='color: #EF4444; margin-top:0; margin-bottom:5px;'>⚠️ {hasar_tr}</h5>
                            <p style='margin-bottom:5px;'><b>Doğruluk Skoru:</b> <span style='color: #EF4444;'>%{conf_score:.2f}</span></p>
                            <p style='margin:0; color: #4B5563; font-size: 14px;'><b>Mühendislik Açıklaması:</b> {hasar_aciklama}</p>
                        </div>
                    """, unsafe_allow_html=True)
else:
    st.warning("Sistem modeli yükleyemediği için analiz fonksiyonu şu an devre dışıdır.")
