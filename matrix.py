import importlib
import inspect
import numpy as np
from collections import defaultdict

"""
Test creation of matrices
"""

def load_objects_from_file(file_name):
    module = importlib.import_module(file_name)
    objects = []
    for name, obj in inspect.getmembers(module, inspect.isclass):
        if obj.__module__ == module.__name__:
            objects.append(obj())
    return objects


def extract_features_and_attributes(objects):
    all_functions = set()
    all_attributes = set()

    for obj in objects:
        functions = [func for func in dir(obj) if callable(getattr(obj, func)) and not func.startswith("__")]
        attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

        all_functions.update(functions)
        all_attributes.update(attributes)

    all_functions = list(all_functions)
    all_attributes = list(all_attributes)

    function_matrix = []
    attribute_matrix = []
    function_to_attributes = defaultdict(set)

    for obj in objects:
        functions = [func for func in dir(obj) if callable(getattr(obj, func)) and not func.startswith("__")]
        function_vector = [1 if func in functions else 0 for func in all_functions]

        attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
        attribute_vector = [1 if attr in attributes else 0 for attr in all_attributes]
        for func in functions:
            func_code = inspect.getsource(getattr(obj, func))
            for attr in attributes:
                if attr in func_code:
                    function_to_attributes[func].add(attr)

        function_matrix.append(function_vector)
        attribute_matrix.append(attribute_vector)

    return (
        np.array(function_matrix),
        np.array(attribute_matrix),
        all_functions,
        all_attributes,
        function_to_attributes
    )


def create_combined_matrix(function_matrix, attribute_matrix):
    return np.hstack((function_matrix, attribute_matrix))


def print_function_to_attributes_mapping(function_to_attributes):
    print("\nMapping of functions to attributes:")
    for func, attrs in function_to_attributes.items():
        print(f"Function: {func}, Attributes: {', '.join(attrs)}")


if __name__ == "__main__":
    objects = load_objects_from_file("objects")
    function_matrix, attribute_matrix, all_functions, all_attributes, function_to_attributes = extract_features_and_attributes(
        objects)

    combined_matrix = create_combined_matrix(function_matrix, attribute_matrix)
    print("Function Matrix:")
    print(function_matrix)
    print("\nAttribute Matrix:")
    print(attribute_matrix)
    print("\nCombined Matrix:")
    print(combined_matrix)

    print("\nAll Functions:")
    print(all_functions)
    print("\nAll Attributes:")
    print(all_attributes)

    print_function_to_attributes_mapping(function_to_attributes)
