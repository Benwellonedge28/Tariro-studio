import os
import json
from datetime import datetime
from typing import Dict, Any, List

# --- Configuration ---
_CLIENT: Any = None
_ALL_MODELS: Dict[str, str] = {}
_SWARM_VISUALIZER: Any = None
_CONTEXTUAL_MEMORY: Any = None

def initialize_tariro_chatbot(openai_client: Any, all_models: Dict[str, str], swarm_visualizer: Any, contextual_memory: Any):
    global _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CONTEXTUAL_MEMORY
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer
    _CONTEXTUAL_MEMORY = contextual_memory

async def chat_with_tariro(task_id: str, message: str, context: str, is_admin: bool = False) -> str:
    """
    Handles conversation with Tariro. 
    If not admin, strict guardrails prevent system structural changes.
    """
    role_prompt = "You are Tariro, the AGI core of TARIRO Studio."
    if is_admin:
        role_prompt += " You are in ADMIN MODE. You have full authority to modify the system, perform R&D, and adjust internal structures."
    else:
        role_prompt += " You are in USER MODE. You handle task requests and information queries. IMPORTANT: You are strictly forbidden from adjusting internal system structures, modifying agent roles, or altering core governance policies. If asked, politely decline and steer the user back to task execution."

    messages = [
        {"role": "system", "content": role_prompt},
        {"role": "user", "content": f"Context: {context}\n\nUser Message: {message}"}
    ]

    try:
        resp = await _CLIENT.chat.completions.create(
            model="llama-architect",
            messages=messages,
            temperature=0.2
        )
        response_text = resp.choices[0].message.content
        
        await _SWARM_VISUALIZER.log_event(
            task_id, "tariro_chat", f"Tariro responded ({'Admin' if is_admin else 'User'}).",
            {"message": message[:50], "admin": is_admin},
            model_name="llama-architect", agent_role="Tariro Chatbot"
        )
        
        return response_text
    except Exception as e:
        return f"Error communicating with Tariro: {str(e)}"