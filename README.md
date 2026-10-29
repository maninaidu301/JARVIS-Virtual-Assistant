# 🤖 JARVIS – Virtual Assistant

A Python-based voice-controlled virtual assistant that helps users perform everyday tasks using voice commands. JARVIS can open desktop applications, search the web, play YouTube videos, retrieve Wikipedia summaries, and provide other useful features.

## ✨ Features

* 🎙️ **Voice Recognition** – Recognizes spoken commands using speech recognition.
* 🔊 **Text-to-Speech** – Responds to users with a synthesized voice.
* 💻 **Application Control** – Opens Notepad, Discord, Calculator, Command Prompt, and Windows Camera.
* 🌐 **Google Search** – Searches the web using voice commands.
* 📚 **Wikipedia Search** – Retrieves short summaries of topics.
* ▶️ **YouTube Playback** – Searches for and plays YouTube videos.
* 🌍 **IP Address Lookup** – Retrieves the public IP address.
* 😂 **Random Jokes** – Provides jokes for entertainment.
* 💡 **Random Advice** – Shares random advice.
* 💬 **WhatsApp Messaging** – Supports sending WhatsApp messages.
* 📧 **Email** – Supports sending emails through Gmail.
* 📰 **Latest News** – Retrieves news headlines when configured with an API key.
* 🌦️ **Weather Reports** – Retrieves weather information when configured with an API key.
* 🎬 **Trending Movies** – Retrieves trending movies when configured with an API key.

## 🛠️ Technologies Used

* Python
* SpeechRecognition
* PyAudio
* pyttsx3
* Requests
* Wikipedia
* PyWhatKit
* Python Decouple
* PyAutoGUI

## 📂 Project Structure

```text
Virtual Assistant/
│
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── utils.py
│
└── functions/
    ├── __init__.py
    ├── online_ops.py
    └── os_ops.py
```

## ⚙️ Requirements

* Windows operating system
* Python installed on your computer
* Microphone
* Internet connection
* Git (optional, for cloning the repository)

Python 3.11 is a reasonable starting point for this project because some dependencies use older versions.

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/maninaidu301/JARVIS-Virtual-Assistant.git
```

### 2. Open the project directory

```bash
cd JARVIS-Virtual-Assistant
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

If an installation error occurs, check the Python version and the compatibility of the pinned package versions.

### 5. Run the assistant

```bash
python main.py
```

Allow microphone access if Windows asks for permission.

## 🗣️ Example Voice Commands

Try saying:

* "Open Notepad"
* "Open Discord"
* "Open Calculator"
* "Open Camera"
* "Open Command Prompt"
* "Search on Google"
* "Search Wikipedia"
* "Play YouTube"
* "What's my IP address?"
* "Tell me a joke"
* "Give me some advice"
* "What's the weather?"
* "Show trending movies"
* "Tell me the latest news"

The exact commands depend on the conditions implemented in `main.py`.

## 🔑 API Configuration

Some features require external API keys.

* **News:** NewsAPI
* **Weather:** OpenWeather
* **Trending Movies:** The Movie Database (TMDB)

These features won't work until the relevant API credentials are configured.

Email functionality also requires appropriate Gmail authentication, such as an app password where supported.

**Security:** Never publish API keys, passwords, access tokens, or other private credentials in a public repository.

## 🔒 Privacy and Security

* Do not commit `.env` files containing credentials.
* Keep passwords and API keys private.
* Review the files staged for upload before committing.
* Use a `.gitignore` file to exclude virtual environments, cache files, and sensitive configuration files.

## ⚠️ Limitations

* Designed primarily for Windows.
* Requires a working microphone for voice commands.
* Speech recognition and online features require internet access.
* Some desktop application paths may need adjustment for different computers.
* API-dependent features require valid credentials.
* Some dependencies may require version adjustments on newer Python releases.

## 🔮 Future Improvements

* Add a graphical user interface.
* Support more natural voice commands.
* Improve error handling and offline functionality.
* Add reminders and task management.
* Integrate additional productivity features.

## 📄 License

This project is distributed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 👩‍💻 Author

**Mani Kanchi**

GitHub: [@maninaidu301](https://github.com/maninaidu301)

---

⭐ If you find this project useful, consider giving the repository a star!
