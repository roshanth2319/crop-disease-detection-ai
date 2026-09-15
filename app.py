import streamlit as st
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image

from decision_support import get_decision_support


# ============================================================
# CONFIGURATION
# ============================================================

MODEL_PATH = "models/efficientnet_baseline.pth"
IMAGE_SIZE = 224


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Crop Disease Detection System",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ---------- PAGE ---------- */

    .stApp {
        background-color: #f6f9f6;
    }

    .block-container {
        max-width: 1150px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }


    /* ---------- TITLE ---------- */

    .main-title {
        text-align: center;
        color: #174d2a;
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #64736a;
        font-size: 17px;
        margin-bottom: 25px;
    }


    /* ---------- SECTION HEADINGS ---------- */

    h2, h3 {
        color: #174d2a !important;
    }


    /* ---------- BUTTON ---------- */

    .stButton > button {
        width: 100%;
        min-height: 52px;
        border-radius: 14px;
        font-size: 17px;
        font-weight: 700;
    }


    /* ---------- FILE UPLOADER ---------- */

    [data-testid="stFileUploader"] {
        background-color: white;
        border: 2px dashed #9dbca4;
        border-radius: 18px;
        padding: 18px;
    }


    /* ---------- METRICS ---------- */

    [data-testid="stMetric"] {
        background-color: white;
        padding: 18px;
        border-radius: 16px;
        border: 1px solid #e1e9e2;
        box-shadow: 0 3px 12px rgba(0,0,0,0.04);
    }


    /* ---------- IMAGE ---------- */

    [data-testid="stImage"] {
        border-radius: 18px;
    }


    /* ---------- EXPANDER ---------- */

    [data-testid="stExpander"] {
        border-radius: 15px;
        border: 1px solid #dce6de;
        background-color: white;
    }


    /* ---------- DIVIDER ---------- */

    hr {
        margin-top: 28px;
        margin-bottom: 28px;
    }


    /* ---------- FOOTER ---------- */

    .footer-text {
        text-align: center;
        color: #718078;
        font-size: 13px;
        padding-top: 20px;
    }


    /* ---------- MOBILE ---------- */

    @media (max-width: 700px) {

        .main-title {
            font-size: 30px;
        }

        .subtitle {
            font-size: 14px;
        }

    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# DEVICE
# ============================================================

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():

    checkpoint = torch.load(
        MODEL_PATH,
        map_location=device
    )

    class_names = checkpoint["class_names"]
    num_classes = checkpoint["num_classes"]

    model = models.efficientnet_b0(
        weights=None
    )

    model.classifier[1] = nn.Linear(
        model.classifier[1].in_features,
        num_classes
    )

    model.load_state_dict(
        checkpoint["model_state_dict"]
    )

    model = model.to(device)
    model.eval()

    return model, class_names


model, class_names = load_model()


# ============================================================
# IMAGE TRANSFORMATION
# ============================================================

transform = transforms.Compose([
    transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🌿 Crop Disease Detection System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'AI-based crop disease classification with preventive decision support'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# PROJECT INTRODUCTION
# ============================================================

st.info(
    "🌱 Upload a crop leaf image and let the AI model identify "
    "the crop condition and provide preventive recommendations."
)


# ============================================================
# SYSTEM INFORMATION
# ============================================================

st.subheader("📊 System Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "🌱 Disease Classes",
        "29"
    )

with col2:
    st.metric(
        "🧠 AI Model",
        "EfficientNet-B0"
    )

with col3:
    st.metric(
        "🎯 Test Accuracy",
        "99.48%"
    )

with col4:
    st.metric(
        "🛡️ Decision Support",
        "Enabled"
    )


# ============================================================
# ANALYSIS SECTION
# ============================================================

st.divider()

st.subheader("🔍 Analyze Your Crop")

st.write(
    "Upload a clear image of a crop leaf. "
    "For better results, make sure the leaf is clearly visible."
)


# ============================================================
# UPLOAD
# ============================================================

uploaded_file = st.file_uploader(
    "📸 Choose a Leaf Image",
    type=["jpg", "jpeg", "png"]
)


# ============================================================
# IMAGE PREVIEW
# ============================================================

if uploaded_file is not None:

    image = Image.open(
        uploaded_file
    ).convert("RGB")

    st.success(
        "✅ Image uploaded successfully!"
    )

    preview_col, analysis_col = st.columns(
        [1.2, 1],
        gap="large"
    )

    # --------------------------------------------------------
    # PREVIEW
    # --------------------------------------------------------

    with preview_col:

        st.subheader("📷 Image Preview")

        st.image(
            image,
            caption="Uploaded Leaf Image",
            use_container_width=True
        )


    # --------------------------------------------------------
    # ANALYSIS
    # --------------------------------------------------------

    with analysis_col:

        st.subheader("🤖 AI Analysis")

        st.write(
            "The EfficientNet-B0 model will analyze the "
            "visual features of the uploaded leaf."
        )

        st.write("")

        analyze = st.button(
            "🔍 ANALYZE LEAF IMAGE",
            type="primary",
            use_container_width=True
        )

        if analyze:

            with st.spinner(
                "🧠 AI is analyzing the leaf..."
            ):

                image_tensor = transform(
                    image
                ).unsqueeze(0).to(device)

                with torch.no_grad():

                    outputs = model(
                        image_tensor
                    )

                    probabilities = torch.softmax(
                        outputs,
                        dim=1
                    )

                    confidence, predicted_index = torch.max(
                        probabilities,
                        1
                    )

                predicted_index = predicted_index.item()

                confidence = (
                    confidence.item() * 100
                )

                predicted_class = class_names[
                    predicted_index
                ]

                # Top 3 predictions
                top_probabilities, top_indices = torch.topk(
                    probabilities,
                    min(3, len(class_names)),
                    dim=1
                )

                top_probabilities = (
                    top_probabilities[0]
                    .cpu()
                    .tolist()
                )

                top_indices = (
                    top_indices[0]
                    .cpu()
                    .tolist()
                )

            st.session_state["prediction"] = {
                "predicted_class": predicted_class,
                "confidence": confidence,
                "top_probabilities": top_probabilities,
                "top_indices": top_indices
            }


# ============================================================
# RESULTS
# ============================================================

if "prediction" in st.session_state:

    prediction = st.session_state["prediction"]

    predicted_class = prediction["predicted_class"]
    confidence = prediction["confidence"]
    top_probabilities = prediction["top_probabilities"]
    top_indices = prediction["top_indices"]


    # ========================================================
    # DECISION SUPPORT
    # ========================================================

    result = get_decision_support(
        predicted_class
    )


    # ========================================================
    # RESULT HEADER
    # ========================================================

    st.divider()

    st.subheader("🎯 AI Analysis Result")

    clean_class = (
        predicted_class
        .replace("___", " • ")
        .replace("_", " ")
    )

    st.success(
        f"🌿 Prediction: {clean_class}"
    )


    # ========================================================
    # CONFIDENCE
    # ========================================================

    confidence_col1, confidence_col2 = st.columns(
        [1, 2]
    )

    with confidence_col1:

        st.metric(
            "🎯 Confidence",
            f"{confidence:.2f}%"
        )

    with confidence_col2:

        st.write("**Model Confidence**")

        st.progress(
            min(confidence / 100, 1.0)
        )

        if confidence >= 90:

            st.success(
                "High-confidence prediction"
            )

        elif confidence >= 70:

            st.warning(
                "Moderate-confidence prediction"
            )

        else:

            st.warning(
                "Low-confidence prediction — "
                "consider checking another image."
            )


    # ========================================================
    # CROP / CONDITION / STATUS
    # ========================================================

    st.write("")

    detail1, detail2, detail3 = st.columns(3)

    with detail1:

        st.metric(
            "🌱 Crop",
            result["crop"]
        )

    with detail2:

        st.metric(
            "🔬 Condition",
            result["disease"]
        )

    with detail3:

        st.metric(
            "🛡️ Status",
            result["status"]
        )


    # ========================================================
    # PREVENTIVE DECISION SUPPORT
    # ========================================================

    st.divider()

    st.subheader(
        "🛡️ Preventive Decision Support"
    )

    st.write(
        "Recommended actions based on the detected crop condition:"
    )

    for number, recommendation in enumerate(
        result["prevention"],
        start=1
    ):

        st.info(
            f"**{number}.** {recommendation}"
        )


    # ========================================================
    # TOP 3 PREDICTIONS
    # ========================================================

    st.divider()

    with st.expander(
        "📊 View Top 3 AI Predictions"
    ):

        for rank, (index, probability) in enumerate(
            zip(
                top_indices,
                top_probabilities
            ),
            start=1
        ):

            class_name = (
                class_names[index]
                .replace("___", " • ")
                .replace("_", " ")
            )

            st.write(
                f"**{rank}. {class_name}**"
            )

            st.progress(
                min(float(probability), 1.0)
            )

            st.caption(
                f"{probability * 100:.2f}% confidence"
            )


# ============================================================
# HOW THE SYSTEM WORKS
# ============================================================

st.divider()

st.subheader(
    "⚙️ How the System Works"
)

st.write(
    "The complete prediction pipeline:"
)

step1, step2, step3, step4 = st.columns(4)

with step1:

    st.info(
        "📸 **1. Upload**\n\n"
        "Select a clear crop leaf image."
    )

with step2:

    st.info(
        "🧠 **2. Analyze**\n\n"
        "EfficientNet-B0 processes the image."
    )

with step3:

    st.info(
        "🔬 **3. Classify**\n\n"
        "The system identifies the crop condition."
    )

with step4:

    st.info(
        "🛡️ **4. Protect**\n\n"
        "Preventive recommendations are provided."
    )


# ============================================================
# FUTURE ENHANCEMENT
# ============================================================

st.divider()

st.subheader(
    "🤖 Future Enhancement"
)

st.info(
    "A multilingual agricultural AI assistant with Telugu "
    "language and voice support can be added in a future version "
    "to explain diseases and preventive measures in a "
    "farmer-friendly way."
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    '<div class="footer-text">'
    '🌿 <b>Crop Disease Detection System</b><br>'
    'AI-Based Crop Disease Classification with Preventive Decision Support'
    '<br><br>'
    'EfficientNet-B0 • 29 Classes • Intelligent Image Analysis'
    '</div>',
    unsafe_allow_html=True
)
