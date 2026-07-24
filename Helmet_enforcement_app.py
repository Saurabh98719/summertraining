import streamlit as st
from ultralytics import YOLO
from PIL import Image

st.set_page_config(page_title="NO-HELMET ENFORCEMENT", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #4b0082 0%, #8a2be2 100%);
        color: white;
    }
    .stApp * {
        color: white !important;
    }
    .stButton > button,
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > div {
        background: rgba(255, 255, 255, 0.15) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.35) !important;
    }
    .stFileUploader label,
    .stFileUploader .uploadFile {
        color: black !important;
    }
    .stFileUploader .uploadFile {
        background: white !important;
    }
    .stMetric, .stBlockContainer {
        background: rgba(255, 255, 255, 0.08) !important;
        border-radius: 8px;
        padding: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("NO-HELMET ENFORCEMENT")

# Top metrics
col1, col2, col3 = st.columns(3)
col1.metric("Status", "ACTIVE")
if "violations" not in st.session_state:
    st.session_state["violations"] = 0
violation_placeholder = col2.empty()
violation_placeholder.metric("Violations", st.session_state["violations"])
col3.metric("Camera ID", "CH-00010")

st.subheader("📷 PHOTO DETECTION")

# Load YOLO model
@st.cache_resource
def load_model():
    return YOLO('yolov8n.pt')

model = load_model()

# Upload photo
img_file = st.file_uploader("Upload Traffic Photo", type=['jpg', 'jpeg', 'png'])

if img_file is not None:
    image = Image.open(img_file)
    st.image(image, caption="Uploaded Photo", use_column_width=True)
    
    if st.button("Detect in Photo"):
        with st.spinner("Running detection..."):
            results = model(image)
            res_img = results[0].plot() # image with bounding boxes
            
            st.subheader("RESULT")
            st.image(res_img, caption="Detection Result", use_column_width=True)
            
            # INCIDENT DETAILS
            st.subheader("INCIDENT DETAILS")
            boxes = results[0].boxes
            names = model.names
            
            detected = {}
            for box in boxes:
                cls = int(box.cls)
                name = names[cls]
                detected[name] = detected.get(name, 0) + 1

            normalized_detected = {str(k).lower(): v for k, v in detected.items()}
            persons = normalized_detected.get("person", 0)
            helmets = normalized_detected.get("helmet", 0)

            if persons > 0 and helmets > 0:
                violations = max(persons - helmets, 0)
            elif persons > 0:
                violations = persons
            else:
                violations = 0

            st.session_state["violations"] = violations
            violation_placeholder.metric("Violations", violations)
            
            if detected:
                for k, v in detected.items():
                    st.write(f"**{k}: {v}**")
                st.write(f"**Potential helmet violations: {violations}**")
            else:
                st.write("No objects detected")

st.subheader("Violation Log")