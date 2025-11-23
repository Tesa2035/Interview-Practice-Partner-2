const API_URL = 'http://localhost:8000';
let currentSessionId = null;
let isRecording = false;
let recognition = null;

// Initialize Speech Recognition
if ('webkitSpeechRecognition' in window) {
    recognition = new webkitSpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = true;
    recognition.lang = 'en-US';

    let silenceTimer = null;

    recognition.onstart = () => {
        isRecording = true;
        document.getElementById('record-btn').classList.add('recording');
        document.getElementById('user-input').value = ''; // Clear input on start
    };

    recognition.onend = () => {
        isRecording = false;
        document.getElementById('record-btn').classList.remove('recording');
        clearTimeout(silenceTimer);
    };

    recognition.onresult = (event) => {
        let finalTranscript = '';
        let interimTranscript = '';

        for (let i = event.resultIndex; i < event.results.length; ++i) {
            if (event.results[i].isFinal) {
                finalTranscript += event.results[i][0].transcript;
            } else {
                interimTranscript += event.results[i][0].transcript;
            }
        }

        // For continuous, we want to show the full accumulated text of this session
        let fullTranscript = '';
        for (let i = 0; i < event.results.length; ++i) {
            fullTranscript += event.results[i][0].transcript;
        }

        document.getElementById('user-input').value = fullTranscript;

        // Reset silence timer
        clearTimeout(silenceTimer);
        silenceTimer = setTimeout(() => {
            recognition.stop();
            sendMessage();
        }, 2000); // Wait for 2 seconds of silence
    };
} else {
    alert('Web Speech API is not supported in this browser. Voice features will be disabled.');
    document.getElementById('record-btn').style.display = 'none';
}

function toggleRecording() {
    if (isRecording) {
        recognition.stop();
    } else {
        recognition.start();
    }
}

async function selectRole(role) {
    try {
        const response = await fetch(`${API_URL}/start_interview`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ role: role }),
        });

        if (!response.ok) {
            const error = await response.json();
            alert(error.detail || 'Failed to start interview');
            return;
        }

        const data = await response.json();
        currentSessionId = data.session_id;

        // Switch UI
        document.getElementById('landing-page').classList.add('hidden');
        document.getElementById('interview-page').classList.remove('hidden');
        document.getElementById('role-title').innerText = `${role} Interview`;

        addMessage('assistant', data.message);
        speak(data.message);

    } catch (error) {
        console.error('Error:', error);
        alert('Failed to connect to the server. Make sure the backend is running.');
    }
}

async function sendMessage() {
    const input = document.getElementById('user-input');
    const message = input.value.trim();

    if (!message) return;

    addMessage('user', message);
    input.value = '';

    try {
        const response = await fetch(`${API_URL}/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                message: message,
                session_id: currentSessionId
            }),
        });

        const data = await response.json();
        addMessage('assistant', data.message);
        speak(data.message);

    } catch (error) {
        console.error('Error:', error);
        addMessage('system', 'Error sending message. Please try again.');
    }
}

async function endInterview() {
    try {
        const response = await fetch(`${API_URL}/end_interview`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ session_id: currentSessionId }),
        });

        const data = await response.json();

        document.getElementById('interview-page').classList.add('hidden');
        document.getElementById('feedback-page').classList.remove('hidden');
        document.getElementById('feedback-content').innerText = data.feedback;

    } catch (error) {
        console.error('Error:', error);
        alert('Failed to end interview.');
    }
}

function addMessage(role, text) {
    const container = document.getElementById('chat-container');
    const div = document.createElement('div');
    div.className = `message ${role}`;
    div.innerText = text;
    container.appendChild(div);
    container.scrollTop = container.scrollHeight;
}

function handleKeyPress(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
}

function speak(text) {
    if ('speechSynthesis' in window) {
        // Cancel any ongoing speech
        window.speechSynthesis.cancel();

        const utterance = new SpeechSynthesisUtterance(text);
        utterance.rate = 1.0;
        utterance.pitch = 1.0;
        window.speechSynthesis.speak(utterance);
    }
}
