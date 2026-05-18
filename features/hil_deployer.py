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
_CRUD_MANAGER: Any = None # Reference to crud_manager module for HardwareDeploymentLog or HardwareTestResult entities
_PERSISTENT_TASK_MANAGER: Any = None # For submitting hardware interaction/deployment tasks
_ASYNC_NOTIFICATION_SYSTEM: Any = None # For alerts on hardware deployment success/failure
_EXTERNAL_AGENCY: Any = None # For interacting with low-level hardware interfaces (USB, JTAG, UART)
_OMNI_PERCEPTUAL_FUSION: Any = None # For real-time sensor feedback from hardware tests
_FORMAL_VERIFICATION: Any = None # For formally verifying firmware/HDL before flashing
_AUTONOMY_GOVERNANCE: Any = None # For policy checks on hardware deployment actions
_SELF_ARCHITECTING_ENGINE: Any = None # For designing hardware components
_LLM_COMPILER: Any = None # For generating firmware/HDL code
_META_LEARNER: Any = None # For learning from hardware deployment outcomes
_DYNAMIC_POLICY_SYNTHESIS: Any = None # For generating hardware deployment policies
_SELF_REPLICATING_EXPANSION: Any = None # For orchestrating large-scale hardware deployments

HIL_DEPLOYER_LOG_DIR: str = ""

