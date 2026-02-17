# 🎙️ Virtual Assistant (Python)

A voice-controlled desktop assistant built using Python that performs basic automation tasks using speech recognition and text-to-speech.

---

## 📌 Project Overview

The assistant follows this processing pipeline:

$$
\text{Speech Input} \rightarrow 
\text{Speech Recognition} \rightarrow 
\text{Command Processing} \rightarrow 
\text{Text-to-Speech Output}
$$

The goal of this project is to explore voice-based automation and practical Python implementation of system-level tasks.

---

## 🚀 Features

$$
\begin{aligned}
&\text{• Time Detection} \\
&\text{• Date Detection} \\
&\text{• Open Notepad} \\
&\text{• Open YouTube} \\
&\text{• Google Search via Voice} \\
&\text{• Exit Commands}
\end{aligned}
$$

---

## 🛠️ Technologies Used

$$
\begin{aligned}
&\text{Python 3} \\
&\text{pyttsx3 (Text-to-Speech Engine)} \\
&\text{SpeechRecognition (Google API)} \\
&\text{PyAudio (Microphone Input)} \\
&\text{datetime, os, webbrowser}
\end{aligned}
$$

---

## 📦 Installation

### Clone Repository
```bash
git clone https://github.com/AbhiramMandala/virtual_assistant.git
cd virtual_assistant

```

### Install Dependencies

$$
\texttt{pip install -r requirements.txt}
$$

If PyAudio fails on Windows:

$$
\texttt{pip install pipwin}
$$

$$
\texttt{pipwin install pyaudio}
$$

---

## ▶️ Execution

$$
\texttt{python assistant.py}
$$

After execution, the assistant greets the user and begins listening continuously.

---

## 🧠 Command Logic

$$
\text{If } "time" \in \text{command} \Rightarrow \text{Return Current Time}
$$

$$
\text{If } "date" \in \text{command} \Rightarrow \text{Return Current Date}
$$

$$
\text{If } "open youtube" \Rightarrow \text{Launch Browser}
$$

$$
\text{If } "bye" \lor "stop" \Rightarrow \text{Terminate Program}
$$

---

## ⚙️ System Requirements

$$
\begin{aligned}
&\text{Python} \geq 3.0 \\
&\text{Working Microphone} \\
&\text{Internet Connection (Required for Recognition)}
\end{aligned}
$$

---

## 🛑 Troubleshooting

### Microphone Issues

$$
\text{Check system input settings and ensure device is default.}
$$

### Recognition Errors

$$
\text{Ensure stable internet and minimal background noise.}
$$

### PyAudio Installation Errors

$$
\text{Match Python architecture with system (32-bit / 64-bit).}
$$

---

## 🔮 Future Enhancements

$$
\begin{aligned}
&\text{Weather API Integration} \\
&\text{System Shutdown / Restart Commands} \\
&\text{Music Playback} \\
&\text{Graphical User Interface (GUI)} \\
&\text{Wake Word Detection}
\end{aligned}
$$

---

## 🤝 Contribution Model

$$
\textbf{Contributions\ are\ welcome!}
$$

$$
\text{Feel free to fork the repository and submit a pull request } \\
\text{with improvements or new features.}
$$


---

## 👨‍💻 Author

$$
\text{Abhiram Mandala}
$$
