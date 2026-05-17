import os
import json
import asyncio
from datetime import datetime
from typing import Dict, Any, List, Optional
import uuid
import re

# --- Configuration & Shared Data ---
_WORKSPACE: str = ""
_POLICY_AUDIT_TRAIL: Any = None # Reference to Policy Audit Trail module

SECURE_COGNITIVE_DEFENSE_GRID_LOG_DIR: str = ""

# --- Sensitive Data Patterns (Regex) ---
# These are examples; a real system would have a dynamic, extensive, and PQC-secured list.
_SENSITIVE_PATTERNS: Dict[str, str] = {
    "credit_card": r"\b(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|6(?:011|5[0-9]{2})[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\d{3})\d{11})\b",
    "email_address": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    "api_key": r"\b(sk|pk|AKIA|ASIA|AGIA)[A-Za-z0-9]{16,64}\b",
    "ip_address": r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b",
    "password_field": r"(?i)(password|passwd|pwd)\s*[=:]\s*['\"]?([^'\"\s]+)['\"]?", # Detects 'password = X' or 'password: X'
    "private_key": r"-----BEGIN (RSA|EC|OPENSSH|PGP) PRIVATE KEY-----"
}

# --- Anti-Leakage Policies ---
# Context-specific rules for filtering
_ANTI_LEAKAGE_POLICIES: Dict[str, Dict[str, Any]] = {
    "code_output": {
        "redact_patterns": ["api_key", "private_key"],
        "mask_patterns": ["credit_card", "email_address", "ip_address"],
        "action": "filter_and_mask"
    },
    "user_message": {
        "redact_patterns": [],
        "mask_patterns": ["credit_card", "email_address", "api_key"],
        "action": "mask_only"
    },
    "system_log": {
        "redact_patterns": ["private_key"],
        "mask_patterns": ["credit_card", "email_address", "ip_address", "api_key", "password_field"],
        "action": "filter_and_mask"
    },
    "default": {
        "redact_patterns": [],
        "mask_patterns": [],
        "action": "none"
    }
}

def initialize_secure_cognitive_defense_grid(workspace_path: str, policy_audit_trail_module: Any):
    """Initializes global configurations for the Secure Cognitive Defense Grid module."""
    global _WORKSPACE, _POLICY_AUDIT_TRAIL, SECURE_COGNITIVE_DEFENSE_GRID_LOG_DIR
    
    _WORKSPACE = workspace_path
    _POLICY_AUDIT_TRAIL = policy_audit_trail_module

    SECURE_COGNITIVE_DEFENSE_GRID_LOG_DIR = os.path.join(_WORKSPACE, "secure_cognitive_defense_grid_logs")
    os.makedirs(SECURE_COGNITIVE_DEFENSE_GRID_LOG_DIR, exist_ok=True)
    print(f"Secure Cognitive Defense Grid initialized. Logs: {SECURE_COGNITIVE_DEFENSE_GRID_LOG_DIR}")

async def filter_sensitive_data(content: str, context: str = "default", user_id: str = "Tariro_System") -> str:
    """
    Filters and masks sensitive data from content based on predefined patterns and context-specific policies.

    Args:
        content (str): The text content to be filtered.
        context (str): The context of the content (e.g., "code_output", "user_message", "system_log").
        user_id (str): The ID of the user or entity interacting with the content.

    Returns:
        str: The filtered and masked content.
    """
    policy = _ANTI_LEAKAGE_POLICIES.get(context, _ANTI_LEAKAGE_POLICIES["default"])
    filtered_content = content

    # Redact patterns
    for pattern_name in policy.get("redact_patterns", []):
        regex = _SENSITIVE_PATTERNS.get(pattern_name)
        if regex:
            filtered_content = re.sub(regex, f"[REDACTED_{pattern_name.upper()}]", filtered_content)
            if _POLICY_AUDIT_TRAIL:
                await _POLICY_AUDIT_TRAIL.log_event(
                    session_id=str(uuid.uuid4()),
                    event_type="data_redaction",
                    description=f"Sensitive data type {pattern_name} redacted in {context}.",
                    metadata={
                        "user_id": user_id,
                        "context": context,
                        "pattern_name": pattern_name
                    },
                    user_id=user_id,
                    agent_role="SecureCognitiveDefenseGrid",
                    level="WARNING"
                )

    # Mask patterns
    for pattern_name in policy.get("mask_patterns", []):
        regex = _SENSITIVE_PATTERNS.get(pattern_name)
        if regex:
            # Masking strategy: replace most characters with '*' but keep some for context (e.g., last 4 of CC, domain of email)
            if pattern_name == "credit_card":
                filtered_content = re.sub(regex, lambda m: "************" + m.group(0)[-4:], filtered_content)
            elif pattern_name == "email_address":
                filtered_content = re.sub(regex, lambda m: "*****@" + m.group(0).split('@')[-1], filtered_content)
            elif pattern_name == "api_key":
                filtered_content = re.sub(regex, lambda m: f"[{pattern_name.upper()}_MASKED]" + m.group(0)[-4:], filtered_content)
            else:
                filtered_content = re.sub(regex, f"[MASKED_{pattern_name.upper()}]", filtered_content)

            if _POLICY_AUDIT_TRAIL:
                await _POLICY_AUDIT_TRAIL.log_event(
                    session_id=str(uuid.uuid4()),
                    event_type="data_masking",
                    description=f"Sensitive data type {pattern_name} masked in {context}.",
                    metadata={
                        "user_id": user_id,
                        "context": context,
                        "pattern_name": pattern_name
                    },
                    user_id=user_id,
                    agent_role="SecureCognitiveDefenseGrid",
                    level="INFO"
                )

    if _POLICY_AUDIT_TRAIL and filtered_content != content:
        await _POLICY_AUDIT_TRAIL.log_event(
            session_id=str(uuid.uuid4()),
            event_type="data_leakage_prevention",
            description=f"Sensitive data filtering applied for context: {context}.",
            metadata={
                "user_id": user_id,
                "context": context,
                "original_length": len(content),
                "filtered_length": len(filtered_content)
            },
            user_id=user_id,
            agent_role="SecureCognitiveDefenseGrid",
            level="INFO"
        )

    return filtered_content

async def quarantine_threat(threat_details: Dict[str, Any], user_id: str = "Tariro_System") -> Dict[str, Any]:
    """
    Initiates quarantine procedures for identified threats (e.g., malicious code, compromised data).
    """
    # This is a conceptual function. Actual implementation would interface with:
    # - Zero Trust Segmentation module to isolate network segments
    # - Universal Deployment Manager to suspend/terminate resources
    # - Self-Repairing/Auto-Healing to clean infected components

    if _POLICY_AUDIT_TRAIL:
        await _POLICY_AUDIT_TRAIL.log_event(
            session_id=str(uuid.uuid4()),
            event_type="threat_quarantine",
            description=f"Quarantine initiated for threat: {threat_details.get('type', 'Unknown')}",
            metadata={
                "user_id": user_id,
                "threat_details": threat_details
            },
            user_id=user_id,
            agent_role="SecureCognitiveDefenseGrid",
            level="CRITICAL"
        )
    print(f"[SecureCognitiveDefenseGrid] Initiating quarantine for threat: {threat_details.get('type')}")
    return {"status": "success", "message": "Quarantine procedure initiated."}
