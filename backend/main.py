from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from interview_manager import InterviewManager
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize InterviewManager
# We'll initialize it lazily or per request if we were handling multiple users properly with sessions.
# For this prototype, we'll use a global instance, which means it only supports one user at a time effectively.
# To support multiple users, we'd need a session ID and a store of InterviewManagers.
interview_managers = {}

class StartRequest(BaseModel):
    role: str
    api_key: str = None

class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"

class EndRequest(BaseModel):
    session_id: str = "default"

@app.post("/start_interview")
async def start_interview(request: StartRequest):
    session_id = "default" # Simple single-session for demo
    
    # If user provides API key, use it. Otherwise rely on env var.
    api_key = request.api_key or os.environ.get("GROQ_API_KEY")
    
    if not api_key:
        raise HTTPException(status_code=400, detail="Groq API Key is required")
        
    try:
        manager = InterviewManager(api_key=api_key)
        response = manager.start_interview(request.role)
        interview_managers[session_id] = manager
        return {"session_id": session_id, "message": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/chat")
async def chat(request: ChatRequest):
    session_id = request.session_id
    if session_id not in interview_managers:
        raise HTTPException(status_code=404, detail="Session not found. Please start an interview first.")
    
    manager = interview_managers[session_id]
    try:
        response = manager.chat(request.message)
        return {"message": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/end_interview")
async def end_interview(request: EndRequest):
    session_id = request.session_id
    if session_id not in interview_managers:
        raise HTTPException(status_code=404, detail="Session not found")
    
    manager = interview_managers[session_id]
    try:
        feedback = manager.end_interview()
        # Clean up
        del interview_managers[session_id]
        return {"feedback": feedback}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Interview Practice Partner API is running"}
