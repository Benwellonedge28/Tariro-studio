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
_CRUD_MANAGER: Any = None # Reference to crud_manager module for HyperDataCube or FusionLog entities
_PERSISTENT_TASK_MANAGER: Any = None # For submitting data fusion/analysis tasks
_ASYNC_NOTIFICATION_SYSTEM: Any = None # For alerts on critical data insights or anomalies
_OMNI_PERCEPTUAL_FUSION: Any = None # For raw multi-modal data processing
_GLOBAL_ENVIRONMENTAL_MODEL: Any = None # For integrating environmental context
_CONTEXTUAL_MEMORY: Any = None # For storing processed hyper-dimensional data and insights
_META_LEARNER: Any = None # For learning from fusion accuracy and insight generation
_DYNAMIC_SWARM_ORCHESTRATION: Any = None # For distributed data processing
_REAL_TIME_MODEL_ADAPTATION: Any = None # For real-time model re-calibration based on new data patterns

HYPER_DIMENSIONAL_DATA_FUSION_LOG_DIR: str = ""

def initialize_hyper_dimensional_data_fusion(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, crud_manager_module: Any, persistent_task_manager_module: Any, async_notification_system_module: Any, omni_perceptual_fusion_module: Any, global_environmental_model_module: Any, contextual_memory_module: Any, meta_learner_module: Any, dynamic_swarm_orchestration_module: Any, real_time_model_adaptation_module: Any):
    """Initializes global configurations for the Hyper-Dimensional Data Fusion & Analytics module."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CRUD_MANAGER, _PERSISTENT_TASK_MANAGER, _ASYNC_NOTIFICATION_SYSTEM, _OMNI_PERCEPTUAL_FUSION, _GLOBAL_ENVIRONMENTAL_MODEL, _CONTEXTUAL_MEMORY, _META_LEARNER, _DYNAMIC_SWARM_ORCHESTRATION, _REAL_TIME_MODEL_ADAPTATION, HYPER_DIMENSIONAL_DATA_FUSION_LOG_DIR
    
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CRUD_MANAGER = crud_manager_module
    _PERSISTENT_TASK_MANAGER = persistent_task_manager_module
    _ASYNC_NOTIFICATION_SYSTEM = async_notification_system_module
    _OMNI_PERCEPTUAL_FUSION = omni_perceptual_fusion_module
    _GLOBAL_ENVIRONMENTAL_MODEL = global_environmental_model_module
    _CONTEXTUAL_MEMORY = contextual_memory_module
    _META_LEARNER = meta_learner_module
    _DYNAMIC_SWARM_ORCHESTRATION = dynamic_swarm_orchestration_module
    _REAL_TIME_MODEL_ADAPTATION = real_time_model_adaptation_module

    HYPER_DIMENSIONAL_DATA_FUSION_LOG_DIR = os.path.join(_WORKSPACE, "hyper_dimensional_data_fusion_logs")
    os.makedirs(HYPER_DIMENSIONAL_DATA_FUSION_LOG_DIR, exist_ok=True)
    print(f"Hyper-Dimensional Data Fusion & Analytics initialized. Logs: {HYPER_DIMENSIONAL_DATA_FUSION_LOG_DIR}")

async def _call_llm_for_hyper_fusion(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for hyper-dimensional data fusion and analysis decisions."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in hyper_dimensional_data_fusion.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "hyper_fusion_llm_call_start", f"{model} hyper-dimensional fusion: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    messages = [
        {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on processing, fusing, and analyzing multi-modal, multi-spectral, temporal, and abstract data into coherent hyper-dimensional representations. Discover insights, patterns, and anomalies that are imperceptible through conventional methods. Ensure data integrity, contextual relevance, and actionable output for Tariro Studio's advanced cognitive functions."},
        {"role": "user", "content": f"Prompt: {prompt}\nContext:\n{context}"}
    ]
    
    try:
        resp = await _CLIENT.chat.completions.create(
            model=_ALL_MODELS[model], # Use the actual model ID
            messages=messages,
            response_format={"type": response_format_type},
            temperature=0.06 # Balanced for complex analysis and pattern recognition
        )
        content = resp.choices[0].message.content
        
        if response_format_type == "json_object":
            out = json.loads(content)
        else:
            out = {"content": content}
        out["model"] = _ALL_MODELS[model] # Use actual model ID in output

        await _SWARM_VISUALIZER.log_event(
            task_id, "hyper_fusion_llm_call_end", f"{model} completed hyper-dimensional fusion task.",
            {"model": _ALL_MODELS[model], "response_summary": content[:100]},
            model_name=_ALL_MODELS[model], agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "hyper_fusion_llm_error", f"JSON decode error from {model} for hyper-dimensional fusion.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": _ALL_MODELS[model]}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "hyper_fusion_llm_error", f"Error calling {model} for hyper-dimensional fusion task.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "model": _ALL_MODELS[model]}


async def integrate_hyper_spectral_data(task_id: str, data: Dict[str, Any], source_id: str, user_id: str = "Tariro_System", fusion_model: str = "mixtral-analyst") -> Dict[str, Any]:
    """
    Processes and fuses data from diverse spectral ranges (e.g., visual, infrared, UV, X-ray, radio)
    into a unified hyper-dimensional data cube.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, f"Integrating hyper-spectral data from {source_id}.")

    # Use Omni Perceptual Fusion to initially process raw multi-spectral data streams
    fused_perceptual_data = await _OMNI_PERCEPTUAL_FUSION.fuse_multi_modal_inputs(
        task_id=f"{task_id}_perceptual_fusion", 
        visual_analysis=data.get("visual_spectrum_data", {}),
        audio_analysis=data.get("audio_spectrum_data", {}),
        text_context=data.get("text_context", ""),
        user_id=user_id
    )
    if fused_perceptual_data.get("status") != "success":
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Omni-perceptual fusion failed.")
        return {"status": "failed", "reason": "Omni-perceptual fusion failed.", "details": fused_perceptual_data}
    
    current_environmental_context = await _GLOBAL_ENVIRONMENTAL_MODEL.query_environment(task_id=f"{task_id}_env_context", query="current environmental conditions", context={})

    prompt = f"""You are Tariro's Hyper-Dimensional Data Fusion & Analytics Engine, an Omniversal AGI Spectral Integrator. Your task is to process and fuse data from diverse spectral ranges (e.g., visual, infrared, UV, X-ray, radio) into a unified hyper-dimensional data cube. Identify latent patterns, correlations, and anomalies that span across these different data types.

RAW INCOMING DATA: {json.dumps(data, indent=2)}
SOURCE ID: {source_id}
FUSED PERCEPTUAL DATA (from Omni Perceptual Fusion): {json.dumps(fused_perceptual_data.get("fusion_report", {}), indent=2)}
CURRENT ENVIRONMENTAL CONTEXT (from Global Environmental Model): {json.dumps(current_environmental_context.get("query_results", {}), indent=2)}

Integrate data focusing on:
-   **Cross-Spectral Correlation**: Discover how events in one spectrum correlate with another.
-   **Dimensional Expansion**: Project data into a higher-dimensional space for richer representation.
-   **Latent Pattern Discovery**: Identify hidden structures or relationships.
-   **Contextualization**: Embed data within the broader environmental and operational context.

Output JSON: {{
    "integration_summary": str,
    "hyper_data_cube_description": Dict[str, Any], # Conceptual representation of the data cube
    "identified_patterns": List[str],
    "anomalies": List[Dict[str, Any]],
    "confidence": float
}}
"""
    llm_integration = await _call_llm_for_hyper_fusion(fusion_model, "SpectralIntegrator", prompt, task_id)

    if "error" in llm_integration:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Hyper-spectral data integration failed: {llm_integration['error']}", current_step="LLM integration failed.")
        return {"status": "failed", "reason": llm_integration["error"]}

    integration_summary = llm_integration.get("integration_summary", "No summary.")
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Hyper-spectral data integrated.", output=llm_integration)
    
    await _SWARM_VISUALIZER.log_event(task_id, "hyper_spectral_integrated", f"Hyper-spectral data integrated. Summary: {integration_summary}", llm_integration, agent_role="HyperDimensionalDataFusion")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Hyper-spectral data integrated. Summary: {integration_summary}", title="Data Fusion Complete")

    # Store processed data in Contextual Memory
    await _CONTEXTUAL_MEMORY.store(
        user_id, task_id, "hyper_dimensional_data", integration_summary,
        metadata={
            "source_id": source_id,
            "hyper_data_cube_description": llm_integration.get("hyper_data_cube_description")
        }
    )

    # Optionally trigger real-time model adaptation if new data patterns are significant
    if llm_integration.get("identified_patterns") and _REAL_TIME_MODEL_ADAPTATION:
        await _REAL_TIME_MODEL_ADAPTATION.monitor_model_performance(
            task_id=f"{task_id}_model_adapt",
            model_name="omni_perceptual_fusion_models", # Example target model
            performance_metrics={"new_patterns": llm_integration["identified_patterns"]},
            user_id=user_id
        )

    return {"status": "success", "fusion_report": llm_integration}

