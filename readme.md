# 🌸 Gita Wisdom App  

[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)  
[![Release](https://img.shields.io/github/v/release/Ritax2003/Gita-Wisdom-App)](https://github.com/Ritax2003/Gita-Wisdom-App/releases)  
[![Downloads](https://img.shields.io/github/downloads/Ritax2003/Gita-Wisdom-App/total?color=yellow)](https://github.com/Ritax2003/Gita-Wisdom-App/releases)  
[![Stars](https://img.shields.io/github/stars/Ritax2003/Gita-Wisdom-App?style=social)](https://github.com/Ritax2003/Gita-Wisdom-App/stargazers)  

---

*"You have a right to perform your prescribed duties, but you are not entitled to the fruits of your actions."*  
— *Bhagavad Gita 2.47*  

A modern **AI-powered desktop application** that provides spiritual guidance from the **Bhagavad Gita**, helping users navigate contemporary challenges through the timeless wisdom of Lord Krishna.  

---

## 📖 Overview  

The **Gita Wisdom App** is a PyQt5-based desktop application that integrates **Google Gemini AI** with curated verses from the Bhagavad Gita.  
It allows users to explore spiritual teachings, ask questions, and receive contextual responses inspired by Krishna’s guidance.  Inspired by https://github.com/subrata2003/gita-wisdom-guide of [Subrata](https://github.com/subrata2003) .

The app also includes sample queries, a clean multi-tab interface, update management, and user-friendly interaction with saved API keys.  

---

## ✨ Key Features  

- 🔑 **API Key Management**: Prompted once on first run, securely saved for reuse  
- 🙏 **AI-Generated Guidance**: Personalized Krishna-inspired responses using Google Gemini  
- 📖 **Sample Queries**: One-click spiritual Q&A with toggleable answers  
- 📊 **Dashboard Tabs**:  
  - Gita Wisdom Guide  
  - Sample Questions
  - Update
- 🌐 **Internet Status**: Always visible in the UI  
- 🔗 **Quick Links**: Wikipedia reference for Bhagavad Gita  
- 📜 **Stats Display**: Total chapters and verses included  
- ⚠️ **Disclaimer**: Encourages consulting professionals for mental health concerns  
- 🔄 **Updater**: GitHub release check  
- 🎨 **Custom Icon**: Packaged with PyInstaller for distribution  

---

## 🏛 Architecture  

```text
User Query → Gemini API → Contextual Response → Display in App

