from extractors.CustomNERTripDetailsExtractor import CustomNERTripDetailsExtractor
from extractors.SpaCyNERTripDetailsExtractor import SpaCyNERTripDetailsExtractor
from extractors.RuleBasedTripDetailsExtractor import RuleBasedTripDetailsExtractor

# Features:
# LOCATION
# ADDRESS
# ATTRACTIONS_COUNT
# TRANSPORT
# MAX_DISTANCE

text = """
hello, i want to visit about 5 attractions and walk about idk 5 kms? in cluj if its possible, thanks
"""

custom_extractor = CustomNERTripDetailsExtractor(model_path="./trip_ner_model")
spacy_extractor = SpaCyNERTripDetailsExtractor()
rule_extractor = RuleBasedTripDetailsExtractor()

print("Custom NER result:", custom_extractor.extract_details(text))
print("SpaCy NER result:", spacy_extractor.extract_details(text))
print("Rule-based result:", rule_extractor.extract_details(text))
