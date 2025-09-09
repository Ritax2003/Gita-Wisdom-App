# 🌸 Gita Wisdom App  

[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)   [![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)  [![Release](https://img.shields.io/github/v/release/Ritax2003/Gita-Wisdom-App)](https://github.com/Ritax2003/Gita-Wisdom-App/releases)   [![Downloads](https://img.shields.io/github/downloads/Ritax2003/Gita-Wisdom-App/total?color=yellow)](https://github.com/Ritax2003/Gita-Wisdom-App/releases)   [![Stars](https://img.shields.io/github/stars/Ritax2003/Gita-Wisdom-App?style=social)](https://github.com/Ritax2003/Gita-Wisdom-App/stargazers)  

---

*"You have a right to perform your prescribed duties, but you are not entitled to the fruits of your actions."*  
— *Bhagavad Gita 2.47*  

The **Gita Wisdom App** is a modern **AI-powered desktop application** that provides spiritual guidance from the **Bhagavad Gita**, helping users navigate contemporary challenges using timeless wisdom.  

---

## 📖 Overview  

The **Gita Wisdom App** is built using **PyQt5** and integrates **Google Gemini AI** with curated verses from the Bhagavad Gita.  

It allows users to explore spiritual teachings, ask questions, and receive contextual guidance inspired by Krishna.  

Inspired by [Subrata’s Gita Wisdom Guide](https://github.com/subrata2003/gita-wisdom-guide).  

The app features sample queries, a clean multi-tab interface, update management, and secure API key handling.  

---

## ✨ Key Features  

- 🔑 **API Key Management**: Prompted once, securely saved for future use  
- 🙏 **AI-Generated Guidance**: Personalized Krishna-inspired responses  
- 📖 **Sample Queries**: One-click spiritual Q&A with toggleable answers  
- 📊 **Dashboard Tabs**:  
  - Gita Wisdom Guide  
  - Sample Questions  
  - Update  
- 🌐 **Internet Status**: Always visible in the UI  
- 🔗 **Quick Links**: Wikipedia reference for Bhagavad Gita  
- 📜 **Stats Display**: Total chapters and verses included  
- ⚠️ **Disclaimer**: Consult professionals for serious concerns  
- 🔄 **Updater**: Checks and downloads GitHub releases  
- 🎨 **Custom Icon**: Packaged with PyInstaller for distribution  

---

## 🛠 Core Components  

| Component       | Technology             | Purpose                                         |
|-----------------|----------------------|-------------------------------------------------|
| Desktop UI       | PyQt5                 | Modern multi-tab interface                      |
| AI Handler       | Google Gemini API      | Generates Krishna-inspired responses           |
| Config Manager   | JSON (local file)      | Stores API keys and app settings               |
| Updater          | GitHub Releases + Python | Checks, downloads & installs updates      |
| Build Tool       | PyInstaller            | Generates distributable .exe files             |

---

## 🚀 Installation  

### 1. Clone the repository:

```bash
git clone https://github.com/Ritax2003/Gita-Wisdom-App.git
cd Gita-Wisdom-App
```

### 2. Install dependencies:
```bash
pip install -r requirements.txt
```
### 3. Run the app:
```bash
python main.py
```

### 4. Build standalone executable (Windows):
```bash
pyinstaller --onefile --windowed --icon=images/app_icon.ico main.py
```

## ▶️ First-Time Setup
### 1. Obtain Google Gemini API Key:
- Visit Google AI Studio
- Sign in with your Google account
- Generate a new API Key

### 2. Launch the App:

- On first run, a dialog will appear asking for your API key

- Enter the key when prompted

### 3. Auto-Save:

- The key is saved in a local config file:
```bash
~/.gita_config.json
```

Only needs to be entered once ,Subsequent runs automatically load the saved API key

## ⚙️ Usage

- Open the app after entering your API key

- Navigate the tabs to:

- Explore Gita Wisdom Guide

- Test Sample Questions

- Check for Updates

- Ask spiritual questions in the input area and receive AI-generated Krishna-inspired guidance

## 🏛 Architecture
User Query → Google Gemini API → Contextual Response → Display in App

## ⚠️ Disclaimer

This tool provides spiritual guidance inspired by the Bhagavad Gita.
For mental health or serious life concerns, please consult a qualified professional.
