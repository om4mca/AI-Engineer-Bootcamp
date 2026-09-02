import inspect
import time
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional


# ==========================================
# 1. Custom Decorators & Assertions
# ==========================================
def execution_timer(func: Callable) -> Callable:
    """Decorator to measure and display function execution time."""

    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = (time.perf_counter() - start) * 1000
        print(f"\n[METRIC] Execution Time ({func.__name__}): {elapsed:.4f} ms")
        return result

    return wrapper


def enforce_types(func: Callable) -> Callable:
    """Decorator enforcing runtime type-checking based on function annotations."""

    def wrapper(*args, **kwargs):
        hints = func.__annotations__
        bound_args = inspect.signature(func).bind(*args, **kwargs)
        bound_args.apply_defaults()

        for param_name, value in bound_args.arguments.items():
            if param_name in hints:
                expected_type = hints[param_name]
                if not isinstance(value, expected_type):
                    raise TypeError(
                        f"Argument '{param_name}' must be of type {expected_type.__name__}, "
                        f"got {type(value).__name__} instead."
                    )
        return func(*args, **kwargs)

    return wrapper


# ==========================================
# 2. Data Structure & Module Definition
# ==========================================
@dataclass
class ConceptNode:
    """Data class representing a Python Core Concept."""

    name: str
    category: str
    definition: str
    code_example: str
    tags: List[str] = field(default_factory=list)


# ==========================================
# 3. Core Engine: Concept Revision Manager
# ==========================================
class ConceptRevisionSystem:

    def __init__(self):
        self._registry: Dict[str, ConceptNode] = {}
        self._load_default_concepts()

    def _load_default_concepts(self):
        """Pre-populates system with standard core Python concepts."""
        defaults = [
            ConceptNode(
                name="Scope & LEGB Rule",
                category="Fundamentals",
                definition="Python resolves variable names using LEGB order: Local, Enclosing, Global, Built-in.",
                code_example=(
                    "x = 'Global'\n"
                    "def outer():\n"
                    "    x = 'Enclosing'\n"
                    "    def inner():\n"
                    "        x = 'Local'\n"
                    "        return x\n"
                    "    return inner()"
                ),
                tags=["scope", "variables", "legb"],
            ),
            ConceptNode(
                name="Type Hinting & Annotations",
                category="Type System",
                definition="Type hints provide explicit syntax for specifying data types, improving code readability and enabling static analysis.",
                code_example=(
                    "def add(a: int, b: int) -> int:\n" "    return a + b"
                ),
                tags=["types", "annotations", "static-analysis"],
            ),
            ConceptNode(
                name="Generators & Lazy Evaluation",
                category="Advanced Flow",
                definition="Generators produce values on-the-fly using the 'yield' keyword, preserving state and optimizing memory.",
                code_example=(
                    "def count_up(n: int):\n"
                    "    for i in range(n):\n"
                    "        yield i"
                ),
                tags=["generators", "memory", "iterators"],
            ),
            ConceptNode(
                name="Decorators",
                category="Metaprogramming",
                definition="A decorator modifies or enhances a function or method dynamically without changing its source code.",
                code_example=(
                    "def log(f):\n"
                    "    def wrapper(*args):\n"
                    "        print('Calling')\n"
                    "        return f(*args)\n"
                    "    return wrapper"
                ),
                tags=["decorators", "functions", "wrappers"],
            ),
        ]
        for concept in defaults:
            self.register_concept(concept)

    def register_concept(self, node: ConceptNode) -> None:
        """Registers a new concept into the registry."""
        self._registry[node.name.lower()] = node

    @execution_timer
    @enforce_types
    def search_concept(self, query: str) -> Optional[ConceptNode]:
        """Searches concepts by name or tags."""
        query_str = query.lower()

        # Direct name lookup
        if query_str in self._registry:
            return self._registry[query_str]

        # Search inside tags or partial names
        for node in self._registry.values():
            if query_str in node.name.lower() or any(
                query_str in t for t in node.tags
            ):
                return node

        return None

    def stream_all_concepts(self):
        """Generator function delivering registered concepts one by one."""
        for concept in self._registry.values():
            yield concept

    def inspect_live_scope(self, target_variable: str) -> str:
        """Inspects runtime scope frames dynamically using the inspect module."""
        caller_frame = inspect.currentframe().f_back
        locals_dict = caller_frame.f_locals
        globals_dict = caller_frame.f_globals

        if target_variable in locals_dict:
            return f"Found '{target_variable}' in Local Scope: {locals_dict[target_variable]}"
        elif target_variable in globals_dict:
            return f"Found '{target_variable}' in Global Scope: {globals_dict[target_variable]}"
        else:
            return (
                f"'{target_variable}' not found in current Local/Global scope."
            )


# ==========================================
# 4. Interactive Execution / Demo
# ==========================================
if __name__ == "__main__":
    system = ConceptRevisionSystem()

    print("============================================")
    print("      PYTHON CONCEPT REVISION SYSTEM        ")
    print("============================================")

    # Demo 1: Stream All Concepts using Generator
    print("\n--- [Demo 1] Streaming Registered Concepts ---")
    for idx, item in enumerate(system.stream_all_concepts(), 1):
        print(f"{idx}. {item.name} ({item.category})")

    # Demo 2: Fast Concept Search with Decorator Validation & Timing
    print("\n--- [Demo 2] Dynamic Concept Lookup ---")
    result = system.search_concept("LEGB")
    if result:
        print(f"\nConcept Found: {result.name}")
        print(f"Category:     {result.category}")
        print(f"Definition:   {result.definition}")
        print("\nCode Example:")
        print("-------------")
        print(result.code_example)

    # Demo 3: Dynamic Scope Inspection
    print("\n--- [Demo 3] Runtime Scope Inspection ---")
    active_session_user = "AI_Engineer_Candidate"
    print(system.inspect_live_scope("active_session_user"))
    print(system.inspect_live_scope("non_existent_var"))

    # Demo 4: Type Checker Decorator Verification (Handling Error)
    print("\n--- [Demo 4] Type Enforcer Decorator Verification ---")
    try:
        # Invalid input type (Integer passed instead of String)
        system.search_concept(12345)
    except TypeError as err:
        print(f"Assertion Triggered Successfully: {err}")