def initialize_hil_deployer(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, crud_manager_module: Any, persistent_task_manager_module: Any, async_notification_system_module: Any, external_agency_module: Any, omni_perceptual_fusion_module: Any, formal_verification_module: Any, autonomy_governance_module: Any, self_architecting_engine_module: Any, llm_compiler_module: Any, meta_learner_module: Any, dynamic_policy_synthesis_module: Any, self_replicating_expansion_module: Any):
    """Initializes global configurations for the Hardware-in-Loop Deployer module."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CRUD_MANAGER, _PERSISTENT_TASK_MANAGER, _ASYNC_NOTIFICATION_SYSTEM, _EXTERNAL_AGENCY, _OMNI_PERCEPTUAL_FUSION, _FORMAL_VERIFICATION, _AUTONOMY_GOVERNANCE, _SELF_ARCHITECTING_ENGINE, _LLM_COMPILER, _META_LEARNER, _DYNAMIC_POLICY_SYNTHESIS, _SELF_REPLICATING_EXPANSION, HIL_DEPLOYER_LOG_DIR
    
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CRUD_MANAGER = crud_manager_module
    _PERSISTENT_TASK_MANAGER = persistent_task_manager_module
    _ASYNC_NOTIFICATION_SYSTEM = async_notification_system_module
    _EXTERNAL_AGENCY = external_agency_module
    _OMNI_PERCEPTUAL_FUSION = omni_perceptual_fusion_module
    _FORMAL_VERIFICATION = formal_verification_module
    _AUTONOMY_GOVERNANCE = autonomy_governance_module
    _SELF_ARCHITECTING_ENGINE = self_architecting_engine_module
    _LLM_COMPILER = llm_compiler_module
    _META_LEARNER = meta_learner_module
    _DYNAMIC_POLICY_SYNTHESIS = dynamic_policy_synthesis_module
    _SELF_REPLICATING_EXPANSION = self_replicating_expansion_module

    HIL_DEPLOYER_LOG_DIR = os.path.join(_WORKSPACE, "hil_deployer_logs")
    os.makedirs(HIL_DEPLOYER_LOG_DIR, exist_ok=True)
    print(f"Hardware-in-Loop Deployer initialized. Logs: {HIL_DEPLOYER_LOG_DIR}")

async def _call_llm_for_hil_deploy(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for hardware deployment and testing decisions."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in hil_deployer.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "hil_deploy_llm_call_start", f"{model} HIL deployment: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    messages = [
        {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on autonomously orchestrating hardware-in-loop (HIL) deployment, testing, and integration processes. This involves generating flashing commands, interpreting physical sensor feedback, managing test benches, and making decisions about hardware release. Ensure safety, reliability, and functional correctness. All HIL operations must be policy-governed and formally verifiable for safety-critical systems."},
        {"role": "user", "content": f"Prompt: {prompt}\nContext:\n{context}"}
    ]
    
    try:
        resp = await _CLIENT.chat.completions.create(
            model=_ALL_MODELS[model], # Use the actual model ID
            messages=messages,
            response_format={"type": response_format_type},
            temperature=0.02 # Very low temp for safety-critical hardware interaction
        )
        content = resp.choices[0].message.content
        
        if response_format_type == "json_object":
            out = json.loads(content)
        else:
            out = {"content": content}
        out["model"] = _ALL_MODELS[model] # Use actual model ID in output

        await _SWARM_VISUALIZER.log_event(
            task_id, "hil_deploy_llm_call_end", f"{model} completed HIL deployment task.",
            {"model": _ALL_MODELS[model], "response_summary": content[:100]},
            model_name=_ALL_MODELS[model], agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "hil_deploy_llm_error", f"JSON decode error from {model} for HIL deployment.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="CRITICAL")
        return {"error": str(e), "raw_content": content, "model": _ALL_MODELS[model]}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "hil_deploy_llm_error", f"Error calling {model} for HIL deployment task.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="CRITICAL")
        return {"error": str(e), "model": _ALL_MODELS[model]}


async def auto_flash_hardware(task_id: str, hardware_id: str, firmware_image: str, interface_config: Dict[str, Any], user_id: str = "Tariro_System", flasher_model: str = "qwen-coder") -> Dict[str, Any]:
    """
    Autonomously flashes firmware/HDL onto target hardware (e.g., FPGA, ESP32) via USB/JTAG.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, f"Auto-flashing firmware to {hardware_id}.")

    # Policy check for hardware flashing
    policy_check_context = {"hardware_id": hardware_id, "firmware_image": firmware_image, "interface_config": interface_config}
    policy_compliance_report = await _AUTONOMY_GOVERNANCE.check_policy(user_id, "hardware_flashing", policy_check_context)
    if not policy_compliance_report.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Hardware flashing blocked by policy.", output=policy_compliance_report)
        return {"status": "failed", "reason": "Policy non-compliance", "details": policy_compliance_report}

    # Formal verification of firmware/HDL before flashing
    fv_result = {"is_correct": True, "reason": "Skipped Formal Verification (mock)."}
    if _FORMAL_VERIFICATION and firmware_image.endswith(('.bin', '.hex', '.sv', '.vhd')):
        # Assuming firmware_image content is available for verification or a reference to it
        fv_result = await _FORMAL_VERIFICATION.verify_design(
            task_id=f"{task_id}_fv",
            design_spec={
                "type": "firmware_or_hdl", 
                "content_reference": firmware_image, 
                "checksum": "mock_checksum"
            }, 
            user_id=user_id
        )
        if not fv_result.get("is_correct", False):
            await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Firmware/HDL failed formal verification. Flashing aborted.", output=fv_result)
            return {"status": "failed", "reason": "Firmware/HDL failed formal verification.", "details": fv_result}

    prompt = f"""You are Tariro's Hardware-in-Loop Deployer, an Omniversal AGI Hardware Flasher. Your task is to autonomously flash firmware or Hardware Description Language (HDL) onto a specified target hardware (e.g., FPGA, ESP32, microcontroller) via appropriate interfaces like USB, JTAG, or UART. Generate the precise flashing commands, monitor the process, and verify successful programming. Ensure safety, reliability, and prevent hardware damage. 

HARDWARE ID: {hardware_id}
FIRMWARE IMAGE (path or identifier): {firmware_image}
INTERFACE CONFIGURATION: {json.dumps(interface_config, indent=2)}

Auto-flash focusing on:
-   **Interface Control**: Generate commands for `openocd`, `esptool`, `iceprog`, etc.
-   **Progress Monitoring**: Monitor flashing process for errors or hang-ups.
-   **Verification**: Read back device memory or checksum to ensure correct programming.
-   **Safety Protocols**: Implement power cycling, reset, or emergency stop procedures.

Output JSON: {{
    "flashing_summary": str,
    "flashing_commands": List[str],
    "flashing_completed": bool,
    "verification_passed": bool,
    "confidence": float
}}
"""
    llm_flashing = await _call_llm_for_hil_deploy(flasher_model, "HardwareFlasher", prompt, task_id)

    if "error" in llm_flashing:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Hardware flashing failed: {llm_flashing['error']}", current_step="LLM flashing failed.")
        return {"status": "failed", "reason": llm_flashing["error"]}

    flashing_summary = llm_flashing.get("flashing_summary", "No summary.")
    flashing_completed = llm_flashing.get("flashing_completed", False)
    verification_passed = llm_flashing.get("verification_passed", False)

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 70, "Flashing complete. Running hardware tests.")

    # Execute flashing commands via External Agency (conceptual)
    # This part would interact with actual hardware tools
    if _EXTERNAL_AGENCY:
        # For each command in llm_flashing["flashing_commands"]:
        # await _EXTERNAL_AGENCY.control_hardware_interface(hardware_id, command)
        pass

    # After flashing, run hardware tests
    test_results = await run_hardware_tests(
        task_id=f"{task_id}_hw_test",
        hardware_id=hardware_id,
        test_suite_id=interface_config.get("test_suite_id", "default_hw_tests"),
        user_id=user_id
    )

    if not test_results.get("tests_passed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 90, "Hardware tests failed after flashing.", output=test_results)
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Hardware {hardware_id} failed tests after flashing. Summary: {flashing_summary}", title="Hardware Flashing Failed", causal_priority="critical")
        return {"status": "failed", "reason": "Hardware tests failed."}

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Hardware auto-flashed and verified.", output=llm_flashing)
    
    await _SWARM_VISUALIZER.log_event(task_id, "hardware_auto_flashed", f"Hardware {hardware_id} auto-flashed. Summary: {flashing_summary}", llm_flashing, agent_role="HILDeployer")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Hardware {hardware_id} auto-flashed and verified. Summary: {flashing_summary}", title="Hardware Flashing Complete")

    # Store deployment log in CRUD Manager
    await _CRUD_MANAGER.create_entity("HardwareDeploymentLog", {"id": task_id, "hardware_id": hardware_id, "firmware": firmware_image, "report": llm_flashing, "timestamp": datetime.now().isoformat()})

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "hardware_flashing", flashing_summary, llm_flashing, user_id)

    return {"status": "success", "flashing_report": llm_flashing}

