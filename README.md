# IntelliGenie - A Personalized Voice Assistant

## Overview

IntelliGenie is a versatile voice-based personal assistant designed to simplify your daily tasks. With capabilities including sending emails and WhatsApp messages, managing apps, taking notes, and providing weather updates, IntelliGenie aims to enhance productivity through intuitive voice commands.

## Features

- **Voice Commands**: Interact with IntelliGenie using natural language commands.
- **Email Integration**: Send emails using Gmail.
- **Weather and Time Updates**: Get current weather and time information.
- **Application Management**: Open and close applications.
- **Media Control**: Pause, play, mute, and adjust volume for media.
- **Reminders and Alarms**: Set alarms and remember important notes.
- **Web Searches**: Search Google, YouTube, and Wikipedia.
- **Screenshots and Photos**: Capture screenshots and take photos.
- **Shutdown**: Shut down the system on command.

## Installation

### Dependencies

Make sure to install the following Python libraries:

- `pyttsx3` for text-to-speech
- `speech_recognition` for voice recognition
- `requests` and `BeautifulSoup` for web scraping
- `pyautogui` for GUI automation
- `google-auth`, `google-auth-oauthlib`, `google-auth-httplib2`, and `google-api-python-client` for Gmail integration

You can install these using pip:

```bash
pip install pyttsx3 speech_recognition requests beautifulsoup4 pyautogui google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

### Gmail Setup

1. **Create OAuth Credentials**: Visit [Google Cloud Console](https://console.developers.google.com/) to create OAuth credentials for Gmail API access. Download the `credentials.json` file.
2. **Token Storage**: Ensure `token.pickle` is available for storing authentication tokens.

## Usage

1. **Run IntelliGenie**: Execute the script to start IntelliGenie and interact with it using voice commands.

```bash
python intelligenie.py
```

2. **Commands**: 
    - Say "Khul Ja Sim Sim" to activate the assistant.
    - Use commands like "open [app name]", "set an alarm", "send an email", "play music", and more.
    - To stop, say "go to sleep" or "finally sleep".

## Code Overview

- **Text-to-Speech and Voice Recognition**: Handles communication between the user and the assistant.
- **Web Interaction**: Fetches weather and time information, performs web searches.
- **Email and WhatsApp Integration**: Manages email sending and WhatsApp messaging.
- **Application Control**: Opens, closes, and manages applications.
- **Media Control**: Adjusts media playback and volume.

## Notes

- Ensure microphone permissions are granted for voice recognition.
- Customize the `email_list` dictionary and other settings as needed.
- The assistant supports various functionalities, including reminders and taking photos, making it a comprehensive tool for daily use.
