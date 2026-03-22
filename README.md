# 👗 AI Personal Style Agent

> *Not just fashion suggestions… but styling powered by AI + your personality.*

---

## 🌟 About the Project

Choosing the right outfit isn’t just about trends — it’s about **you**.

This project is an **AI-powered personal styling assistant** that analyzes your appearance (skin tone, eye color, gender) using image input or real-time camera capture and suggests:

* 🎨 Best color palette for you
* 👗 Outfit inspiration from the web
* 💡 Style insights
* 🌱 Sustainable fashion tips

Instead of guessing what looks good, this system **uses AI + computer vision** to guide you.

---

## 💡 The Idea

Most people struggle with questions like:

* “Which color suits my skin tone?”
* “What should I wear today?”
* “How do I find outfit inspiration quickly?”

So I built a system that does:

```
Upload Photo / Use Camera
        ↓
AI analyzes your appearance
        ↓
Suggests personalized colors
        ↓
Finds outfit inspiration online
        ↓
Displays results instantly
```

---

## 🚀 Features

### 👤 Personalization

* Based on **skin tone + eye color + gender**
* Not generic suggestions

### 📷 Real-Time Camera Support

* Capture photo directly
* No need to upload manually

### 🎨 Smart Color Palette

* Warm / Cool / Neutral tone detection
* Suggests colors like:

  * Olive
  * Mustard
  * Lavender
  * Sapphire

### 🌐 Web-Based Outfit Search

* Searches real outfit inspiration
* Uses dynamic queries like:

  ```
  olive female outfit fashion
  ```

### 🧠 Style Insights

* Explains *why* a color suits you

### 🌱 Sustainability Tips

* Encourages smart clothing reuse

### 📊 Style Score

* Fun + engaging user experience

---

## 🧠 AI Components

This project combines multiple AI concepts:

### 1️⃣ Computer Vision

* Skin tone detection from images
* Built using OpenCV

### 2️⃣ Agent-Based Logic

* Decides color palette based on inputs

### 3️⃣ Web Intelligence

* Fetches real-time outfit inspiration

---

## 🏗️ Architecture

```
Streamlit UI
     ↓
Image Input (Upload / Camera)
     ↓
Computer Vision (Skin Tone Detection)
     ↓
AI Agent (Color Decision)
     ↓
Search Tool (Outfit Inspiration)
     ↓
Final Recommendations UI
```

---

## 🛠️ Tech Stack

| Layer      | Technology            |
| ---------- | --------------------- |
| Frontend   | Streamlit             |
| Backend    | Python                |
| AI / CV    | OpenCV                |
| Web Search | DuckDuckGo (DDGS)     |
| Libraries  | numpy, pandas, pillow |

---

## 🎯 Project Level

👉 Intermediate → Advanced AI Project

Why?

* Combines **Computer Vision + AI + Web Integration**
* Includes **real-time camera input**
* Uses **agent-based decision system**
* Not just UI — actual logic + intelligence

---

## 🔥 What Makes It Unique?

* Not a simple fashion app
* Not hardcoded suggestions
* Uses **real-time user data**
* Combines **AI + personalization + web search**
* Supports **male & female styling separately**

---

## 🚧 Future Improvements

This project can be extended to:

* 👕 Body type detection (Slim / Athletic / Plus)
* 🎯 Seasonal color analysis (Spring / Summer / Winter)
* 🤖 AI outfit generation (using diffusion models)
* 📈 Fashion trend prediction

---

## 🧑‍💻 How to Run

```bash
git clone <your-repo>
cd project-folder

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py
```

---

## 🎤 How to Explain This Project

> "I built an AI-based fashion styling system that uses computer vision to analyze a user’s appearance and suggests personalized color palettes and outfit inspirations. It integrates Streamlit for UI, OpenCV for image processing, and real-time web search to provide dynamic fashion recommendations."

---

## ✨ Final Thought

This project is not just about fashion.

It’s about **bringing AI into everyday decisions** —
making styling smarter, faster, and personalized.

---

⭐ If you like this project, consider giving it a star!
