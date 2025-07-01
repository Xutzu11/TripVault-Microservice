from data.combined.prompts import prompts
from extractors.CustomNERTripDetailsExtractor import CustomNERTripDetailsExtractor
import os

ner_extractor = CustomNERTripDetailsExtractor('../trip_ner_model')

LABELS = ['LOCATION', 'ADDRESS', 'ATTRACTIONS_COUNT', 'TRANSPORT', 'MAX_DISTANCE', 'MAX_PRICE', 'MIN_RATING']
INDIVIDUAL_FOLDER_PATH = "data/individual"


def format_output(raw_output):
    return {
        'LOCATION': [raw_output['location']] if raw_output['location'] else [],
        'ADDRESS': [raw_output['address']] if raw_output['address'] else [],
        'ATTRACTIONS_COUNT': [raw_output['number_of_attractions']] if raw_output['number_of_attractions'] else [],
        'TRANSPORT': [raw_output['transport']] if raw_output['transport'] else [],
        'MAX_DISTANCE': [raw_output['max_distance']] if raw_output['max_distance'] else [],
        'MAX_PRICE': [raw_output['max_price']] if raw_output['max_price'] else [],
        'MIN_RATING': [raw_output['min_rating']] if raw_output['min_rating'] else [],
    }


def write_extraction_results():
    # Process combined prompts
    from data.combined.prompts import prompts as combined_prompts

    results = []
    individual_results = {label: [] for label in LABELS}

    for prompt in combined_prompts:
        raw = ner_extractor.extract_details(prompt)
        formatted = format_output(raw)
        results.append(formatted)
        for label in LABELS:
            value = formatted[label][0] if formatted[label] else ""
            individual_results[label].append(value)

    with open("data/combined/actual.py", "w", encoding="utf-8") as f:
        f.write("actual = [\n")
        for result in results:
            f.write(f"    {result},\n")
        f.write("]\n")

    # for label in LABELS:
    #     folder = label.lower()
    #     path = os.path.join(INDIVIDUAL_FOLDER_PATH, folder)
    #     os.makedirs(path, exist_ok=True)
    #     with open(os.path.join(path, "actual.py"), "w", encoding="utf-8") as f:
    #         f.write("actual = [\n")
    #         for item in individual_results[label]:
    #             f.write(f"    '{item}',\n")
    #         f.write("]\n")

    # Process individual prompts
    # for label in LABELS:
    #     folder = label.lower()
    #     try:
    #         module_path = f"data.individual.{folder}.prompts"
    #         individual_prompts = __import__(module_path, fromlist=['prompts']).prompts
    #
    #         individual_actuals = []
    #         for prompt in individual_prompts:
    #             raw = ner_extractor.extract_details(prompt)
    #             formatted = format_output(raw)
    #             value = formatted[label][0] if formatted[label] else ""
    #             individual_actuals.append(value)
    #
    #         with open(os.path.join(INDIVIDUAL_FOLDER_PATH, folder, "actual.py"), "w", encoding="utf-8") as f:
    #             f.write("actual = [\n")
    #             for item in individual_actuals:
    #                 f.write(f"    '{item}',\n")
    #             f.write("]\n")
    #
    #     except Exception as e:
    #         print(f"Failed to process prompts for {label}: {e}")