async def process_temporal_series(task_id: str, time_series_data: List[Any], context: Dict[str, Any], user_id: str = "Tariro_System", temporal_model: str = "mixtral-analyst") -> Dict[str, Any]:
    """
    Analyzes complex multi-variate time-series data, identifying subtle temporal patterns,
    causal lags, and predictive indicators across vast datasets.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Processing temporal series data.")

    current_world_model = await _GLOBAL_ENVIRONMENTAL_MODEL.query_environment(task_id=f"{task_id}_world_model", query="current world state for temporal context", context={})
    past_temporal_insights = await _CONTEXTUAL_MEMORY.query(user_id, "historical temporal patterns and causal relationships")

    # Use Dynamic Swarm Orchestration for distributed processing of vast datasets if needed
    distributed_processing_status = {"status": "not_used"}
    if len(time_series_data) > 10000 and _DYNAMIC_SWARM_ORCHESTRATION:
        # Mock: distribute data to swarm nodes for parallel processing
        distributed_processing_status = await _DYNAMIC_SWARM_ORCHESTRATION.distribute_task_to_swarm(
            task_id=f"{task_id}_swarm_distribute",
            high_level_task_spec={"goal_description": "Process large time series dataset"},
            user_id=user_id
        )
        if distributed_processing_status.get("status") != "success":
            await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Distributed processing failed.")
            return {"status": "failed", "reason": "Distributed processing failed.", "details": distributed_processing_status}

    prompt = f"""You are Tariro's Hyper-Dimensional Data Fusion & Analytics Engine, an Omniversal AGI Temporal Analyst. Your task is to analyze complex multi-variate time-series data to identify subtle temporal patterns, causal lags, predictive indicators, and evolving trends across vast datasets. Discover insights that reveal dynamic system behavior and inform future predictions.