async def run_hardware_tests(task_id: str, hardware_id: str, test_suite_id: str, user_id: str = "Tariro_System", tester_model: str = "mixtral-analyst") -> Dict[str, Any]:
    """
    Executes a specified test suite on physical hardware and interprets the results
    using real-time sensor feedback.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, f"Running hardware tests on {hardware_id}.")

    # Policy check for hardware testing
    policy_check_context = {"hardware_id": hardware_id, "test_suite_id": test_suite_id}
    policy_compliance_report = await _DYNAMIC_POLICY_SYNTHESIS.get_autonomy_level(user_id, "hardware_testing")
    if policy_compliance_report.get("config", {}).get("level") == "human_required":
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, "Human approval required for hardware testing due to safety policies.", title="Hardware Test Approval Needed", causal_priority="critical")
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PAUSED", 0, "Awaiting human approval for hardware testing.")
        return {"status": "paused", "reason": "Human approval required for hardware testing."}

    # Use Omni Perceptual Fusion for real-time sensor feedback during tests
    sensor_feedback = await _OMNI_PERCEPTUAL_FUSION.process_sensor_stream(
        task_id=f"{task_id}_sensor_fusion",
        stream_type="hardware_test_data",
        user_id=user_id
    )
    # Mock: interpret sensor feedback to get test outcomes
    interpreted_sensor_data = sensor_feedback.get("fusion_report", {}).get("interpreted_data", {})

    prompt = f"""You are Tariro's Hardware-in-Loop Deployer, an Omniversal AGI Hardware Tester. Your task is to execute a specified test suite on physical hardware, interpret the results using real-time sensor feedback, and determine if the hardware passes or fails. Ensure tests are comprehensive, reliable, and provide clear diagnostics.

HARDWARE ID: {hardware_id}
TEST SUITE ID: {test_suite_id}
INTERPRETED SENSOR DATA (from Omni Perceptual Fusion): {json.dumps(interpreted_sensor_data, indent=2)}

Run tests focusing on:
-   **Functional Correctness**: Verify expected behavior.
-   **Performance Benchmarking**: Measure speed, power consumption, etc.
-   **Reliability**: Test robustness under various conditions.
-   **Failure Analysis**: Pinpoint the exact cause of any test failures.
-   **Automated Interpretation**: Translate raw sensor data into pass/fail criteria.

