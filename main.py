from fastapi import FastAPI, HTTPException
from extractors.CustomNERTripDetailsExtractor import CustomNERTripDetailsExtractor
from extractors.RuleBasedTripDetailsExtractor import RuleBasedTripDetailsExtractor
from extractors.SpaCyNERTripDetailsExtractor import SpaCyNERTripDetailsExtractor
from converters.TripDetailsConverter import TripDetailConverter
from input_models import PromptInput, PathInput
from clustering import dbscan
from best_path import best_path
import traceback

app = FastAPI()

# Load extractors and converter
ner_extractor = CustomNERTripDetailsExtractor()
rule_extractor = RuleBasedTripDetailsExtractor()
spacy_extractor = SpaCyNERTripDetailsExtractor()
converter = TripDetailConverter()


@app.post("/internal/extract-filters")
def extract_filters(input: PromptInput):
    try:
        prompt = input.prompt
        print(f"Prompt: {prompt}")
        ner_filters = ner_extractor.extract_details(prompt)
        print(f"NER Filters: {ner_filters}")
        rule_filters = rule_extractor.extract_details(prompt)
        print(f"Rule Filters: {rule_filters}")
        spacy_filters = spacy_extractor.extract_details(prompt)
        print(f"Spacy Filters: {spacy_filters}")
        for key in ner_filters:
            if ner_filters[key] is None:
                ner_filters[key] = rule_filters[key]
            if ner_filters[key] is None:
                ner_filters[key] = spacy_filters[key]

        return converter.convert(ner_filters)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/internal/optimal-path")
def optimal_path(input: PathInput):
    try:
        clusters = dbscan(attractions=input.attractions, eps=100, min_samples=1)
        print(f"Clusters: {clusters}")
        optimal_path_result = best_path(start_point=input.start_point,
                                        clusters=clusters,
                                        max_distance=input.max_distance,
                                        min_rating=input.min_rating,
                                        max_price=input.max_price,
                                        max_attractions=input.nr_attractions)
        print(f"Optimal path found: {optimal_path_result}")
        return {
            "best_attractions": optimal_path_result,
        }
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
