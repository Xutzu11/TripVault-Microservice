import spacy

class CustomNERTripDetailsExtractor:
    def __init__(self, model_path="./trip_ner_model"):
        self.ner_model = spacy.load(model_path)

    def extract_details(self, text):
        doc = self.ner_model(text)

        return {
            "location": self._extract_location(doc),
            "address": self._extract_address(doc),
            "number_of_attractions": self._extract_number_of_attractions(doc),
            "transport": self._extract_transport(doc),
            "max_distance": self._extract_max_distance(doc),
            "min_rating": self._extract_min_rating(doc),
            "max_price": self._extract_max_price(doc)
        }

    def _extract_location(self, doc):
        for ent in doc.ents:
            if ent.label_ == "LOCATION":
                return ent.text
        return None

    def _extract_address(self, doc):
        for ent in doc.ents:
            if ent.label_ == "ADDRESS":
                return ent.text
        return None

    def _extract_number_of_attractions(self, doc):
        for ent in doc.ents:
            if ent.label_ == "ATTRACTIONS_COUNT":
                return ent.text
        return None

    def _extract_transport(self, doc):
        for ent in doc.ents:
            if ent.label_ == "TRANSPORT":
                return ent.text
        return None

    def _extract_max_distance(self, doc):
        for ent in doc.ents:
            if ent.label_ == "MAX_DISTANCE":
                return ent.text
        return None

    def _extract_min_rating(self, doc):
        for ent in doc.ents:
            if ent.label_ == "MIN_RATING":
                return ent.text
        return None

    def _extract_max_price(self, doc):
        for ent in doc.ents:
            if ent.label_ == "MAX_PRICE":
                return ent.text
        return None