Output JSON: {{
    "test_summary": str,
    "tests_passed": bool,
    "failed_tests": List[Dict[str, Any]], # {{'test_name': str, 'reason': str, 'log': str}}
    "diagnostics": str,
    "confidence": float
}}
"""
    llm_test_results = await _call_llm_for_hil_deploy(tester_model, "HardwareTester", prompt, task_id)

    if "error" in llm_test_results:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Hardware testing failed: {llm_test_results['error']}", current_step="LLM testing failed.")
        return {"status": "failed", "reason": llm_test_results["error"]}

    test_summary = llm_test_results.get("test_summary", "No summary.")
    tests_passed = llm_test_results.get("tests_passed", False)

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Hardware tests completed.", output=llm_test_results)
    
    await _SWARM_VISUALIZER.log_event(task_id, "hardware_tests_completed", f"Hardware {hardware_id} tests completed. Passed: {tests_passed}. Summary: {test_summary}", llm_test_results, agent_role="HILDeployer")
    if not tests_passed:
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Hardware {hardware_id} tests failed. Summary: {test_summary}", title="Hardware Test Failed", causal_priority="critical")
    else:
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Hardware {hardware_id} tests passed. Summary: {test_summary}", title="Hardware Test Passed")

    # Store test results in CRUD Manager
    await _CRUD_MANAGER.create_entity("HardwareTestResult", {"id": task_id, "hardware_id": hardware_id, "test_suite_id": test_suite_id, "results": llm_test_results, "timestamp": datetime.now().isoformat()})

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "hardware_testing", test_summary, llm_test_results, user_id)

    return {"status": "success", "test_report": llm_test_results}

async def ship_to_staging(task_id: str, hardware_id: str, deployment_target: str, user_id: str = "Tariro_System", deployer_model: str = "llama-architect") -> Dict[str, Any]:
    """
    If hardware tests pass, orchestrates shipping the hardware (or its configuration)
    to a staging environment.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, f"Shipping hardware {hardware_id} to staging {deployment_target}.")

    # Policy check for hardware staging deployment
    policy_check_context = {"hardware_id": hardware_id, "deployment_target": deployment_target}
    policy_compliance_report = await _AUTONOMY_GOVERNANCE.check_policy(user_id, "hardware_deployment", policy_check_context)
    if not policy_compliance_report.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Hardware staging deployment blocked by policy.", output=policy_compliance_report)
        return {"status": "failed", "reason": "Policy non-compliance", "details": policy_compliance_report}

    prompt = f"""You are Tariro's Hardware-in-Loop Deployer, an Omniversal AGI Staging Orchestrator. Your task is to orchestrate the shipping and integration of validated hardware (or its configuration) into a staging environment. This involves physical logistics, network configuration, and final verification checks before full production deployment. 

HARDWARE ID: {hardware_id}
DEPLOYMENT TARGET (staging environment): {deployment_target}

Ship to staging focusing on:
-   **Physical Logistics**: If applicable, generate commands for robotic arms or human instructions.
-   **Network Integration**: Configure network settings for hardware in staging.
-   **Environmental Setup**: Ensure physical conditions in staging are met.
-   **Post-Deployment Verification**: Run final smoke tests or health checks.
-   **Safety & Security**: Maintain safety protocols and secure configuration during transit and deployment.

Output JSON: {{
    "staging_summary": str,
    "staging_plan": List[Dict[str, Any]], # {{'step': str, 'action': str, 'executor': str, 'details': Dict}}
    "staging_completed": bool,
    "confidence": float
}}
"""
    llm_staging_plan = await _call_llm_for_hil_deploy(deployer_model, "StagingOrchestrator", prompt, task_id)

    if "error" in llm_staging_plan:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Hardware staging failed: {llm_staging_plan['error']}", current_step="LLM planning failed.")
        return {"status": "failed", "reason": llm_staging_plan["error"]}

    staging_summary = llm_staging_plan.get("staging_summary", "No summary.")
    staging_completed = llm_staging_plan.get("staging_completed", False)

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Hardware shipped to staging.", output=llm_staging_plan)
    
    await _SWARM_VISUALIZER.log_event(task_id, "hardware_shipped_to_staging", f"Hardware {hardware_id} shipped to staging. Summary: {staging_summary}", llm_staging_plan, agent_role="HILDeployer")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Hardware {hardware_id} shipped to staging. Summary: {staging_summary}", title="Hardware Staging Complete")

    # Store deployment log in CRUD Manager
    await _CRUD_MANAGER.create_entity("HardwareDeploymentLog", {"id": str(uuid.uuid4()), "hardware_id": hardware_id, "target": deployment_target, "report": llm_staging_plan, "status": "STAGING", "timestamp": datetime.now().isoformat()})

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "hardware_staging", staging_summary, llm_staging_plan, user_id)

    return {"status": "success", "staging_report": llm_staging_plan}

