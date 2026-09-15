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
    page_title="Crop Disease Detection",
    page_icon="🌿",
    layout="centered"
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

st.title("🌿 Crop Disease Detection System")

st.write(
    "AI-based crop disease classification with "
    "preventive decision support."
)

st.divider()


# ============================================================
# MODEL INFORMATION
# ============================================================

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Disease Classes",
        len(class_names)
    )

with col2:
    st.metric(
        "Model",
        "EfficientNet-B0"
    )


# ============================================================
# IMAGE UPLOAD
# ============================================================

st.subheader("Upload Leaf Image")

uploaded_file = st.file_uploader(
    "Choose a leaf image",
    type=["jpg", "jpeg", "png"]
)


# ============================================================
# PREDICTION
# ============================================================

if uploaded_file is not None:

    image = Image.open(
        uploaded_file
    ).convert("RGB")

    st.image(
        image,
        caption="Uploaded Leaf Image",
        use_container_width=True
    )

    if st.button(
        "🔍 Detect Disease",
        use_container_width=True
    ):

        with st.spinner(
            "Analyzing leaf image..."
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

            predicted_index = (
                predicted_index.item()
            )

            confidence = (
                confidence.item() * 100
            )

            predicted_class = class_names[
                predicted_index
            ]

        # ----------------------------------------------------
        # RESULT
        # ----------------------------------------------------

        st.divider()

        st.subheader(
            "Prediction Result"
        )

        st.success(
            f"Predicted Class: {predicted_class}"
        )

        st.info(
            f"Confidence: {confidence:.2f}%"
        )

        # ----------------------------------------------------
        # DECISION SUPPORT
        # ----------------------------------------------------

        result = get_decision_support(
            predicted_class
        )

        st.divider()

        st.subheader(
            "Preventive Decision Support"
        )

        st.write(
            f"**Status:** {result['status']}"
        )

        st.write(
            f"**Crop:** {result['crop']}"
        )

        st.write(
            f"**Disease:** {result['disease']}"
        )

        st.write(
            "**Recommended Actions:**"
        )

        for recommendation in result["prevention"]:

            st.write(
                f"• {recommendation}"
            )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Crop Disease Detection System | "
    "EfficientNet-B0 | 29 Classes"
)