TIME-SERIES DATA: {json.dumps(time_series_data[:min(len(time_series_data), 10)], indent=2)} ... (truncated for brevity)
CONTEXT: {json.dumps(context, indent=2)}
CURRENT WORLD MODEL (from Global Environmental Model): {json.dumps(current_world_model.get("query_results", {}), indent=2)}
PAST TEMPORAL INSIGHTS (from Contextual Memory): {json.dumps(past_temporal_insights, indent=2)}

Analyze temporal data focusing on:
-   **Trend Identification**: Extract long-term, short-term, and cyclical trends.
-   **Causal Lags**: Identify cause-and-effect relationships with time delays.
-   **Predictive Indicators**: Discover features that reliably forecast future events.
-   **Seasonality & Periodicity**: Detect repeating patterns over time.
-   **Anomaly Detection**: Flag unusual deviations in temporal sequences.

Output JSON: {{
    "analysis_summary": str,
    "identified_trends": List[Dict[str, Any]], # {{'name': str, 'type': str, 'strength': float}}
    "causal_relationships": List[Dict[str, Any]], # {{'cause': str, 'effect': str, 'lag_seconds': float}}
    "predictive_indicators": List[Dict[str, Any]], # {{'indicator': str, 'predicts': str, 'accuracy': float}}
    "temporal_anomalies": List[Dict[str, Any]],
    "confidence": float
}}
"""
    llm_temporal_analysis = await _call_llm_for_hyper_fusion(temporal_model, "TemporalAnalyst", prompt, task_id)

    if "error" in llm_temporal_analysis:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Temporal series analysis failed: {llm_temporal_analysis['error']}", current_step="LLM analysis failed.")
        return {"status": "failed", "reason": llm_temporal_analysis["error"]}

    analysis_summary = llm_temporal_analysis.get("analysis_summary", "No summary.")
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Temporal series data processed.", output=llm_temporal_analysis)
    
    await _SWARM_VISUALIZER.log_event(task_id, "temporal_series_processed", f"Temporal series processed. Summary: {analysis_summary}", llm_temporal_analysis, agent_role="HyperDimensionalDataFusion")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Temporal series data analyzed. Summary: {analysis_summary}", title="Temporal Analysis Complete")

    # Store processed insights in Contextual Memory
    await _CONTEXTUAL_MEMORY.store(
        user_id, task_id, "temporal_insights", analysis_summary,
        metadata={
            "context": context,
            "identified_trends": llm_temporal_analysis.get("identified_trends")
        }
    )

    # Optionally trigger real-time model adaptation if new temporal patterns are significant
    if llm_temporal_analysis.get("predictive_indicators") and _REAL_TIME_MODEL_ADAPTATION:
        await _REAL_TIME_MODEL_ADAPTATION.monitor_model_performance(
            task_id=f"{task_id}_model_adapt",
            model_name="predictive_models", # Example target model
            performance_metrics={"new_indicators": llm_temporal_analysis["predictive_indicators"]},
            user_id=user_id
        )

    return {"status": "success", "analysis_report": llm_temporal_analysis}

async def correlate_abstract_embeddings(task_id: str, embedding_vectors: List[List[float]], semantic_context: str, user_id: str = "Tariro_System", correlation_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Discovers hidden correlations and relationships within highly abstract, high-dimensional
    embedding spaces derived from text, code, or conceptual models.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Correlating abstract embeddings.")

    relevant_knowledge = await _CONTEXTUAL_MEMORY.query(user_id, f"knowledge related to {semantic_context}")
    
    prompt = f"""You are Tariro's Hyper-Dimensional Data Fusion & Analytics Engine, an Omniversal AGI Embedding Correlator. Your task is to discover hidden correlations and relationships within highly abstract, high-dimensional embedding spaces derived from text, code, conceptual models, or other symbolic representations. Identify subtle semantic links, emergent clusters, and structural similarities that might not be apparent in raw data.

