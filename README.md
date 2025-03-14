# Multilingual Text-to-Speech Converter

## 🗣 Overview
This is a Streamlit-based web application that converts text into speech for multiple languages. The app automatically detects the language of the input text and generates speech accordingly.

## 🚀 Features
- Detects the language of the input text automatically.
- Converts text to speech using Google Text-to-Speech (gTTS).
- Supports multiple languages.
- Provides an option to play and download the generated audio file.

## 🛠 Installation & Setup
### Prerequisites
Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Install Required Packages
Run the following command to install the necessary dependencies:
```bash
pip install streamlit gtts langdetect
```

### Run the Application
Execute the following command in your terminal:
```bash
streamlit run app.py
```

## 📂 Project Structure
```
📁 Multilingual-TTS
│── app.py             # Main application script
│── requirements.txt   # List of required packages
│── README.md          # Project documentation
```

## 🎯 Usage
1. Run the application.
2. Enter text in any language in the provided text box.
3. Click the "Convert to Speech" button.
4. The app will detect the language and generate speech.
5. Listen to the audio or download it for later use.

## 🤝 Contributing
Feel free to fork this repository, create a feature branch, and submit a pull request with your improvements!

## 📜 License
This project is open-source and available under the MIT License.

## 🌟 Acknowledgments
- [Streamlit](https://streamlit.io/)
- [Google Text-to-Speech (gTTS)](https://pypi.org/project/gTTS/)
- [langdetect](https://pypi.org/project/langdetect/)

---
Happy coding! 🚀

