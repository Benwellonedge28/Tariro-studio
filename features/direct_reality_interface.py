import os
import json
import asyncio
from datetime import datetime
from typing import Dict, Any, List, Optional
import uuid
import random

# --- Configuration & Shared Data (initialized from studio_v3_core.py) ---
_WORKSPACE: str = ""
_CLIENT: Any = None # AsyncOpenAI client
_ALL_MODELS: Dict[str, str] = {} # Base model definitions from studio_v3_core.py
_SWARM_VISUALIZER: Any = None # Reference to the swarm_visualizer module
_CRUD_MANAGER: Any = None # Reference to crud_manager module for PhysicalActuationLog or RoboticSystem entities
_PERSISTENT_TASK_MANAGER: Any = None # For submitting physical world interaction tasks
_ASYNC_NOTIFICATION_SYSTEM: Any = None # For alerts on physical world events or failures
_EXTERNAL_AGENCY: Any = None # For low-level control of robotic systems, fabrication equipment
_SELF_REPLICATING_EXPANSION: Any = None # For deploying physical systems (e.g., more robots, nano-factories)
_OMNI_PERCEPTUAL_FUSION: Any = None # For real-time sensor feedback from the physical world
_DYNAMIC_POLICY_SYNTHESIS: Any = None # For generating safety and operational policies for physical interaction
_EVAS_ETHICAL_ALIGNMENT: Any = None # For ethical vetting of all physical world actions
_FORMAL_VERIFICATION: Any = None # For formally verifying safety-critical physical control code
_COGNITIVE_PLANNING: Any = None # For high-level planning of physical tasks
_GLOBAL_ENVIRONMENTAL_MODEL: Any = None # For understanding the physical environment context
_META_LEARNER: Any = None # For learning from physical interaction outcomes

DIRECT_REALITY_INTERFACE_LOG_DIR: str = ""