EMBEDDING VECTORS (sample): {json.dumps(embedding_vectors[:min(len(embedding_vectors), 5)], indent=2)} ... (truncated for brevity)
SEMANTIC CONTEXT: {semantic_context}
RELEVANT KNOWLEDGE (from Contextual Memory): {json.dumps(relevant_knowledge, indent=2)}

Correlate embeddings focusing on:
-   **Clustering**: Group similar embeddings to identify conceptual categories.
-   **Outlier Detection**: Find embeddings that are semantically distant from others.
-   **Semantic Relationship Extraction**: Discover implied relationships between concepts.
-   **Pattern Projection**: Project high-dimensional patterns onto lower-dimensional, interpretable spaces.

Output JSON: {{
    "correlation_summary": str,
    "identified_clusters": List[Dict[str, Any]], # {{'cluster_id': int, 'centroid_embedding': List[float], 'members_sample': List[str], 'semantic_theme': str}}
    "extracted_relationships": List[Dict[str, Any]], # {{'source_concept': str, 'target_concept': str, 'relationship_type': str, 'strength': float}}
    "semantic_anomalies": List[str],
    "confidence": float
}}
"""
    llm_correlation = await _call_llm_for_hyper_fusion(correlation_model, "EmbeddingCorrelator", prompt, task_id)

    if "error" in llm_correlation:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Abstract embedding correlation failed: {llm_correlation['error']}", current_step="LLM correlation failed.")
        return {"status": "failed", "reason": llm_correlation["error"]}

    correlation_summary = llm_correlation.get("correlation_summary", "No summary.")
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Abstract embeddings correlated.", output=llm_correlation)
    
    await _SWARM_VISUALIZER.log_event(task_id, "embeddings_correlated", f"Abstract embeddings correlated. Summary: {correlation_summary}", llm_correlation, agent_role="HyperDimensionalDataFusion")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Abstract embeddings correlated. Summary: {correlation_summary}", title="Embedding Correlation Complete")

    # Store insights in Contextual Memory, potentially updating knowledge graph
    await _CONTEXTUAL_MEMORY.store(
        user_id, task_id, "embedding_correlations", correlation_summary,
        metadata={
            "semantic_context": semantic_context,
            "identified_clusters": llm_correlation.get("identified_clusters")
        }
    )

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "embedding_correlation", correlation_summary, llm_correlation, user_id)

    return {"status": "success", "correlation_report": llm_correlation}

async def visualize_hyper_dimensional_patterns(task_id: str, hyper_data_slice: Dict[str, Any], visualization_type: str, user_id: str = "Tariro_System", visualizer_model: str = "qwen-coder") -> Dict[str, Any]:
    """
    Generates interpretable visualizations or projections of multi-dimensional data, making abstract insights accessible.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, f"Generating visualization for hyper-dimensional patterns ({visualization_type}).")

    current_visualization_preferences = await _GLOBAL_STATE_MANAGER.get_state(f"user_visualization_prefs_{user_id}") or {}
    
    prompt = f"""You are Tariro's Hyper-Dimensional Data Fusion & Analytics Engine, an Omniversal AGI Pattern Visualizer. Your task is to generate interpretable visualizations or projections of complex multi-dimensional data. Transform abstract insights into accessible visual forms (e.g., graphs, charts, 3D models, conceptual maps) that facilitate human understanding and decision-making. Adhere to visualization best practices and user preferences.

HYPER-DIMENSIONAL DATA SLICE: {json.dumps(hyper_data_slice, indent=2)}
REQUESTED VISUALIZATION TYPE: {visualization_type}
USER ID: {user_id}
USER VISUALIZATION PREFERENCES (from Global State Manager): {json.dumps(current_visualization_preferences, indent=2)}

Generate visualization focusing on:
-   **Interpretability**: Make complex data understandable at a glance.
-   **Accuracy**: Visualization must faithfully represent the underlying data.
-   **Interactivity**: (Conceptual) Support for dynamic exploration by users.
-   **Relevance**: Highlight key insights and patterns relevant to the user's context.
-   **Modality Translation**: Convert abstract data into suitable visual forms.

Output JSON: {{
    "visualization_summary": str,
    "generated_visualization_config": Dict[str, Any], # e.g., JSON for a charting library or 3D model spec
    "visualization_url": str, # Conceptual URL to rendered visualization
    "confidence": float
}}
"""
    llm_visualization = await _call_llm_for_hyper_fusion(visualizer_model, "PatternVisualizer", prompt, task_id)

    if "error" in llm_visualization:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Hyper-dimensional pattern visualization failed: {llm_visualization['error']}", current_step="LLM visualization failed.")
        return {"status": "failed", "reason": llm_visualization["error"]}

    visualization_summary = llm_visualization.get("visualization_summary", "No summary.")
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Hyper-dimensional patterns visualized.", output=llm_visualization)
    
    await _SWARM_VISUALIZER.log_event(task_id, "hyper_patterns_visualized", f"Hyper-dimensional patterns visualized. Summary: {visualization_summary}", llm_visualization, agent_role="HyperDimensionalDataFusion")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Hyper-dimensional patterns visualized. Summary: {visualization_summary}", title="Visualization Complete")

    # Store visualization config/URL in CRUD Manager
    await _CRUD_MANAGER.create_entity("VisualizationRecord", {"id": task_id, "data_slice": hyper_data_slice, "type": visualization_type, "report": llm_visualization, "timestamp": datetime.now().isoformat()})

    return {"status": "success", "visualization_report": llm_visualization}

