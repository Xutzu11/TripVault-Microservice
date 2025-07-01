import os
import importlib.util

BASE_PATH = "data"
LABELS = ['LOCATION', 'ADDRESS', 'ATTRACTIONS_COUNT', 'TRANSPORT', 'MAX_DISTANCE', 'MAX_PRICE', 'MIN_RATING']


def load_module_from_file(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if not spec or not spec.loader:
        raise ImportError(f"Cannot load {module_name} from {file_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def compute_accuracy_combined(expected, actual, label):
    correct = 0
    total = 0
    for e, a in zip(expected, actual):
        expected_vals = set([v.lower() for v in e.get(label, [])])
        actual_vals = set([v.lower() for v in a.get(label, [])])
        total += len(expected_vals)
        correct += len(expected_vals & actual_vals)
    return round(correct / total, 2) if total > 0 else 1.0 if correct == 0 else 0.0


def compute_accuracy_individual(expected_list, actual_list):
    correct = 0
    total = len(expected_list)
    for e, a in zip(expected_list, actual_list):
        if e.strip().lower() == a.strip().lower():
            correct += 1
    return round(correct / total, 2) if total > 0 else 1.0 if correct == 0 else 0.0


def process_combined():
    expected_mod = load_module_from_file("combined_expected", os.path.join(BASE_PATH, "combined", "expected.py"))
    actual_mod = load_module_from_file("combined_actual", os.path.join(BASE_PATH, "combined", "actual.py"))

    expected = expected_mod.expected
    actual = actual_mod.actual

    combined_accuracies = []
    print("Combined Prompt Accuracies:")
    for label in LABELS:
        acc = compute_accuracy_combined(expected, actual, label)
        print(f"{label}: {acc}")
        combined_accuracies.append(acc)

    with open(os.path.join(BASE_PATH, "combined", "accuracy.py"), "w") as f:
        f.write(f"combined_acc = {combined_accuracies}\n")


def process_individual():
    print("\nIndividual Prompt Accuracies:")
    all_individual_accuracies = []

    for label in LABELS:
        folder = label.lower()
        expected_path = os.path.join(BASE_PATH, "individual", folder, "expected.py")
        actual_path = os.path.join(BASE_PATH, "individual", folder, "actual.py")

        try:
            expected_mod = load_module_from_file(f"{folder}_expected", expected_path)
            actual_mod = load_module_from_file(f"{folder}_actual", actual_path)

            expected = expected_mod.expected
            actual = actual_mod.actual

            acc = compute_accuracy_individual(expected, actual)
            print(f"{label}: {acc}")
            all_individual_accuracies.append(acc)

            with open(os.path.join(BASE_PATH, "individual", folder, "accuracy.py"), "w") as f:
                f.write(f"individual_acc = {acc}\n")

        except Exception as e:
            print(f"Failed for {label} ({folder}): {e}")
            all_individual_accuracies.append(0.0)

    summary_path = os.path.join(BASE_PATH, "individual", "accuracy.py")
    with open(summary_path, "w") as f:
        f.write(f"individual_acc = {all_individual_accuracies}\n")

