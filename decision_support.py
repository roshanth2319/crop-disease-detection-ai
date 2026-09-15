# ============================================================
# PREVENTIVE DECISION SUPPORT MODULE
# Crop Disease Detection System
# ============================================================

def get_decision_support(disease_class):

    recommendations = {

        # ---------------- APPLE ----------------

        "Apple___Apple_Scab": {
            "status": "Disease Detected",
            "crop": "Apple",
            "disease": "Apple Scab",
            "prevention": [
                "Remove and destroy infected fallen leaves.",
                "Maintain good air circulation by proper pruning.",
                "Avoid prolonged leaf wetness where possible.",
                "Use integrated disease-management practices."
            ]
        },

        "Apple___Black_Rot": {
            "status": "Disease Detected",
            "crop": "Apple",
            "disease": "Black Rot",
            "prevention": [
                "Remove infected fruits and plant material.",
                "Prune affected branches and maintain orchard sanitation.",
                "Avoid injuries to fruits and branches.",
                "Monitor plants regularly for new symptoms."
            ]
        },

        "Apple___Cedar_Apple_Rust": {
            "status": "Disease Detected",
            "crop": "Apple",
            "disease": "Cedar Apple Rust",
            "prevention": [
                "Remove severely affected plant material.",
                "Maintain good air circulation through pruning.",
                "Monitor leaves regularly during favorable disease conditions.",
                "Follow integrated disease-management practices."
            ]
        },

        "Apple___Healthy": {
            "status": "Healthy",
            "crop": "Apple",
            "disease": "No disease detected",
            "prevention": [
                "Continue regular crop monitoring.",
                "Maintain proper irrigation and nutrition.",
                "Keep the growing area clean.",
                "Inspect leaves regularly for early symptoms."
            ]
        },

        # ---------------- BELL PEPPER ----------------

        "Bell_Pepper___Bacterial_Spot": {
            "status": "Disease Detected",
            "crop": "Bell Pepper",
            "disease": "Bacterial Spot",
            "prevention": [
                "Remove severely infected plant material.",
                "Avoid working with plants when foliage is wet.",
                "Improve field sanitation.",
                "Use healthy planting material and monitor plants regularly."
            ]
        },

        "Bell_Pepper___Healthy": {
            "status": "Healthy",
            "crop": "Bell Pepper",
            "disease": "No disease detected",
            "prevention": [
                "Continue regular crop inspection.",
                "Maintain proper irrigation.",
                "Keep weeds and plant debris under control.",
                "Monitor leaves for early disease symptoms."
            ]
        },

        # ---------------- CHERRY ----------------

        "Cherry___Powdery_Mildew": {
            "status": "Disease Detected",
            "crop": "Cherry",
            "disease": "Powdery Mildew",
            "prevention": [
                "Improve air circulation through proper pruning.",
                "Avoid excessive humidity around foliage.",
                "Remove severely affected plant material.",
                "Monitor new growth regularly."
            ]
        },

        "Cherry___Healthy": {
            "status": "Healthy",
            "crop": "Cherry",
            "disease": "No disease detected",
            "prevention": [
                "Continue regular monitoring.",
                "Maintain proper irrigation and nutrition.",
                "Prune appropriately to improve air circulation.",
                "Remove dead plant material."
            ]
        },

        # ---------------- CORN ----------------

        "Corn_(Maize)___Cercospora_leaf_spot_Gray_leaf_spot": {
            "status": "Disease Detected",
            "crop": "Corn (Maize)",
            "disease": "Cercospora Leaf Spot",
            "prevention": [
                "Remove or manage infected crop residue.",
                "Maintain good field sanitation.",
                "Monitor lower leaves for early symptoms.",
                "Use integrated crop-management practices."
            ]
        },

        "Corn_(Maize)___Common_rust_": {
            "status": "Disease Detected",
            "crop": "Corn (Maize)",
            "disease": "Common Rust",
            "prevention": [
                "Monitor leaves regularly for rust pustules.",
                "Maintain healthy crop growth.",
                "Remove heavily infected plant material where practical.",
                "Follow recommended local disease-management practices."
            ]
        },

        "Corn_(Maize)___Healthy": {
            "status": "Healthy",
            "crop": "Corn (Maize)",
            "disease": "No disease detected",
            "prevention": [
                "Continue regular crop monitoring.",
                "Maintain balanced irrigation and nutrition.",
                "Manage weeds and crop residue.",
                "Inspect leaves regularly."
            ]
        },

        "Corn_(Maize)___Northern_Leaf_Blight": {
            "status": "Disease Detected",
            "crop": "Corn (Maize)",
            "disease": "Northern Leaf Blight",
            "prevention": [
                "Manage infected crop residue.",
                "Monitor lower leaves for expanding lesions.",
                "Maintain good crop health.",
                "Use integrated disease-management practices."
            ]
        },

        # ---------------- GRAPE ----------------

        "Grape___Black_rot": {
            "status": "Disease Detected",
            "crop": "Grape",
            "disease": "Black Rot",
            "prevention": [
                "Remove infected berries and plant debris.",
                "Improve canopy ventilation through proper pruning.",
                "Monitor developing fruit regularly.",
                "Maintain good vineyard sanitation."
            ]
        },

        "Grape___Esca_(Black_Measles)": {
            "status": "Disease Detected",
            "crop": "Grape",
            "disease": "Esca (Black Measles)",
            "prevention": [
                "Remove severely affected plant material where appropriate.",
                "Avoid unnecessary wounds during pruning.",
                "Maintain vineyard sanitation.",
                "Monitor vines regularly for symptom development."
            ]
        },

        "Grape___Healthy": {
            "status": "Healthy",
            "crop": "Grape",
            "disease": "No disease detected",
            "prevention": [
                "Continue regular vineyard inspection.",
                "Maintain good canopy management.",
                "Provide appropriate irrigation and nutrition.",
                "Remove dead or diseased plant material."
            ]
        },

        "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
            "status": "Disease Detected",
            "crop": "Grape",
            "disease": "Leaf Blight",
            "prevention": [
                "Remove infected leaves and plant debris.",
                "Improve canopy ventilation.",
                "Avoid prolonged moisture on foliage.",
                "Monitor vines regularly."
            ]
        },

        # ---------------- PEACH ----------------

        "Peach___Bacterial_spot": {
            "status": "Disease Detected",
            "crop": "Peach",
            "disease": "Bacterial Spot",
            "prevention": [
                "Remove severely affected plant material.",
                "Maintain good orchard sanitation.",
                "Avoid unnecessary injury to leaves and fruit.",
                "Monitor plants regularly for new symptoms."
            ]
        },

        "Peach___Healthy": {
            "status": "Healthy",
            "crop": "Peach",
            "disease": "No disease detected",
            "prevention": [
                "Continue regular orchard monitoring.",
                "Maintain proper irrigation and nutrition.",
                "Prune appropriately for air circulation.",
                "Remove dead plant material."
            ]
        },

        # ---------------- POTATO ----------------

        "Potato___Early_blight": {
            "status": "Disease Detected",
            "crop": "Potato",
            "disease": "Early Blight",
            "prevention": [
                "Remove infected plant debris.",
                "Maintain proper crop rotation where possible.",
                "Avoid prolonged leaf wetness.",
                "Monitor lower leaves for early symptoms."
            ]
        },

        "Potato___Healthy": {
            "status": "Healthy",
            "crop": "Potato",
            "disease": "No disease detected",
            "prevention": [
                "Continue regular field monitoring.",
                "Maintain appropriate irrigation and nutrition.",
                "Manage weeds and crop residue.",
                "Inspect leaves regularly."
            ]
        },

        "Potato___Late_blight": {
            "status": "Disease Detected",
            "crop": "Potato",
            "disease": "Late Blight",
            "prevention": [
                "Remove severely infected plant material.",
                "Monitor crops closely during cool and wet conditions.",
                "Avoid prolonged moisture on foliage.",
                "Use integrated disease-management practices."
            ]
        },

        # ---------------- STRAWBERRY ----------------

        "Strawberry___Healthy": {
            "status": "Healthy",
            "crop": "Strawberry",
            "disease": "No disease detected",
            "prevention": [
                "Continue regular crop monitoring.",
                "Maintain good field sanitation.",
                "Provide appropriate irrigation.",
                "Remove damaged or dead leaves."
            ]
        },

        "Strawberry___Leaf_scorch": {
            "status": "Disease Detected",
            "crop": "Strawberry",
            "disease": "Leaf Scorch",
            "prevention": [
                "Remove severely affected leaves.",
                "Maintain good field sanitation.",
                "Avoid excessive leaf wetness.",
                "Monitor new leaves regularly."
            ]
        },

        # ---------------- TOMATO ----------------

        "Tomato___Bacterial_spot": {
            "status": "Disease Detected",
            "crop": "Tomato",
            "disease": "Bacterial Spot",
            "prevention": [
                "Remove severely infected leaves and plant debris.",
                "Avoid handling plants when foliage is wet.",
                "Improve crop sanitation.",
                "Use healthy planting material."
            ]
        },

        "Tomato___Early_blight": {
            "status": "Disease Detected",
            "crop": "Tomato",
            "disease": "Early Blight",
            "prevention": [
                "Remove infected leaves and plant debris.",
                "Maintain good air circulation.",
                "Avoid prolonged leaf wetness.",
                "Practice crop rotation where possible."
            ]
        },

        "Tomato___Healthy": {
            "status": "Healthy",
            "crop": "Tomato",
            "disease": "No disease detected",
            "prevention": [
                "Continue regular plant inspection.",
                "Maintain proper irrigation and nutrition.",
                "Keep the growing area clean.",
                "Monitor leaves regularly for early symptoms."
            ]
        },

        "Tomato___Late_blight": {
            "status": "Disease Detected",
            "crop": "Tomato",
            "disease": "Late Blight",
            "prevention": [
                "Remove severely infected plant material.",
                "Monitor closely during cool and wet conditions.",
                "Avoid prolonged leaf wetness.",
                "Use integrated disease-management practices."
            ]
        },

        "Tomato___Septoria_leaf_spot": {
            "status": "Disease Detected",
            "crop": "Tomato",
            "disease": "Septoria Leaf Spot",
            "prevention": [
                "Remove infected lower leaves.",
                "Clear infected plant debris.",
                "Improve air circulation around plants.",
                "Avoid overhead watering where possible."
            ]
        },

        "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
            "status": "Disease Detected",
            "crop": "Tomato",
            "disease": "Yellow Leaf Curl Virus",
            "prevention": [
                "Monitor and manage whitefly populations.",
                "Remove severely affected plants where appropriate.",
                "Control weeds that may harbor insect vectors.",
                "Use healthy planting material and monitor plants regularly."
            ]
        }
    }

    # Match class names without being affected by capitalization
    normalized_class = disease_class.lower()

    for class_name, result in recommendations.items():

        if class_name.lower() == normalized_class:
            return result
    # Fallback for unexpected class names
    return {
        "status": "Unknown",
        "crop": "Unknown",
        "disease": disease_class,
        "prevention": [
            "Recheck the image prediction.",
            "Inspect the plant manually for symptoms.",
            "Consult a local agricultural expert if symptoms persist."
        ]
    }


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    test_class = "Tomato___Early_Blight"

    result = get_decision_support(test_class)

    print("=" * 60)
    print("PREVENTIVE DECISION SUPPORT")
    print("=" * 60)

    print(f"Status  : {result['status']}")
    print(f"Crop    : {result['crop']}")
    print(f"Disease : {result['disease']}")

    print("\nRecommendations:")

    for item in result["prevention"]:
        print(f"- {item}")