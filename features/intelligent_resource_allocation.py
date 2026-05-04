
# intelligent_resource_allocation.py
# TARIRO Studio: Intelligent Resource Allocation for Business Processes

import datetime
import random
from collections import defaultdict

class ResourceAllocator:
    def __init__(self, resources, business_processes, strategic_priorities):
        self.resources = resources  # e.g., {'human': {'devs': 10, 'qa': 5}, 'compute': {'servers': 20, 'gpu': 5}}
        self.business_processes = business_processes  # {process_name: {'demands': {'human.devs': 2, 'compute.servers': 5}, 'priority': 'high', 'performance': 0.8}}
        self.strategic_priorities = strategic_priorities  # e.g., {'process_A': 'high', 'process_B': 'medium'}
        self.allocation_logs = []
        print("Intelligent Resource Allocator initialized.")

    def _evaluate_resource_availability(self):
        """
        Evaluates the current availability of all resources.
        """
        print("Evaluating current resource availability...")
        available = {}
        for category, items in self.resources.items():
            available[category] = {item: count for item, count in items.items() if count > 0}
        return available

    def _calculate_process_demand(self):
        """
        Aggregates resource demands from all active business processes.
        """
        print("Calculating aggregated resource demands...")
        total_demand = defaultdict(float)
        for process_name, details in self.business_processes.items():
            for resource_path, quantity in details.get("demands", {}).items():
                total_demand[resource_path] += quantity
        return total_demand

    def _optimize_allocation(self, available_resources, total_demand):
        """
        Optimizes resource allocation based on availability, demand, and strategic priorities.
        This is a simplified heuristic; real optimization would use linear programming or advanced algorithms.
        """
        print("Optimizing resource allocation...")
        new_allocations = defaultdict(dict)
        remaining_resources = {cat: {item: count for item, count in self.resources[cat].items()} for cat in self.resources}
        
        # Sort processes by strategic priority (high > medium > low)
        sorted_processes = sorted(self.business_processes.items(), key=lambda item: {'high': 3, 'medium': 2, 'low': 1}.get(item[1].get('priority', 'medium'), 0), reverse=True)

        for process_name, details in sorted_processes:
            process_demands = details.get("demands", {})
            allocated_for_process = {}
            can_fully_allocate = True

            for resource_path, quantity_needed in process_demands.items():
                category, item = resource_path.split('.')
                if remaining_resources[category][item] >= quantity_needed:
                    allocated_for_process[resource_path] = quantity_needed
                    remaining_resources[category][item] -= quantity_needed
                else:
                    # Cannot fully meet demand for this process, try partial if possible
                    allocated_for_process[resource_path] = remaining_resources[category][item]
                    remaining_resources[category][item] = 0
                    can_fully_allocate = False
            
            if can_fully_allocate:
                new_allocations[process_name] = allocated_for_process
                print(f"  Fully allocated resources for process: {process_name}")
            else:
                print(f"  Partially allocated resources for process: {process_name} (Insufficient resources)")
                # Revert allocation for this process if it can't be fully satisfied (simple rollback)
                # In a real system, more complex partial allocation or preemption would be considered
                # For this example, we just don't add partial allocation to new_allocations.

        return new_allocations, remaining_resources

    def run_allocation_cycle(self):
        """
        Runs a full cycle of intelligent resource allocation.
        """
        print("\n--- Running Intelligent Resource Allocation Cycle ---")
        available = self._evaluate_resource_availability()
        demands = self._calculate_process_demand()
        optimized_allocations, final_remaining = self._optimize_allocation(available, demands)

        self.allocation_logs.append({
            "timestamp": datetime.datetime.now().isoformat(),
            "initial_resources": self.resources,
            "total_demands": demands,
            "optimized_allocations": optimized_allocations,
            "remaining_resources": final_remaining
        })
        print("--- Resource Allocation Cycle Complete ---")
        return optimized_allocations, final_remaining

# Example usage:
if __name__ == "__main__":
    # Dummy data for demonstration
    initial_resources_example = {
        "human": {"devs": 10, "qa": 5, "managers": 3},
        "compute": {"servers": 20, "gpu": 5, "storage_tb": 100},
        "budget": {"marketing": 50000, "R&D": 100000}
    }
    
    business_processes_example = {
        "Product_Development": {
            "demands": {"human.devs": 6, "compute.servers": 8, "compute.gpu": 2, "budget.R&D": 50000},
            "priority": "high",
            "performance": 0.9
        },
        "Customer_Support_System": {
            "demands": {"human.qa": 2, "compute.servers": 5, "budget.marketing": 10000},
            "priority": "medium",
            "performance": 0.8
        },
        "Marketing_Campaign": {
            "demands": {"human.managers": 1, "compute.servers": 3, "budget.marketing": 40000},
            "priority": "high",
            "performance": 0.7
        },
        "Internal_Tooling": {
            "demands": {"human.devs": 2, "compute.servers": 2},
            "priority": "low",
            "performance": 0.6
        }
    }
    strategic_priorities_example = {"Product_Development": "critical", "Marketing_Campaign": "high"}

    allocator = ResourceAllocator(
        resources=initial_resources_example,
        business_processes=business_processes_example,
        strategic_priorities=strategic_priorities_example
    )

    optimized_allocations, remaining_resources = allocator.run_allocation_cycle()

    print("\n--- Optimized Allocations ---")
    for process, allocation in optimized_allocations.items():
        print(f"Process: {process}")
        for res, qty in allocation.items():
            print(f"  - {res}: {qty}")
    
    print("\n--- Remaining Resources ---")
    for category, items in remaining_resources.items():
        for item, qty in items.items():
            print(f"- {category}.{item}: {qty}")
