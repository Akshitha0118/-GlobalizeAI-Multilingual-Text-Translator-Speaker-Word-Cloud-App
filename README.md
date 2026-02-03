# GlobalizeAI-Multilingual-Text-Translator-Speaker-Word-Cloud-App

Globalize is an interactive **Streamlit web app** that allows users to **detect language, translate text into multiple languages, generate word clouds, and convert text to speech** — all in one place.

It combines **NLP, Translation, Visualization, and Text-to-Speech** to make multilingual text more accessible and engaging.

---

## 🚀 Features

✨ **Automatic Language Detection**  
Detects the input language using `langdetect`.

🌐 **Multi-Language Translation**  
Translate text into multiple languages using **Google Translator**.

🔊 **Text-to-Speech (TTS)**  
Listen to translated text using **gTTS** (only supported speech languages shown).

☁️ **Word Cloud Visualization**  
Generate a word cloud from English-translated text to visualize key terms.

🎨 **Modern Glass UI**  
Beautiful glassmorphism UI with gradient background and smooth layout.

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Google Text-to-Speech (gTTS)**
- **Deep Translator**
- **NLTK**
- **WordCloud**
- **Matplotlib**

---

## 📦 Installation

### 1️⃣ Clone the Repository
git clone https://github.com/Akshitha0118/GlobalizeAI-Multilingual-Text-Translator-Speaker-Word-Cloud-App
.git
cd globalize
---
### 2️⃣ Install Dependencies
pip install -r requirements.txt
---
### 3️⃣ Run the App
streamlit run app.py
---

The app will open automatically in your browser 🌐
---
## 🧠 How It Works

User enters a paragraph

App detects the input language

Text is translated to English (if required)

Word cloud is generated from English text

User selects target languages

Translated text is spoken aloud using gTTS
---
## 🌍 Supported Languages

Displays only gTTS-supported languages for speech

Translation supports many global languages
---
## 📸 UI Preview

Glass UI • Gradient Background • Responsive Layout
---
## 🔒 Notes

Internet connection required (Google Translation & TTS)

Speech output depends on gTTS language availability
