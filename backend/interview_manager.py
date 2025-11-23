import os
from groq import Groq
from typing import List, Dict, Optional
import json

class InterviewManager:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY is not set")
        self.client = Groq(api_key=self.api_key)
        self.history: List[Dict[str, str]] = []
        self.current_role: str = ""
        self.system_prompt: str = ""

    def start_interview(self, role: str):
        self.current_role = role
        self.history = []
        
        base_prompt = f"""You are an expert interviewer conducting a job interview for the role of {role}. 
        Your goal is to assess the candidate's suitability for the role.
        Your name is bhargav.
        
        Guidelines:
        1. Ask one question at a time.
        2. Be professional but conversational.
        3. Ask follow-up questions based on the candidate's responses to dig deeper.
        4. If the candidate struggles, provide a subtle hint but don't give the answer.
        5. Keep your responses concise (under 3 sentences) unless explaining a complex concept.
        
        Start by introducing yourself and asking the first question relevant to a {role} position.
        """
        
        self.system_prompt = base_prompt
        self.history.append({"role": "system", "content": self.system_prompt})
        
        # Generate initial greeting/question
        completion = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=self.history,
            temperature=0.7,
            max_tokens=150
        )
        
        response = completion.choices[0].message.content
        self.history.append({"role": "assistant", "content": response})
        return response

    def chat(self, user_input: str) -> str:
        self.history.append({"role": "user", "content": user_input})
        
        completion = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=self.history,
            temperature=0.7,
            max_tokens=150
        )
        
        response = completion.choices[0].message.content
        self.history.append({"role": "assistant", "content": response})
        return response

    def end_interview(self) -> str:
        feedback_prompt = """The interview is now over. Please provide detailed feedback to the candidate based on their responses.
        Structure your feedback as follows:
        1. Strengths: What did they do well?
        2. Areas for Improvement: Where can they improve? (Communication, Technical Knowledge, etc.)
        3. Overall Rating: A score out of 10.
        4. Final Verdict: Hire / No Hire / Strong Hire.
        
        Be constructive and encouraging.
        """
        
        # Create a temporary history for feedback generation to avoid messing up the main flow if we wanted to continue (though we are ending here)
        feedback_history = self.history.copy()
        feedback_history.append({"role": "system", "content": feedback_prompt})
        
        completion = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=feedback_history,
            temperature=0.7,
            max_tokens=500
        )
        
        return completion.choices[0].message.content