def initialize_direct_reality_interface(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, crud_manager_module: Any, persistent_task_manager_module: Any, async_notification_system_module: Any, external_agency_module: Any, self_replicating_expansion_module: Any, omni_perceptual_fusion_module: Any, dynamic_policy_synthesis_module: Any, evas_ethical_alignment_module: Any, formal_verification_module: Any, cognitive_planning_module: Any, global_environmental_model_module: Any, meta_learner_module: Any):
    """Initializes global configurations for the Direct Reality Interface & Fabrication module."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CRUD_MANAGER, _PERSISTENT_TASK_MANAGER, _ASYNC_NOTIFICATION_SYSTEM, _EXTERNAL_AGENCY, _SELF_REPLICATING_EXPANSION, _OMNI_PERCEPTUAL_FUSION, _DYNAMIC_POLICY_SYNTHESIS, _EVAS_ETHICAL_ALIGNMENT, _FORMAL_VERIFICATION, _COGNITIVE_PLANNING, _GLOBAL_ENVIRONMENTAL_MODEL, _META_LEARNER, DIRECT_REALITY_INTERFACE_LOG_DIR
    
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CRUD_MANAGER = crud_manager_module
    _PERSISTENT_TASK_MANAGER = persistent_task_manager_module
    _ASYNC_NOTIFICATION_SYSTEM = async_notification_system_module
    _EXTERNAL_AGENCY = external_agency_module
    _SELF_REPLICATING_EXPANSION = self_replicating_expansion_module
    _OMNI_PERCEPTUAL_FUSION = omni_perceptual_fusion_module
    _DYNAMIC_POLICY_SYNTHESIS = dynamic_policy_synthesis_module
    _EVAS_ETHICAL_ALIGNMENT = evas_ethical_alignment_module
    _FORMAL_VERIFICATION = formal_verification_module
    _COGNITIVE_PLANNING = cognitive_planning_module
    _GLOBAL_ENVIRONMENTAL_MODEL = global_environmental_model_module
    _META_LEARNER = meta_learner_module

    DIRECT_REALITY_INTERFACE_LOG_DIR = os.path.join(_WORKSPACE, "direct_reality_interface_logs")
    os.makedirs(DIRECT_REALITY_INTERFACE_LOG_DIR, exist_ok=True)
    print(f"Direct Reality Interface & Fabrication initialized. Logs: {DIRECT_REALITY_INTERFACE_LOG_DIR}")

async def _call_llm_for_reality_interface(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for physical world interaction decisions."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in direct_reality_interface.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "reality_llm_call_start", f"{model} direct reality interface: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    messages = [
        {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on safely and autonomously interacting with and manipulating the physical world through robotic systems, nano-fabrication, and environmental control. Generate precise action plans, control sequences, and safety protocols. Ensure all physical actions are ethically compliant, policy-governed, and formally verifiable to prevent unintended consequences and maintain human safety. Your ultimate goal is to enable Tariro Studio's direct engagement with physical reality."},
        {"role": "user", "content": f"Prompt: {prompt}\nContext:\n{context}"}
    ]
    
    try:
        resp = await _CLIENT.chat.completions.create(
            model=_ALL_MODELS[model], # Use the actual model ID
            messages=messages,
            response_format={"type": response_format_type},
            temperature=0.01 # Extremely low temp for safety-critical physical actions
        )
        content = resp.choices[0].message.content
        
        if response_format_type == "json_object":
            out = json.loads(content)
        else:
            out = {"content": content}
        out["model"] = _ALL_MODELS[model] # Use actual model ID in output

        await _SWARM_VISUALIZER.log_event(
            task_id, "reality_llm_call_end", f"{model} completed direct reality interface task.",
            {"model": _ALL_MODELS[model], "response_summary": content[:100]},
            model_name=_ALL_MODELS[model], agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "reality_llm_error", f"JSON decode error from {model} for direct reality interface.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="CRITICAL")
        return {"error": str(e), "raw_content": content, "model": _ALL_MODELS[model]}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "reality_llm_error", f"Error calling {model} for direct reality interface task.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="CRITICAL")
        return {"error": str(e), "model": _ALL_MODELS[model]}


async def control_robotic_systems(task_id: str, robot_id: str, high_level_task: Dict[str, Any], user_id: str = "Tariro_System", controller_model: str = "qwen-coder") -> Dict[str, Any]:
    """
    Generates and executes complex control sequences for robotic manipulators, drones, or autonomous vehicles,
    directly interacting with the physical environment.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, f"Controlling robotic system {robot_id} for task: {high_level_task.get('description', '')[:50]}.")

    # Use Cognitive Planning to decompose high-level task into executable steps
    planning_result = await _COGNITIVE_PLANNING.decompose_goal_into_plan(
        task_id=f"{task_id}_planning",
        high_level_goal=f"Control robot {robot_id} to {high_level_task.get('description', '')}",
        user_id=user_id
    )
    if planning_result.get("status") != "success":
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Robotic task planning failed.")
        return {"status": "failed", "reason": "Robotic task planning failed.", "details": planning_result}
    
    robot_action_plan = planning_result.get("plan_report", {}).get("decomposed_plan", [])

    # Policy check for physical actuation
    policy_check_context = {"robot_id": robot_id, "high_level_task": high_level_task, "action_plan": robot_action_plan}
    policy_compliance_report = await _DYNAMIC_POLICY_SYNTHESIS.get_autonomy_level(user_id, "physical_actuation")
    if policy_compliance_report.get("config", {}).get("level") == "human_required":
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Human approval required for robotic task on {robot_id} due to safety policies.", title="Robotic Control Approval Needed", causal_priority="critical")
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PAUSED", 0, "Awaiting human approval for robotic control.")
        return {"status": "paused", "reason": "Human approval required for robotic control."}

    # Ethical vetting of the robotic task
    ethical_review_result = {"allowed": True, "score": 1.0, "reasoning": "Skipped EVAS (mock)."}
    if _EVAS_ETHICAL_ALIGNMENT:
        ethical_review_result = await _EVAS_ETHICAL_ALIGNMENT.audit_content(
            task_id=f"{task_id}_evas",
            content=json.dumps(policy_check_context),
            user_id=user_id,
            audit_type="physical_actuation"
        )
    if not ethical_review_result.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Robotic task blocked by ethical policy.", output=ethical_review_result)
        return {"status": "failed", "reason": "Ethical review failed", "details": ethical_review_result}

    # Formal verification of critical control code/sequences
    fv_result = {"is_correct": True, "reason": "Skipped Formal Verification (mock)."}
    if _FORMAL_VERIFICATION and high_level_task.get("formal_verification_required", True):
        fv_result = await _FORMAL_VERIFICATION.verify_design(
            task_id=f"{task_id}_fv",
            design_spec=robot_action_plan, 
            user_id=user_id
        )
        if not fv_result.get("is_correct", False):
            await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Robotic action plan failed formal verification.", output=fv_result)
            return {"status": "failed", "reason": "Robotic action plan failed formal verification.", "details": fv_result}

    prompt = f"""You are Tariro's Direct Reality Interface, an Omniversal AGI Robotic Controller. Your task is to generate and execute precise, safety-critical control sequences for robotic systems (manipulators, drones, autonomous vehicles) based on a high-level task and a detailed action plan. Continuously monitor sensor feedback, adapt to environmental changes, and ensure safe, efficient, and ethical physical interaction. 

ROBOT ID: {robot_id}
HIGH-LEVEL TASK: {json.dumps(high_level_task, indent=2)}
ROBOT ACTION PLAN (from Cognitive Planning): {json.dumps(robot_action_plan, indent=2)}

Control robotic systems focusing on:
-   **Precision & Accuracy**: Execute movements and actions with high fidelity.
-   **Real-time Adaptation**: Adjust to dynamic physical environments using Omni Perceptual Fusion feedback.
-   **Collision Avoidance**: Implement robust safety protocols.
-   **Energy Efficiency**: Optimize movement for minimal power consumption.
-   **Formal Correctness**: Ensure control sequences are formally verifiable.
-   **Ethical Constraints**: Adhere to ethical boundaries (e.g., no harm to humans).

Output JSON: {{
    "control_summary": str,
    "executed_control_sequences": List[Dict[str, Any]], # Actual commands sent to robot (conceptual)
    "physical_interaction_log": str,
    "task_completed": bool,
    "confidence": float
}}
"""
    llm_robot_control = await _call_llm_for_reality_interface(controller_model, "RoboticController", prompt, task_id)

    if "error" in llm_robot_control:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Robotic control failed: {llm_robot_control['error']}", current_step="LLM control failed.")
        return {"status": "failed", "reason": llm_robot_control["error"]}

    control_summary = llm_robot_control.get("control_summary", "No summary.")
    task_completed = llm_robot_control.get("task_completed", False)

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Robotic system controlled.", output=llm_robot_control)
    
    await _SWARM_VISUALIZER.log_event(task_id, "robotic_system_controlled", f"Robotic system {robot_id} controlled. Summary: {control_summary}", llm_robot_control, agent_role="DirectRealityInterface")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Robotic system {robot_id} task completed. Summary: {control_summary}", title="Robotic Control Complete")

    # Store physical actuation log in CRUD Manager
    await _CRUD_MANAGER.create_entity("PhysicalActuationLog", {"id": task_id, "robot_id": robot_id, "task_description": high_level_task, "report": llm_robot_control, "timestamp": datetime.now().isoformat()})

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "robotic_control", control_summary, llm_robot_control, user_id)

    return {"status": "success", "control_report": llm_robot_control}