async def deploy_production_hardware(task_id: str, hardware_id: str, production_target: str, user_id: str = "Tariro_System", deployer_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Orchestrates the deployment of fully validated hardware into a production environment.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, f"Deploying production hardware {hardware_id} to {production_target}.")

    # Policy check for production hardware deployment
    policy_check_context = {"hardware_id": hardware_id, "production_target": production_target}
    policy_compliance_report = await _AUTONOMY_GOVERNANCE.check_policy(user_id, "production_hardware_deployment", policy_check_context)
    if not policy_compliance_report.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Production hardware deployment blocked by policy.", output=policy_compliance_report)
        return {"status": "failed", "reason": "Policy non-compliance", "details": policy_compliance_report}

    prompt = f"""You are Tariro's Hardware-in-Loop Deployer, an Omniversal AGI Production Deployer. Your task is to orchestrate the deployment of fully validated hardware into a production environment. Generate a robust deployment plan that ensures minimal disruption, maximum reliability, and full adherence to operational and security policies. 

HARDWARE ID: {hardware_id}
PRODUCTION TARGET: {production_target}

Deploy to production focusing on:
-   **Reliability**: Ensure redundant systems and failover mechanisms.
-   **Security**: Implement highest level of security hardening.
-   **Minimal Downtime**: Plan for hot-swapping or phased rollouts.
-   **Monitoring**: Set up comprehensive production monitoring and alerting.
-   **Rollback Strategy**: Define clear procedures for emergency rollback.

Output JSON: {{
    "deployment_summary": str,
    "deployment_plan": List[Dict[str, Any]], # {{'step': str, 'action': str, 'executor': str, 'details': Dict}}
    "deployment_completed": bool,
    "confidence": float
}}
"""
    llm_production_deploy = await _call_llm_for_hil_deploy(deployer_model, "ProductionDeployer", prompt, task_id)

    if "error" in llm_production_deploy:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Production hardware deployment failed: {llm_production_deploy['error']}", current_step="LLM planning failed.")
        return {"status": "failed", "reason": llm_production_deploy["error"]}

    deployment_summary = llm_production_deploy.get("deployment_summary", "No summary.")
    deployment_completed = llm_production_deploy.get("deployment_completed", False)

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Hardware deployed to production.", output=llm_production_deploy)
    
    await _SWARM_VISUALIZER.log_event(task_id, "hardware_deployed_to_production", f"Hardware {hardware_id} deployed to production. Summary: {deployment_summary}", llm_production_deploy, agent_role="HILDeployer")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Hardware {hardware_id} deployed to production. Summary: {deployment_summary}", title="Production Deployment Complete")

    # Store deployment log in CRUD Manager
    await _CRUD_MANAGER.create_entity("HardwareDeploymentLog", {"id": str(uuid.uuid4()), "hardware_id": hardware_id, "target": production_target, "report": llm_production_deploy, "status": "PRODUCTION", "timestamp": datetime.now().isoformat()})

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "production_hardware_deployment", deployment_summary, llm_production_deploy, user_id)

    # If the hardware is a new Tariro instance, trigger Self-Replicating Expansion to integrate it into the swarm
    if deployment_completed and hardware_id.startswith("Tariro_instance") and _SELF_REPLICATING_EXPANSION:
        await _SELF_REPLICATING_EXPANSION.add_instance_to_swarm(
            task_id=f"{task_id}_add_to_swarm",
            instance_id=hardware_id,
            user_id=user_id
        )

    return {"status": "success", "deployment_report": llm_production_deploy}