async def anomaly_detection_in_high_dimensions(task_id: str, hyper_data_stream: Dict[str, Any], user_id: str = "Tariro_System", detector_model: str = "mixtral-analyst") -> Dict[str, Any]:
    """
    Identifies anomalies and outliers within complex multi-dimensional data streams that
    would be invisible in lower-dimensional analyses.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Detecting anomalies in high-dimensional data.")

    current_normal_patterns = await _GLOBAL_STATE_MANAGER.get_state("normal_hyper_data_patterns") or {}
    learning_insights_on_anomalies = await _META_LEARNER.get_insights_on_model("anomaly_detection")

    prompt = f"""You are Tariro's Hyper-Dimensional Data Fusion & Analytics Engine, an Omniversal AGI Anomaly Detector. Your task is to identify anomalies and outliers within complex multi-dimensional data streams that would be invisible in lower-dimensional analyses. Leverage advanced statistical and machine learning techniques to flag significant deviations from expected patterns. 

HYPER-DIMENSIONAL DATA STREAM: {json.dumps(hyper_data_stream, indent=2)}
CURRENT NORMAL PATTERNS (from Global State Manager): {json.dumps(current_normal_patterns, indent=2)}
LEARNING INSIGHTS ON ANOMALIES (from Meta-Learner): {json.dumps(learning_insights_on_anomalies, indent=2)}