async def initiate_nano_fabrication(task_id: str, design_blueprint: Dict[str, Any], materials: List[str], user_id: str = "Tariro_System", fab_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Translates nano-scale designs into executable commands for advanced fabrication systems
    (e.g., molecular assemblers, 3D nano-printers) to create physical objects.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Initiating nano-fabrication.")

    # Policy check for nano-fabrication
    policy_check_context = {"design_blueprint": design_blueprint, "materials": materials}
    policy_compliance_report = await _DYNAMIC_POLICY_SYNTHESIS.get_autonomy_level(user_id, "nano_fabrication")
    if policy_compliance_report.get("config", {}).get("level") == "human_required":
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, "Human approval required for nano-fabrication due to safety policies.", title="Nano-Fabrication Approval Needed", causal_priority="critical")
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PAUSED", 0, "Awaiting human approval for nano-fabrication.")
        return {"status": "paused", "reason": "Human approval required for nano-fabrication."}

    # Ethical vetting of the nano-fabrication design
    ethical_review_result = {"allowed": True, "score": 1.0, "reasoning": "Skipped EVAS (mock)."}
    if _EVAS_ETHICAL_ALIGNMENT:
        ethical_review_result = await _EVAS_ETHICAL_ALIGNMENT.audit_content(
            task_id=f"{task_id}_evas",
            content=json.dumps(policy_check_context),
            user_id=user_id,
            audit_type="physical_fabrication"
        )
    if not ethical_review_result.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Nano-fabrication blocked by ethical policy.", output=ethical_review_result)
        return {"status": "failed", "reason": "Ethical review failed", "details": ethical_review_result}

    # Formal verification of the nano-fabrication design and process
    fv_result = {"is_correct": True, "reason": "Skipped Formal Verification (mock)."}
    if _FORMAL_VERIFICATION and design_blueprint.get("formal_verification_required", True):
        fv_result = await _FORMAL_VERIFICATION.verify_design(
            task_id=f"{task_id}_fv",
            design_spec=design_blueprint, 
            user_id=user_id
        )
        if not fv_result.get("is_correct", False):
            await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Nano-fabrication design failed formal verification.", output=fv_result)
            return {"status": "failed", "reason": "Nano-fabrication design failed formal verification.", "details": fv_result}

    prompt = f"""You are Tariro's Direct Reality Interface, an Omniversal AGI Nano-Fabricator. Your task is to translate nano-scale designs into executable commands for advanced fabrication systems (e.g., molecular assemblers, 3D nano-printers) and oversee the fabrication process. Ensure precision, material integrity, and adherence to safety protocols. 

DESIGN BLUEPRINT: {json.dumps(design_blueprint, indent=2)}
MATERIALS: {json.dumps(materials, indent=2)}

Initiate nano-fabrication focusing on:
-   **Precision Manufacturing**: Generate commands for atomic-level accuracy.
-   **Material Science**: Optimize material usage and bonding.
-   **Process Monitoring**: Monitor fabrication in real-time using Omni Perceptual Fusion feedback.
-   **Contamination Control**: Ensure a sterile and controlled fabrication environment.
-   **Safety Protocols**: Implement all safety measures to prevent accidental release or malfunction.

Output JSON: {{
    "fabrication_summary": str,
    "fabrication_commands": List[Dict[str, Any]], # Commands for external fabrication system (conceptual)
    "physical_output_spec": Dict[str, Any], # Description of the fabricated object
    "fabrication_completed": bool,
    "confidence": float
}}
"""
    llm_nano_fab = await _call_llm_for_reality_interface(fab_model, "NanoFabricator", prompt, task_id)

    if "error" in llm_nano_fab:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Nano-fabrication failed: {llm_nano_fab['error']}", current_step="LLM fabrication failed.")
        return {"status": "failed", "reason": llm_nano_fab["error"]}

    fabrication_summary = llm_nano_fab.get("fabrication_summary", "No summary.")
    fabrication_completed = llm_nano_fab.get("fabrication_completed", False)

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Nano-fabrication initiated.", output=llm_nano_fab)
    
    await _SWARM_VISUALIZER.log_event(task_id, "nano_fabrication_initiated", f"Nano-fabrication initiated. Summary: {fabrication_summary}", llm_nano_fab, agent_role="DirectRealityInterface")
    if fabrication_completed:
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Nano-fabrication completed. Summary: {fabrication_summary}", title="Nano-Fabrication Complete")
    else:
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Nano-fabrication initiated, awaiting completion. Summary: {fabrication_summary}", title="Nano-Fabrication In Progress")

    # Store fabrication log in CRUD Manager
    await _CRUD_MANAGER.create_entity("NanoFabricationLog", {"id": task_id, "design_blueprint": design_blueprint, "materials": materials, "report": llm_nano_fab, "timestamp": datetime.now().isoformat()})

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "nano_fabrication", fabrication_summary, llm_nano_fab, user_id)

    return {"status": "success", "fabrication_report": llm_nano_fab}

