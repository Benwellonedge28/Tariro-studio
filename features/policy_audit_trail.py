import os
import json
import hashlib
import time
import logging
from typing import Dict, Any, Optional

logger = logging.getLogger("PolicyAuditTrail")

# Global constant, assumed to be set by the main studio_v3.py
WORKSPACE = os.getenv("WORKSPACE", "/app/workspace")
AUDIT_LOG_FILE = os.path.join(WORKSPACE, "policy_audit_trail.log")
MERKLE_ROOT_FILE = os.path.join(WORKSPACE, "merkle_root.json")

async def log_change(
    task_id: str,
    event_type: str,
    old_value: Optional[Any],
    new_value: Any,
    actor: str,
    description: str,
    metadata: Optional[Dict[str, Any]] = None,
) -> None:
    """Logs a system change to an append-only, tamper-evident audit trail."""
    timestamp = int(time.time())
    log_entry = {
        "timestamp": timestamp,
        "task_id": task_id,
        "event_type": event_type,
        "old_value": old_value,
        "new_value": new_value,
        "actor": actor,
        "description": description,
        "metadata": metadata or {},
    }
    log_json = json.dumps(log_entry, sort_keys=True)
    entry_hash = hashlib.sha256(log_json.encode('utf-8')).hexdigest()

    # Read previous Merkle root for chaining
    previous_root = "0" * 64 # Default for first entry
    try:
        with open(MERKLE_ROOT_FILE, 'r') as f:
            data = json.load(f)
            previous_root = data.get("merkle_root", previous_root)
    except (FileNotFoundError, json.JSONDecodeError):
        pass # Root will be default or created

    # Calculate new Merkle root (simple chain hash for this implementation)
    # In a full Merkle tree, this would be more complex, hashing pairs of entries.
    current_root = hashlib.sha256(f"{previous_root}{entry_hash}".encode('utf-8')).hexdigest()
    log_entry["entry_hash"] = entry_hash
    log_entry["previous_root"] = previous_root
    log_entry["current_root"] = current_root

    # Append to log file
    try:
        with open(AUDIT_LOG_FILE, 'a') as f:
            f.write(json.dumps(log_entry) + '\n')
        # Update Merkle root file
        with open(MERKLE_ROOT_FILE, 'w') as f:
            json.dump({"merkle_root": current_root, "last_entry_hash": entry_hash}, f)
        logger.info(f"Audit: {event_type} by {actor} (Root: {current_root[:8]}...)")
    except Exception as e:
        logger.error(f"Failed to write to audit log or update Merkle root: {e}")

async def verify_audit_trail() -> Tuple[bool, str]:
    """Verifies the integrity of the audit trail using Merkle root chaining."""
    logger.info("Verifying audit trail integrity...")
    try:
        with open(AUDIT_LOG_FILE, 'r') as f:
            lines = f.readlines()

        if not lines: # Empty log is valid
            return True, "Audit trail is empty and valid."

        calculated_merkle_root = "0" * 64
        for i, line in enumerate(lines):
            entry = json.loads(line)
            entry_hash = entry.pop("entry_hash") # Remove this before recalculating hash
            previous_root_in_entry = entry.pop("previous_root")
            current_root_in_entry = entry.pop("current_root")
            
            recalculated_entry_hash = hashlib.sha256(json.dumps(entry, sort_keys=True).encode('utf-8')).hexdigest()
            
            if recalculated_entry_hash != entry_hash:
                return False, f"Integrity FAIL: Entry {i} hash mismatch. Expected {entry_hash}, got {recalculated_entry_hash}."
            
            # Verify chaining
            if i == 0:
                if previous_root_in_entry != "0" * 64: # First entry's previous root must be default
                    return False, f"Integrity FAIL: First entry's previous_root is not default. ({previous_root_in_entry})"
            else:
                # Use the current_root from the PREVIOUS entry to check current entry's previous_root
                prev_entry = json.loads(lines[i-1])
                if prev_entry["current_root"] != previous_root_in_entry:
                    return False, f"Integrity FAIL: Entry {i} chain broken. Previous entry root {prev_entry["current_root"]} != entry's previous_root {previous_root_in_entry}."
            
            # Update for next iteration's chaining check
            calculated_merkle_root = current_root_in_entry
        
        # Finally, check the last written root against the final calculated one
        with open(MERKLE_ROOT_FILE, 'r') as f:
            final_root_data = json.load(f)
            stored_merkle_root = final_root_data.get("merkle_root")
            if stored_merkle_root != calculated_merkle_root:
                return False, f"Integrity FAIL: Final stored Merkle root mismatch. Expected {calculated_merkle_root}, got {stored_merkle_root}."

        logger.info("Audit trail integrity verified successfully.")
        return True, "Audit trail integrity verified successfully."
    except (FileNotFoundError, json.JSONDecodeError) as e:
        return False, f"Error verifying audit trail: {e}"
    except Exception as e:
        logger.error(f"An unexpected error occurred during audit trail verification: {e}")
        return False, f"An unexpected error occurred: {e}"