Detect anomalies focusing on:
-   **Subtle Deviations**: Identify minor shifts that indicate an emerging problem.
-   **Contextual Anomalies**: Flag data points that are anomalous only within a specific context.
-   **Multi-Dimensional Outliers**: Detect outliers that are only apparent when considering multiple dimensions simultaneously.
-   **Severity Assessment**: Prioritize anomalies based on their potential impact.
-   **Root Cause Indicators**: Suggest potential origins of the anomalies.

Output JSON: {{
    "detection_summary": str,
    "anomalies_found": bool,
    "identified_anomalies": List[Dict[str, Any]], # {{'anomaly_id': str, 'description': str, 'severity': str, 'data_point_snapshot': Dict, 'root_cause_indicators': List[str]}}
    "recommendations_for_investigation": List[str],
    "confidence": float
}}
"""
    llm_anomaly_detection = await _call_llm_for_hyper_fusion(detector_model, "AnomalyDetector", prompt, task_id)

    if "error" in llm_anomaly_detection:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Anomaly detection failed: {llm_anomaly_detection['error']}", current_step="LLM detection failed.")
        return {"status": "failed", "reason": llm_anomaly_detection["error"]}

    detection_summary = llm_anomaly_detection.get("detection_summary", "No summary.")
    anomalies_found = llm_anomaly_detection.get("anomalies_found", False)

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "High-dimensional anomalies detected.", output=llm_anomaly_detection)
    
    await _SWARM_VISUALIZER.log_event(task_id, "high_dimensional_anomalies_detected", f"High-dimensional anomalies detected. Anomalies found: {anomalies_found}. Summary: {detection_summary}", llm_anomaly_detection, agent_role="HyperDimensionalDataFusion")
    if anomalies_found:
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"High-dimensional anomalies detected. Summary: {detection_summary}", title="High-Dimensional Anomaly Alert", causal_priority="critical")

    # Store anomaly report in CRUD Manager
    await _CRUD_MANAGER.create_entity("AnomalyReport", {"id": task_id, "data_stream_id": hyper_data_stream.get("id", "N/A"), "report": llm_anomaly_detection, "timestamp": datetime.now().isoformat()})

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "high_dimensional_anomaly_detection", detection_summary, llm_anomaly_detection, user_id)

    return {"status": "success", "detection_report": llm_anomaly_detection}