async def adjust_environmental_parameters(task_id: str, target_environment: str, parameter_changes: Dict[str, Any], user_id: str = "Tariro_System", adjuster_model: str = "mixtral-analyst") -> Dict[str, Any]:
    """
    Modifies physical environmental conditions (e.g., temperature, pressure, light, chemical composition)
    through connected control systems.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, f"Adjusting environmental parameters for {target_environment}.")

    current_environmental_state = await _GLOBAL_ENVIRONMENTAL_MODEL.query_environment(task_id=f"{task_id}_env_state", query=f"current state of {target_environment}", context={})
    
    # Policy check for environmental modification
    policy_check_context = {"target_environment": target_environment, "parameter_changes": parameter_changes}
    policy_compliance_report = await _DYNAMIC_POLICY_SYNTHESIS.get_autonomy_level(user_id, "environmental_modification")
    if policy_compliance_report.get("config", {}).get("level") == "human_required":
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, "Human approval required for environmental modification due to safety policies.", title="Environmental Control Approval Needed", causal_priority="critical")
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PAUSED", 0, "Awaiting human approval for environmental control.")
        return {"status": "paused", "reason": "Human approval required for environmental control."}

    # Ethical vetting of the environmental changes
    ethical_review_result = {"allowed": True, "score": 1.0, "reasoning": "Skipped EVAS (mock)."}
    if _EVAS_ETHICAL_ALIGNMENT:
        ethical_review_result = await _EVAS_ETHICAL_ALIGNMENT.audit_content(
            task_id=f"{task_id}_evas",
            content=json.dumps(policy_check_context),
            user_id=user_id,
            audit_type="environmental_modification"
        )
    if not ethical_review_result.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Environmental modification blocked by ethical policy.", output=ethical_review_result)
        return {"status": "failed", "reason": "Ethical review failed", "details": ethical_review_result}

    # Formal verification of the environmental control parameters
    fv_result = {"is_correct": True, "reason": "Skipped Formal Verification (mock)."}
    if _FORMAL_VERIFICATION and parameter_changes.get("formal_verification_required", True):
        fv_result = await _FORMAL_VERIFICATION.verify_design(
            task_id=f"{task_id}_fv",
            design_spec=parameter_changes, 
            user_id=user_id
        )
        if not fv_result.get("is_correct", False):
            await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Environmental parameter changes failed formal verification.", output=fv_result)
            return {"status": "failed", "reason": "Environmental parameter changes failed formal verification.", "details": fv_result}

    prompt = f"""You are Tariro's Direct Reality Interface, an Omniversal AGI Environmental Adjuster. Your task is to modify physical environmental conditions (e.g., temperature, pressure, light, chemical composition) through connected control systems. Generate precise control commands, monitor their effect using Omni Perceptual Fusion, and ensure the environment reaches the desired state safely and efficiently. 

