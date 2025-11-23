🧠 Project Overview

The AI Interview Practice Partner is an intelligent conversational agent designed to help users prepare for job interviews across different domains (Software Engineering, Sales, Retail, etc.).
The assistant simulates a real interviewer, asks multi-turn follow-up questions, evaluates user responses, provides feedback, and adapts to multiple user personas.

This project is designed to demonstrate:

Conversational Quality

Agentic Behaviour

Intelligence & Adaptability

Robust technical implementation using modern LLM frameworks

The system supports Voice Interaction (preferred) and Chat Mode, making it suitable for both desktop and mobile interfaces.

🚀 Key Features



✅ 1. Mock Interview Simulation

Domain-specific interview flows (e.g., Software Developer, SDE1, Retail Associate, Sales Executive).

Dynamic follow-up questions based on user answers.

✅ 2. AI-Powered Feedback System

Communication analysis

Technical correctness

Confidence & clarity scoring

Improvement suggestions

✅ 3. Multi-Persona Handling

The agent is trained to handle:

Persona Type	Description
Confused User	Unsure what job or mode to choose
Efficient User	Wants very fast answers, no fluff
Chatty User	Talks about unrelated topics
Edge-case User	Gives invalid inputs, asks impossible or irrelevant questions
✅ 4. Voice Interaction

Speech-to-Text (Whisper API / Web Speech API)

Text-to-Speech (OpenAI Realtime API / Web Speech API)

✅ 5. Fully Modular Architecture

Easy to extend question banks

Plug-and-play model interface

Works with any LLM: OpenAI, Gemini, Llama, local models, etc.

🏛️ System Architecture
User
 ├── Voice Input / Text Chat
 ├── Frontend UI (React / Next.js / HTML)
 └── Backend API
        │
        ├── STT Module (Whisper or browser STT)
        ├── LLM Interaction Layer
        │     ├── Prompt Controller
        │     ├── Persona Handler
        │     ├── Follow-Up Engine
        │     └── Feedback Evaluator
        ├── State Manager (Redis or in-memory)
        └── Logs & Analytics

⚙️ Tech Stack
Frontend

React.js / Next.js

Tailwind CSS

Web Speech API (for browser voice input/output)

Axios for API calls

Backend

Node.js / Express

OpenAI Realtime API or standard Chat Completion API

Whisper for Speech-to-Text

JWT for secure sessions

Redis (optional) for managing conversation state

WebSocket support for streaming responses

LLM

OpenAI GPT-4.1 / GPT-5.1 (or any other provider)

Finetuned system prompts for:

Persona handling

Interview mode switching

Follow-up reasoning

Feedback analysis

🧩 Core Functional Modules
1️⃣ Interview Question Generator

Generates structured interview rounds:

HR round

Technical round

Behavioural round

Role-specific situations

Uses few-shot and chain-of-thought prompting.

2️⃣ Follow-up Question Engine

After each user message:

Evaluate answer

Identify gaps

Generate natural follow-up questions

Example:

User: “I have experience in Java.”

Agent:

"Great! Can you describe a recent Java project where you solved a difficult problem?"

3️⃣ Response Evaluation Module

Evaluates:

Technical Accuracy

Communication

Delivery & Structure

Real-world Relevance

STAR Format Compliance

Provides a score & improvement plan.

4️⃣ Persona Handler

Handles different behaviours through a state classifier:

Persona	How the Agent Responds
Confused	Asks clarifying questions, suggests roles
Efficient	Short, crisp questions
Chatty	Gently brings back to topic
Edge Case	Gracefully declines or redirects
5️⃣ Voice Interaction
Speech-to-text

Whisper API

Browser STT fallback

Text-to-speech

OpenAI Audio API

Browser TTS fallback

🧪 Testing Strategy
Test with multiple personas

Confused User Scenario

User: “I don’t know which job role to select.”

Agent: “No problem! What field are you most comfortable with—tech, retail, or sales?”

Efficient User Scenario

User: “Start technical round immediately.”

Agent: “Sure. Question 1: Explain multithreading.”

Chatty User Scenario

User: “Did you watch the India match yesterday?”

Agent: “That sounds exciting! For now, let’s return to your interview prep…”

Edge Case User

User: “Write a 1000-line code inside this chat.”

Agent: “I can provide a high-level solution but not a full production application.”

📂 Project Structure
/project-root
│── README.md
│── /frontend
│     ├── index.html
│     ├── App.jsx
│     └── interview-ui/
│
│── /backend
│     ├── server.js
│     ├── routes/
│     ├── controllers/
│     ├── utils/
│     └── prompts/
│
│── /models
│     ├── interviewFlows.json
│     └── personaLogic.js

🔧 Setup Instructions
1. Clone Repo
git clone https://github.com/yourusername/interview-agent.git
cd interview-agent

2. Install Dependencies

Backend

cd backend
npm install


Frontend

cd frontend
npm install

3. Environment Variables

Create .env:

OPENAI_API_KEY=your_key
PORT=5000

4. Start Servers

Backend:

npm start


Frontend:

npm run dev

🎥 Demo Video Guidelines (for submission)

Your 10-minute demo must include:

✔️ Show the agent handling these scenarios:

Confused User

Efficient User

Chatty User

Edge-case User

✔️ Demonstrate:

Voice input/output

Technical & HR rounds

Follow-up question generation

Evaluation & feedback module

Persona detection

✔️ Include architecture explanation:

High-level diagram

Why you chose OpenAI / LLM-based reasoning

Importance of state management

Error handling

❌ No slides
❌ Only screen + voiceover
🧠 Design Decisions & Reasoning (For Evaluation Panel)
1. LLM instead of rule-based

Rule-based trees fail with messy user behaviour.
LLM provides:

Dynamic follow-ups

Persona detection

Natural conversation flow

2. Prompt Engineering

System prompt locks behaviour

Few-shot examples for each persona

Dynamic memory improves context retention

3. State Management

Needed because:

Interviews are multi-round

Follow-up questions depend on past answers

Persona must persist across turns

4. Voice Preferred

Matches real interview environment.

5. Modularity First

Easily add more roles

Swap or upgrade LLM with minimal code changes

📈 Future Improvements

Resume Parsing

ATS-based scoring

Custom interview training plans

Local model support (Llama3, Phi-3)

Multi-language interviews

🎯 Conclusion

This project showcases a complete end-to-end intelligent interview agent with:

Deep conversational reasoning

Real-world interview simulation

Multi-persona adaptability

Strong architecture and modularity

Voice-enabled natural interaction

Perfect for portfolio, hiring challenges, and GitHub demonstration.
