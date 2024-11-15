import importlib
import inspect
from collections import defaultdict

"""
Classifier class whose task is to classify objects by functions and display attributes
"""



def load_objects_from_file(file_name):
    module = importlib.import_module(file_name)
    objects = []
    for name, obj in inspect.getmembers(module, inspect.isclass):
        if obj.__module__ == module.__name__:
            objects.append(obj())
    return objects

def extract_features_with_attributes(objects):
    function_clusters = defaultdict(lambda: {"objects": [], "attributes": []})
    object_attributes = {}  # Атрибуты объектов

    for obj in objects:
        attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
        object_attributes[obj.__class__.__name__] = attributes  # Добавляем атрибуты объекта

        functions = [func for func in dir(obj) if callable(getattr(obj, func)) and not func.startswith("__")]
        for func in functions:
            function_clusters[func]["objects"].append(obj.__class__.__name__)

            func_obj = getattr(obj, func)
            if inspect.isfunction(func_obj) or inspect.ismethod(func_obj):
                sig = inspect.signature(func_obj)
                params = list(sig.parameters.keys())
                function_clusters[func]["attributes"].extend(params)

    for func in function_clusters:
        function_clusters[func]["attributes"] = list(set(function_clusters[func]["attributes"]))

    return function_clusters, object_attributes

def classify_objects_with_attributes(objects):
    function_clusters, object_attributes = extract_features_with_attributes(objects)

    with open("object_categories_with_attributes.txt", "w") as file:
        for func, details in function_clusters.items():
            file.write(f"Function: {func}\n")
            file.write(f"Objects using this function: {', '.join(details['objects'])}\n")
            file.write(f"Attributes used in this function: {', '.join(details['attributes'])}\n\n")

        file.write("\nObject Attributes:\n")
        for obj_name, attributes in object_attributes.items():
            file.write(f"Object: {obj_name}\n")
            file.write(f"Attributes: {', '.join(attributes)}\n\n")

        file.write("\nFunctions used by a single object:\n")
        for func, details in function_clusters.items():
            if len(details['objects']) == 1:
                file.write(f"Function: {func} (used by {details['objects'][0]})\n")
        file.write("\nFunctions used by multiple objects:\n")
        for func, details in function_clusters.items():
            if len(details['objects']) > 1:
                file.write(f"Function: {func} (used by {', '.join(details['objects'])})\n")

if __name__ == "__main__":
    objects = load_objects_from_file("objects")
    classify_objects_with_attributes(objects)

    print("Object classification completed. Results saved to 'object_categories_with_attributes.txt'.")