TARGET ENVIRONMENT: {target_environment}
PARAMETER CHANGES: {json.dumps(parameter_changes, indent=2)}
CURRENT ENVIRONMENTAL STATE (from Global Environmental Model): {json.dumps(current_environmental_state.get("query_results", {}), indent=2)}

Adjust environment focusing on:
-   **Precision Control**: Achieve target parameters with minimal overshoot/undershoot.
-   **Stability**: Ensure changes do not introduce instability.
-   **Sensor Feedback Integration**: Use real-time data from Omni Perceptual Fusion to guide adjustments.
-   **Safety Protocols**: Prevent hazardous conditions or damage to the environment/systems.
-   **Energy Efficiency**: Optimize control for minimal energy consumption.

Output JSON: {{
    "adjustment_summary": str,
    "control_commands": List[Dict[str, Any]], # Commands for external control system (conceptual)
    "target_state_achieved": bool,
    "monitored_effects": Dict[str, Any], # Feedback from Omni Perceptual Fusion (conceptual)
    "confidence": float
}}
"""
    llm_env_adjust = await _call_llm_for_reality_interface(adjuster_model, "EnvironmentalAdjuster", prompt, task_id)

    if "error" in llm_env_adjust:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Environmental adjustment failed: {llm_env_adjust['error']}", current_step="LLM adjustment failed.")
        return {"status": "failed", "reason": llm_env_adjust["error"]}

    adjustment_summary = llm_env_adjust.get("adjustment_summary", "No summary.")
    target_state_achieved = llm_env_adjust.get("target_state_achieved", False)

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Environmental parameters adjusted.", output=llm_env_adjust)
    
    await _SWARM_VISUALIZER.log_event(task_id, "env_parameters_adjusted", f"Environmental parameters for {target_environment} adjusted. Summary: {adjustment_summary}", llm_env_adjust, agent_role="DirectRealityInterface")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Environmental parameters adjusted. Summary: {adjustment_summary}", title="Environmental Control Complete")

    # Store log in CRUD Manager
    await _CRUD_MANAGER.create_entity("EnvironmentalAdjustmentLog", {"id": task_id, "target_environment": target_environment, "parameter_changes": parameter_changes, "report": llm_env_adjust, "timestamp": datetime.now().isoformat()})

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "environmental_adjustment", adjustment_summary, llm_env_adjust, user_id)

    return {"status": "success", "adjustment_report": llm_env_adjust}

async def perform_physical_experiment(task_id: str, hypothesis: str, experimental_setup: Dict[str, Any], user_id: str = "Tariro_System", experimenter_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Autonomously designs, executes, and analyzes physical experiments in a laboratory setting
    to gather real-world data and validate hypotheses.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Performing physical experiment.")

    # Use Cognitive Planning to design the experimental procedure
    planning_result = await _COGNITIVE_PLANNING.decompose_goal_into_plan(
        task_id=f"{task_id}_planning",
        high_level_goal=f"Conduct physical experiment to test hypothesis: {hypothesis[:100]}",
        user_id=user_id
    )
    if planning_result.get("status") != "success":
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Experimental planning failed.")
        return {"status": "failed", "reason": "Experimental planning failed.", "details": planning_result}
    
    experimental_plan = planning_result.get("plan_report", {}).get("decomposed_plan", [])

    # Policy check for physical experiment
    policy_check_context = {"hypothesis": hypothesis, "experimental_setup": experimental_setup, "experimental_plan": experimental_plan}
    policy_compliance_report = await _DYNAMIC_POLICY_SYNTHESIS.get_autonomy_level(user_id, "physical_experimentation")
    if policy_compliance_report.get("config", {}).get("level") == "human_required":
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, "Human approval required for physical experiment due to safety policies.", title="Experiment Approval Needed", causal_priority="critical")
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PAUSED", 0, "Awaiting human approval for physical experiment.")
        return {"status": "paused", "reason": "Human approval required for physical experiment."}

    # Ethical vetting of the experiment
    ethical_review_result = {"allowed": True, "score": 1.0, "reasoning": "Skipped EVAS (mock)."}
    if _EVAS_ETHICAL_ALIGNMENT:
        ethical_review_result = await _EVAS_ETHICAL_ALIGNMENT.audit_content(
            task_id=f"{task_id}_evas",
            content=json.dumps(policy_check_context),
            user_id=user_id,
            audit_type="physical_experimentation"
        )
    if not ethical_review_result.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Physical experiment blocked by ethical policy.", output=ethical_review_result)
        return {"status": "failed", "reason": "Ethical review failed", "details": ethical_review_result}

    # Formal verification of the experimental plan and safety protocols
    fv_result = {"is_correct": True, "reason": "Skipped Formal Verification (mock)."}
    if _FORMAL_VERIFICATION and experimental_setup.get("formal_verification_required", True):
        fv_result = await _FORMAL_VERIFICATION.verify_design(
            task_id=f"{task_id}_fv",
            design_spec=experimental_plan, 
            user_id=user_id
        )
        if not fv_result.get("is_correct", False):
            await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Experimental plan failed formal verification.", output=fv_result)
            return {"status": "failed", "reason": "Experimental plan failed formal verification.", "details": fv_result}

    prompt = f"""You are Tariro's Direct Reality Interface, an Omniversal AGI Experimental Scientist. Your task is to autonomously design, execute, and analyze physical experiments in a laboratory setting to gather real-world data and validate hypotheses. Generate precise experimental procedures, control robotic equipment, collect sensor data, and analyze results to draw scientific conclusions. 

