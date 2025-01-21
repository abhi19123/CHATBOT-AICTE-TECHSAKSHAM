# AI Chatbot with Flask and PyTorch

A modern chatbot implementation using PyTorch for the AI model and Flask for the web interface. The chatbot can be trained on custom intents and provides real-time responses through a web interface.

## Features
- Custom intent-based chatbot using PyTorch
- RESTful API using Flask
- Real-time chat interface with JavaScript
- Customizable training data through intents.json
- Two deployment options:
  - Integrated Flask app with templates
  - Standalone frontend with API

## Prerequisites
- Python 3.8+
- pip package manager

## Installation

1. Clone the repository:
```bash
git clone https://github.com/python-engineer/chatbot-deployment.git
cd chatbot-deployment
```

2. Create and activate virtual environment:
```bash
python -m venv venv
. venv/bin/activate
```

3. Install dependencies:
```bash
pip install Flask torch torchvision nltk
```

4. Download NLTK data:
```python
python -c "import nltk; nltk.download('punkt')"
```

## Training the Chatbot

1. Customize the intents in `intents.json` with your own intents and responses

2. Train the model:
```bash
python train.py
```

3. The trained model will be saved as `data.pth`

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your browser and navigate to `http://localhost:5000`

## Project Structure
- `app.py`: Flask application and API endpoints
- `chat.py`: Chatbot inference logic
- `train.py`: Model training script
- `model.py`: Neural network architecture
- `nltk_utils.py`: Text processing utilities
- `intents.json`: Training data with intents and responses
- `static/`: Frontend assets (CSS, JS)
- `templates/`: HTML templates
- `standalone-frontend/`: Separate frontend implementation

## API Endpoints
- `POST /predict`: Get chatbot response
  - Request body: `{"message": "your message here"}`
  - Response: `{"answer": "chatbot response"}`

## Customization
You can customize the chatbot by:
1. Modifying intents in `intents.json`
2. Adjusting the neural network architecture in `model.py`
3. Changing the chat interface in `templates/base.html`
