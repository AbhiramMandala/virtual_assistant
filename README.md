# 🎙️ Python Voice Assistant

A simple voice-controlled desktop assistant built using Python.  
This project demonstrates speech recognition, text-to-speech conversion, and basic automation.

---

## 📌 Project Overview

The assistant listens to voice input, converts it to text, processes the command, and responds using speech output.

$$
\textbf{Flow:} \quad 
\text{Speech Input} \rightarrow 
\text{Speech Recognition} \rightarrow 
\text{Command Processing} \rightarrow 
\text{Text-to-Speech Output}
$$

---

## 🚀 Features

- 🕒 Current Time Detection  
- 📅 Current Date Detection  
- 📝 Opens Notepad  
- ▶️ Opens YouTube  
- 🔎 Google Search via Voice  
- 👋 Exit Command Support  

---

## 🛠️ Technologies Used

$$
\begin{aligned}
&\text{Python} \\
&\text{pyttsx3 (Text-to-Speech)} \\
&\text{SpeechRecognition (Google API)} \\
&\text{datetime, os, webbrowser}
\end{aligned}
$$

---

## ⚙️ System Requirements

$$
\begin{aligned}
&\text{Python} \geq 3.0 \\
&\text{Working Microphone} \\
&\text{Internet Connection (for recognition)}
\end{aligned}
$$

---

## 📦 Installation

```bash
pip install pyttsx3 SpeechRecognition pyaudio
