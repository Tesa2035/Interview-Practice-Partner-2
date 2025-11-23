<<<<<<< HEAD
# Interview Practice Partner

An AI-powered agent that helps users prepare for job interviews by conducting mock interviews, asking follow-up questions, and providing detailed feedback.

## Features
- **Role-Specific Interviews**: Practice for Sales, Software Engineering, or Retail roles.
- **Voice Interaction**: Speak your answers using the Web Speech API.
- **AI Interviewer**: Powered by Groq (Llama 3) for fast, conversational responses.
- **Feedback System**: Detailed analysis of your performance with strengths and areas for improvement.
- **Modern UI**: Glassmorphism design with dark mode.

## Architecture
- **Backend**: Python (FastAPI)
    - Handles interview state and logic.
    - Integrates with Groq API for LLM inference.
- **Frontend**: HTML/CSS/JS (Vanilla)
    - Responsive UI.
    - Web Speech API for Speech-to-Text (STT) and Text-to-Speech (TTS).

## Setup Instructions

1. **Prerequisites**
    - Python 3.8+
    - A Groq API Key

2. **Installation**
    ```bash
    # Clone the repository (if applicable)
    
    # Create virtual environment
    python3 -m venv venv
    source venv/bin/activate
    
    # Install dependencies
    pip install -r requirements.txt
    ```

3. **Running the Application**
    
    **Backend:**
    ```bash
    # In the root directory
    source venv/bin/activate
    cd backend
    uvicorn main:app --reload
    ```
    The backend will run at `http://localhost:8000`.

    **Frontend:**
    Simply open `frontend/index.html` in a modern browser (Chrome/Edge recommended for Web Speech API support).

4. **Usage**
    - Open the frontend.
    - Enter your Groq API Key (if not set in backend environment variables).
    - Select a role.
    - Start chatting or speaking!
    - Click "End Interview" to get feedback.

## Design Decisions
- **FastAPI**: Chosen for speed and ease of creating REST APIs.
- **Groq**: Chosen for its ultra-low latency, essential for a conversational voice interface.
- **Vanilla JS**: Kept the frontend lightweight and dependency-free for this prototype.
- **Web Speech API**: Used native browser capabilities for STT/TTS to reduce latency and complexity compared to server-side audio processing.
=======
# Interview-Practice-Partner
>>>>>>> 0e4e973e064e3382dd3f1d735bebf37eafb517a5
