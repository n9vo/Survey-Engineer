# SurveyEngineer

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

SurveyEngineer is a proof-of-concept open-source tool designed to create and edit surveys using AI-driven prompts. It simplifies the process of survey generation by converting natural language input from the user into structured JSON data.

## Features

- **AI-Powered Survey Creation**: Automatically generate surveys from simple user descriptions using OpenAI's GPT-3.5.
- **Multiple Question Types**: Supports various question types including voice recording, multiple choice, free response, boolean, and sliders.
- **Real-Time Survey Editing**: Update and modify existing surveys based on user input while maintaining the original format.
- **Web Interface**: User-friendly web interface built with Flask to create and manage surveys.

## Installation

To install and run SurveyEngineer, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/nevolua/surveyengineer.git
    cd surveyengineer
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Fill in your OpenAI credentials on **line 9** of main.py:
    ```py
    client = OpenAI(organization="", api_key="")
    ```

4. Start the application:
    ```sh
    python main.py
    ```

## Usage

1. **Access the Web Interface**: Open your browser and navigate to `http://localhost:80` to access the SurveyEngineer interface.
2. **Create a Survey**: Describe your survey and let the AI generate the JSON structure.
3. **Modify Surveys**: Use the update functionality to make changes to your survey based on specific user inputs.

## Example

Here's an example of a generated JSON survey format:

```json
{
    "survey_name": "Customer Feedback",
    "questions": [
        {
            "prompt": "How satisfied are you with our service?",
            "id": 1,
            "type": "slider",
            "slider_min": 1,
            "slider_max": 10
        },
        {
            "prompt": "Please provide additional comments.",
            "id": 2,
            "type": "free_response"
        }
    ]
}
