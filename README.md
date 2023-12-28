# AI Personal Assistant

## Overview

Welcome to the AI Personal Assistant repository! This project was developed as a final year project by me, it is aimed at being a powerful and customizable artificial intelligence assistant that can assist you with various tasks, streamline your daily activities, and enhance your overall productivity. - This is progress.

## How it works
The AI assistant is activated at the mention of the activation word - "Jasper" by default.

On first launch, all speeches, though recognized by the PA are not addressed until the activation word is mentioned, when activation word is mentioned, the GUI initially black turns green and the PA can now listen to prompt and address them.

When the user speaks, the PA uses the Google Speech-to-Text library to transcribe the audio received from the user's microphone to text.

The program checks if the text contains termination word like "bye", if it does, the program terminates, the GUI turns red and closes after three seconds, if it doesn't, the text is then sent to the saved model to determine the intent of the input.

The [model](https://github.com/zeekielcodes/AI-PA-model/blob/main/model.ipynb) trained on a small [dataset](https://github.com/zeekielcodes/AI-PA-model/blob/main/my-dataset.csv) using the Multinomial Naive Bayes Algorithm from Scikit-Learn processes the text and returns a predicted intent.

In the program, each possible intent is mapped to a function which gets called depending on what intent the model returns.

Some features have not been completely integrated, some implemented, but the dataset for the model has not been modified and model retrained to integrate/activate them.

Inspired by Jarvis in Iron Man - This is my staying point and progress, depending on when you're viewing this, cause I'll come back to improve this as I grow in my programming career.

Contributions are welcomed too.

## Features

- **Voice Recognition:** Communicate with your assistant through natural language and voice commands.
- **Task Automation:** Automate repetitive tasks to save time and increase efficiency.
- **Information Retrieval:** Access information from the web, weather updates, news, and more.
- **Calendar Integration:** Manage your schedule and receive reminders for important events.
- **Customizable Modules:** Extend the functionality by adding custom modules tailored to your needs.
- **Security:** Prioritize the security and privacy of your personal information.

## Getting Started

Follow these steps to get started with the AI Personal Assistant:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/zeekielcodes/AI-Personal-Assisatant.git
   cd ai-personal-assistant

2. **Install Dependencies:**
   ```python
   pip install -r requirements.txt

4. **Configuration:**
Customize the configuration files to set up your preferences and API keys.

5. **Run the Assistant:**
   ```python
   python main.py

7. **Interact:**
Start interacting with your personal assistant and explore its capabilities!

## Contributing

If you would like to contribute to the development of the AI Personal Assistant, feel free to fork the repository, make your changes, and submit a pull request. Contributions are always welcome!

## Issues and Feedback

If you encounter any issues or have feedback, please open an issue on the GitHub repository. Your input is valuable in improving the overall functionality and user experience.

## Usage and Access

Feel free to modify and distribute the code for personal or commercial use.

Happy coding, and enjoy your AI Personal Assistant!