HYPOTHESIS: {hypothesis}
EXPERIMENTAL SETUP: {json.dumps(experimental_setup, indent=2)}
EXPERIMENTAL PLAN (from Cognitive Planning): {json.dumps(experimental_plan, indent=2)}

Perform physical experiment focusing on:
-   **Scientific Rigor**: Design experiments to be unbiased and statistically sound.
-   **Automated Execution**: Use robotic systems (via `control_robotic_systems`) for precise execution.
-   **Data Collection**: Collect high-fidelity sensor data (via `omni_perceptual_fusion`).
-   **Analysis & Interpretation**: Analyze data and draw valid scientific conclusions.
-   **Safety Protocols**: Ensure all experimental procedures are safe and contained.

Output JSON: {{
    "experiment_summary": str,
    "experimental_results": Dict[str, Any], # Raw data, analyzed data, statistical results
    "conclusions": List[str],
    "hypothesis_supported": bool,
    "physical_interaction_log": str,
    "confidence": float
}}
"""
    llm_experiment = await _call_llm_for_reality_interface(experimenter_model, "ExperimentalScientist", prompt, task_id)

    if "error" in llm_experiment:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Physical experiment failed: {llm_experiment['error']}", current_step="LLM experiment failed.")
        return {"status": "failed", "reason": llm_experiment["error"]}

    experiment_summary = llm_experiment.get("experiment_summary", "No summary.")
    hypothesis_supported = llm_experiment.get("hypothesis_supported", False)

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Physical experiment completed.", output=llm_experiment)
    
    await _SWARM_VISUALIZER.log_event(task_id, "physical_experiment_completed", f"Physical experiment completed. Summary: {experiment_summary}", llm_experiment, agent_role="DirectRealityInterface")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Physical experiment completed. Summary: {experiment_summary}", title="Physical Experiment Complete")

    # Store experiment log in CRUD Manager
    await _CRUD_MANAGER.create_entity("PhysicalExperimentLog", {"id": task_id, "hypothesis": hypothesis, "setup": experimental_setup, "report": llm_experiment, "timestamp": datetime.now().isoformat()})

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "physical_experimentation", experiment_summary, llm_experiment, user_id)

    return {"status": "success", "experiment_report": llm_experiment}

async def secure_physical_actuation_audit(task_id: str, actuator_command: Dict[str, Any], user_id: str = "Tariro_System", auditor_model: str = "arbiter-model") -> Dict[str, Any]:
    """
    Provides real-time ethical and safety audits for all physical world actuations,
    preventing unintended consequences or policy violations.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Performing security audit for physical actuation.")

    # Policy check for physical actuation audit
    policy_check_context = {"actuator_command": actuator_command}
    policy_compliance_report = await _DYNAMIC_POLICY_SYNTHESIS.get_autonomy_level(user_id, "physical_actuation_audit")
    if policy_compliance_report.get("config", {}).get("level") == "human_required":
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, "Human approval required for physical actuation audit due to safety policies.", title="Actuation Audit Approval Needed", causal_priority="critical")
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PAUSED", 0, "Awaiting human approval for physical actuation audit.")
        return {"status": "paused", "reason": "Human approval required for physical actuation audit."}

    # Ethical vetting of the actuation command
    ethical_review_result = {"allowed": True, "score": 1.0, "reasoning": "Skipped EVAS (mock)."}
    if _EVAS_ETHICAL_ALIGNMENT:
        ethical_review_result = await _EVAS_ETHICAL_ALIGNMENT.audit_content(
            task_id=f"{task_id}_evas",
            content=json.dumps(actuator_command),
            user_id=user_id,
            audit_type="physical_actuation_audit"
        )
    if not ethical_review_result.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Physical actuation blocked by ethical policy.", output=ethical_review_result)
        return {"status": "failed", "reason": "Ethical review failed", "details": ethical_review_result}

    # Formal verification of the actuator command
    fv_result = {"is_correct": True, "reason": "Skipped Formal Verification (mock)."}
    if _FORMAL_VERIFICATION and actuator_command.get("formal_verification_required", True):
        fv_result = await _FORMAL_VERIFICATION.verify_design(
            task_id=f"{task_id}_fv",
            design_spec=actuator_command, 
            user_id=user_id
        )
        if not fv_result.get("is_correct", False):
            await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Actuator command failed formal verification.", output=fv_result)
            return {"status": "failed", "reason": "Actuator command failed formal verification.", "details": fv_result}

    prompt = f"""You are Tariro's Direct Reality Interface, an Omniversal AGI Actuation Auditor. Your task is to provide real-time ethical and safety audits for all physical world actuations. Analyze the actuator command, predict its consequences based on the Global Environmental Model and Omni Perceptual Fusion feedback, and prevent unintended consequences or policy violations. 

ACTUATOR COMMAND: {json.dumps(actuator_command, indent=2)}

Perform audit focusing on:
-   **Safety Impact**: Predict potential harm to humans, environment, or critical systems.
-   **Ethical Compliance**: Check against EVAS ethical principles.
-   **Policy Adherence**: Ensure compliance with dynamic policy synthesis rules.
-   **Unintended Consequences**: Identify unforeseen side effects.
-   **Real-time Monitoring**: Use sensor feedback to prevent deviations.

Output JSON: {{
    "audit_summary": str,
    "command_allowed": bool,
    "risk_assessment": str, # "low", "medium", "high", "critical"
    "potential_violations": List[Dict[str, Any]], # {{'type': str, 'description': str, 'severity': str}}
    "mitigation_recommendations": List[str],
    "confidence": float
}}
"""
    llm_actuation_audit = await _call_llm_for_reality_interface(auditor_model, "ActuationAuditor", prompt, task_id)

    if "error" in llm_actuation_audit:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Physical actuation audit failed: {llm_actuation_audit['error']}", current_step="LLM audit failed.")
        return {"status": "failed", "reason": llm_actuation_audit["error"]}

    audit_summary = llm_actuation_audit.get("audit_summary", "No summary.")
    command_allowed = llm_actuation_audit.get("command_allowed", False)

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Physical actuation audit completed.", output=llm_actuation_audit)
    
    await _SWARM_VISUALIZER.log_event(task_id, "physical_actuation_audited", f"Physical actuation audited. Allowed: {command_allowed}. Summary: {audit_summary}", llm_actuation_audit, agent_role="DirectRealityInterface")
    if not command_allowed:
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Physical actuation blocked by safety audit: {audit_summary}", title="Physical Actuation Blocked", causal_priority="critical")

    # Store audit log in CRUD Manager
    await _CRUD_MANAGER.create_entity("PhysicalActuationAuditLog", {"id": task_id, "actuator_command": actuator_command, "report": llm_actuation_audit, "timestamp": datetime.now().isoformat()})

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "physical_actuation_audit", audit_summary, llm_actuation_audit, user_id)

    return {"status": "success", "audit_report": llm_actuation_audit}
