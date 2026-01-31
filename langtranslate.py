import streamlit as st
from gtts import gTTS
from gtts.lang import tts_langs
from deep_translator import GoogleTranslator
from langdetect import detect
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
import nltk
from io import BytesIO

# ----------------------------
# SAFE NLTK DOWNLOAD
# ----------------------------
@st.cache_resource
def download_nltk():
    nltk.download("punkt")

download_nltk()

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(page_title="Globalize", layout="wide")

# ----------------------------
# ADVANCED CSS (GLASS UI)
# ----------------------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #667eea, #764ba2);
}
.block-container {
    background: rgba(255,255,255,0.12);
    padding: 2rem;
    border-radius: 20px;
    backdrop-filter: blur(14px);
}
h1, h2, h3 {
    text-align: center;
    color: white;
}
textarea {
    border-radius: 12px !important;
}
.stButton>button {
    background: linear-gradient(90deg,#ff9966,#ff5e62);
    color: white;
    font-weight: bold;
    border-radius: 12px;
    padding: 0.5rem 1.2rem;
}
.center-box {
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# TITLE
# ----------------------------
st.title("🌍 Globalize — Translate • Visualize • Speak")

# ----------------------------
# gTTS SUPPORTED LANGUAGES ONLY
# ----------------------------
GTTS_LANGS = tts_langs()
LANGUAGE_MAP = {name.title(): code for code, name in GTTS_LANGS.items()}

# ----------------------------
# TEXT TO SPEECH
# ----------------------------
def speak(text, lang):
    tts = gTTS(text=text, lang=lang)
    audio = BytesIO()
    tts.write_to_fp(audio)
    st.audio(audio.getvalue(), format="audio/mp3")

# ----------------------------
# WORD CLOUD
# ----------------------------
def generate_wordcloud(text):
    words = word_tokenize(text.lower())
    wc = WordCloud(
        width=900,
        height=450,
        background_color="white",
        colormap="viridis"
    ).generate(" ".join(words))

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    return fig

# ----------------------------
# INPUT SECTION
# ----------------------------
col1, col2 = st.columns(2)

with col1:
    paragraph = st.text_area("✍️ Enter your paragraph", height=220)

with col2:
    selected_languages = st.multiselect(
        "🌐 Select languages (Speech supported only)",
        list(LANGUAGE_MAP.keys())
    )

# ----------------------------
# READ ORIGINAL
# ----------------------------
if st.button("🔊 Read Original Text"):
    if paragraph.strip():
        speak(paragraph, "en")

# ----------------------------
# LANGUAGE DETECTION + ENGLISH TRANSLATION
# ----------------------------
english_text = ""

if paragraph.strip():
    try:
        detected_lang = detect(paragraph)
        st.success(f"Detected Language Code: **{detected_lang}**")
    except:
        detected_lang = "en"

    if detected_lang != "en":
        english_text = GoogleTranslator(
            source="auto",
            target="en"
        ).translate(paragraph)

        st.subheader("🌐 Universal English Translation")
        st.write(english_text)
    else:
        english_text = paragraph

# ----------------------------
# CENTER WORD CLOUD
# ----------------------------
if english_text:
    st.markdown("<h3>☁️ Word Cloud</h3>", unsafe_allow_html=True)
    st.markdown('<div class="center-box">', unsafe_allow_html=True)
    st.pyplot(generate_wordcloud(english_text))
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------
# TRANSLATE + SPEAK
# ----------------------------
if st.button("🌍 Translate & Read Aloud"):
    for lang_name in selected_languages:
        lang_code = LANGUAGE_MAP[lang_name]

        translated = GoogleTranslator(
            source="auto",
            target=lang_code
        ).translate(paragraph)

        st.subheader(f"🗣 {lang_name}")
        st.write(translated)
        speak(translated, lang_code)
