import logging
import os
import importlib.util
from typing import Any, Dict, List, Optional

logger = logging.getLogger("ModuleRegistry")

class ModuleRegistry:
    """
    Manages dynamic loading and registration of runtime modules.
    """
    def __init__(self, base_path: str, security_kernel: Any):
        self.base_path = base_path
        self.security_kernel = security_kernel # Reference to the SecurityKernel
        self.modules: Dict[str, Any] = {}

    def register_module(self, name: str, module_instance: Any):
        """Registers an instance of a module."""
        if name in self.modules:
            logger.warning(f"Module {name} already registered. Overwriting.")
        self.modules[name] = module_instance
        logger.info(f"Module '{name}' registered.")

    def get_module(self, name: str) -> Optional[Any]:
        """Retrieves a registered module by name."""
        return self.modules.get(name)

    def load_module_from_path(self, module_name: str, path: str) -> Optional[Any]:
        """
        Dynamically loads a module from a given file path.
        Includes basic security checks.
        """
        module_file_path = os.path.join(path, f"{module_name}.py")
        if not os.path.exists(module_file_path):
            logger.error(f"Module file not found at {module_file_path}")
            return None

        spec = importlib.util.spec_from_file_location(module_name, module_file_path)
        if spec is None:
            logger.error(f"Could not load module specification for {module_name} from {module_file_path}")
            return None

        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        try:
            spec.loader.exec_module(module)
            logger.info(f"Dynamically loaded module '{module_name}' from {module_file_path}")
            # Perform security scan on the loaded module's code
            with open(module_file_path, 'r') as f:
                code = f.read()
            vulnerabilities = asyncio.run(self.security_kernel.scan_for_vulnerabilities(code))
            if vulnerabilities:
                logger.critical(f"Module {module_name} contains vulnerabilities: {vulnerabilities}. Blocking registration.")
                return None
            return module
        except Exception as e:
            logger.error(f"Error executing module {module_name} from {module_file_path}: {e}", exc_info=True)
            return None
