import streamlit as st
from agent import agent
from tools.image_tool import detect_skin_tone
import random


st.set_page_config(page_title="AI Fashion Stylist", layout="wide")

st.markdown("""
<style>

.title {
    font-size: 48px;
    font-weight: 700;
    text-align: center;
    background: linear-gradient(90deg,#ff7a18,#ffb347,#ff4e50);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: glow 3s infinite alternate;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #555;
}

@keyframes glow {
    from { text-shadow: 0 0 10px rgba(255,122,24,0.3); }
    to { text-shadow: 0 0 25px rgba(255,78,80,0.8); }
}

</style>

<div class="title">✨ Rangify AI</div>
<div class="subtitle">
Your Intelligent AI Fashion Stylist – Discover Colors, Style, and Confidence
</div>

""", unsafe_allow_html=True)

st.divider()


if "result" not in st.session_state:
    st.session_state.result = None


# Input Section
st.subheader(" Personal Features")

colA, colB, colC = st.columns(3)

with colA:
    eye = st.selectbox("Eye Color", ["brown", "blue", "green", "black"])

with colB:
    skin = st.selectbox("Skin Tone", ["warm", "cool", "neutral"])

with colC:
    gender = st.selectbox("Gender", ["women", "men"])


st.divider()


# Image Upload Section
st.subheader("📤 Upload Face Image (Optional)")
uploaded_image = st.file_uploader(
    "Upload Image",
    type=["jpg", "png", "jpeg"]
)


# Camera Section
st.subheader("📷 Or Capture from Camera")

col1, col2, col3 = st.columns([1,2,1])

with col2:
    camera_image = st.camera_input("Take a photo")


@st.cache_data
def detect_skin_cached(img):
    return detect_skin_tone(img)


detected_tone = None

if uploaded_image is not None:
    detected_tone = detect_skin_cached(uploaded_image)
    st.success(f"Detected Skin Tone: {detected_tone}")
    skin = detected_tone.lower()

elif camera_image is not None:
    detected_tone = detect_skin_cached(camera_image)
    st.success(f"Detected Skin Tone (Camera): {detected_tone}")
    skin = detected_tone.lower()


st.divider()




def show_color_palette(colors):

    st.subheader("🎨 Color Palette Preview")

    cols = st.columns(len(colors))

    for i, color in enumerate(colors):

        cols[i].markdown(
            f"""
            <div style="
            background:{color.lower()};
            height:100px;
            border-radius:12px;
            display:flex;
            align-items:center;
            justify-content:center;
            color:white;
            font-weight:bold;">
            {color}
            </div>
            """,
            unsafe_allow_html=True
        )


def style_explanation(eye, skin):

    if skin == "warm":
        return "Warm skin tones look best with earthy colors like olive, terracotta and mustard."

    elif skin == "cool":
        return "Cool skin tones match jewel colors like sapphire, lavender and plum."

    else:
        return "Neutral skin tones can wear both warm and cool colors."


def sustainability_tip(color):

    tips = {
        "olive": "Olive outfits pair well with reused denim pieces.",
        "mustard": "Mustard works great with vintage clothing.",
        "terracotta": "Earth tones support sustainable fashion cycles."
    }

    return tips.get(color.lower(),
        "Try mixing this color with clothes you already own.")


# Generate Button Centered
colX, colY, colZ = st.columns([2,1,2])

with colY:
    generate = st.button("✨ Generate Advice")


if generate:

    prompt = f"""
    Gender: {gender}
    Eye color: {eye}
    Skin tone: {skin}
    """

    with st.spinner("Generating AI fashion advice..."):
        st.session_state.result = agent(prompt, skin, gender)


result = st.session_state.result


if result:

    st.divider()

    st.subheader("🎯 Recommended Colors")

    for color in result["palette"]:
        st.write("✔", color)

    show_color_palette(result["palette"])


    st.divider()

    st.subheader("🖼 Outfit Inspiration")

    if result.get("links"):

        cols = st.columns(3)

        for i, item in enumerate(result["links"][:6]):

            with cols[i % 3]:

                if item.get("image"):
                    st.image(item["image"], width="stretch")

                if item.get("source"):
                    st.markdown(f"[🔗 View Outfit Inspiration]({item['source']})")

    else:
        st.warning("No outfit inspiration found.")


    st.divider()

    colA, colB = st.columns(2)

    st.divider()

st.subheader("🤖 AI Stylist Advice")

if result and result.get("ai_advice"):
    st.info(result["ai_advice"])

    with colA:
        st.subheader("🧠 Style Insight")
        st.write(style_explanation(eye, skin))

        st.subheader("🌱 Sustainability Tip")

        if result.get("palette"):
            tip = sustainability_tip(result["palette"][0])
            st.write(tip)

    with colB:

        st.subheader("📷 Uploaded / Captured Image")

        if uploaded_image is not None:
            st.image(uploaded_image, caption="Uploaded Image")

        elif camera_image is not None:
            st.image(camera_image, caption="Captured Photo")

        st.subheader("Detected Skin Tone")

        if detected_tone:
            st.write(detected_tone.lower())
        else:
            st.write(skin)


    st.divider()

    score = random.randint(80,95)
    st.metric("⭐ Style Match Score", f"{score}%")