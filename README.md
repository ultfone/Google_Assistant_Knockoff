# Google_Assistant_Knockoff
This is Stupid Meaningless Project about a chatbot(gemini 1.5 technically) which can  listen to your voice ,interpret it and speak the responses it generates

## Overview
This is a simple voice assistant that uses speech recognition to capture user input, processes the input with Google Gemini AI, and responds with generated text converted to speech.

## Features
- Captures user speech using a microphone
- Sends the captured speech as text to Google Gemini AI
- Converts the AI's response to speech using Google Text-to-Speech (gTTS)
- Plays the response using Pygame's audio module

## Requirements
Ensure you have the following dependencies installed:
- Python 3.x
- `speechrecognition`
- `google-generativeai`
- `gtts`
- `pygame`

## Installation
1. Clone this repository or download the script.
2. Install the required dependencies:
   ```sh
   pip install speechrecognition google-generativeai gtts pygame
   ```

## Usage
1. Run the script:
   ```sh
   python script.py
   ```
2. Speak into the microphone when prompted.
3. The AI will generate a response and speak it back to you.
4. The process will continue in a loop until manually stopped with `CTRL+C`.

## Notes
- Ensure your microphone is properly set up and configured.
- The script continuously listens for input until manually exited.
- API key must be configured for Google Gemini AI in the script.

## License
This project is for educational purposes only. Use responsibly.

