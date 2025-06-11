import spacy

class SpaCyNERTripDetailsExtractor:
    def __init__(self, model_name="en_core_web_sm"):
        self.ner_model = spacy.load(model_name)

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
        # Look for GPE / LOC labels
        for ent in doc.ents:
            if ent.label_ in ["GPE", "LOC"]:
                return ent.text
        return None

    def _extract_address(self, doc):
        # spaCy doesn't have a direct ADDRESS label, but FAC (facilities) is the closest
        for ent in doc.ents:
            if ent.label_ == "FAC":
                return ent.text
        return None

    def _extract_number_of_attractions(self, doc):
        # No direct support; look for CARDINAL as a fallback
        for ent in doc.ents:
            if ent.label_ == "CARDINAL":
                return ent.text
        return None

    def _extract_transport(self, doc):
        # No direct NER label for transport; not handled out of the box
        return None

    def _extract_max_distance(self, doc):
        # QUANTITY may capture something like "20 kilometers"
        for ent in doc.ents:
            if ent.label_ == "QUANTITY":
                return ent.text
        return None

    def _extract_min_rating(self, doc):
        # No direct NER label for rating; not handled out of the box
        return None

    def _extract_max_price(self, doc):
        # No direct NER label for price; not handled out of the box
        return None
