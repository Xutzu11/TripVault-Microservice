import spacy
import random
from spacy.training.example import Example
from patterns.location_patterns import PATTERNS as LOCATION_PATTERNS

# Import all training data from your separate files
from data.train_data_clean_prompts import TRAIN_DATA as CLEAN_PROMPT_DATA
from data.train_data_messy_prompts import TRAIN_DATA as MESSY_PROMPT_DATA
from data.train_data_location import TRAIN_DATA as LOCATION_DATA
from data.train_data_attractions_count import TRAIN_DATA as ATTRACTIONS_COUNT_DATA
from data.train_data_transport import TRAIN_DATA as TRANSPORT_DATA
from data.train_data_max_distance import TRAIN_DATA as MAX_DISTANCE_DATA
from data.train_data_address import TRAIN_DATA as ADDRESS_DATA
from data.train_data_rating import TRAIN_DATA as RATING_DATA
from data.train_data_price import TRAIN_DATA as PRICE_DATA

# Combine everything into one big dataset
ALL_TRAIN_DATA = (
    CLEAN_PROMPT_DATA +
    MESSY_PROMPT_DATA +
    LOCATION_DATA +
    ATTRACTIONS_COUNT_DATA +
    TRANSPORT_DATA +
    MAX_DISTANCE_DATA +
    ADDRESS_DATA +
    RATING_DATA +
    PRICE_DATA
)

# Lowercase everything + fix offsets
def preprocess_data(data):
    preprocessed = []
    for text, annotations in data:
        lower_text = text.lower()
        new_entities = []
        for start, end, label in annotations['entities']:
            entity_text = text[start:end]
            entity_text_lower = entity_text.lower()
            # Find new start & end in lower_text
            new_start = lower_text.find(entity_text_lower)
            if new_start == -1:
                print(f"Warning: couldn't find '{entity_text}' in text: {lower_text}")
                continue
            new_end = new_start + len(entity_text_lower)
            new_entities.append((new_start, new_end, label))
        preprocessed.append((lower_text, {"entities": new_entities}))
    return preprocessed


TRAIN_DATA = preprocess_data(ALL_TRAIN_DATA)


# Initialize blank model
nlp = spacy.blank("en")

# Add NER pipeline
ner = nlp.add_pipe("ner")

# Define your labels
labels = ["LOCATION", "ADDRESS", "ATTRACTIONS_COUNT", "TRANSPORT", "MAX_DISTANCE", "MIN_RATING", "MAX_PRICE"]

# Add all labels to NER
for label in labels:
    ner.add_label(label)

# Train the model
other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
with nlp.disable_pipes(*other_pipes):
    optimizer = nlp.begin_training()

    for epoch in range(50):
        print(f"Epoch {epoch + 1}")
        random.shuffle(TRAIN_DATA)
        losses = {}
        for text, annotations in TRAIN_DATA:
            doc = nlp.make_doc(text)
            example = Example.from_dict(doc, annotations)
            nlp.update([example], drop=0.3, losses=losses)
        print(f"Losses: {losses}")

ruler = nlp.add_pipe("entity_ruler", before="ner", config={"phrase_matcher_attr": "LOWER"})
ruler.add_patterns(LOCATION_PATTERNS)


#  Save the combined model (NER + EntityRuler)
nlp.to_disk("./trip_ner_model")
print("NER + EntityRuler model saved to ./trip_ner_model")
