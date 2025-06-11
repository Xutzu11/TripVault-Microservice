import re
from helpers.transport_word_lists import WALKING_WORDS, DRIVING_WORDS, TRANSIT_WORDS
class RuleBasedTripDetailsExtractor:
    def __init__(self):
        pass  # Nothing to initialize

    def extract_details(self, text):
        return {
            "location": self._extract_location(text),
            "address": self._extract_address(text),
            "number_of_attractions": self._extract_number_of_attractions(text),
            "transport": self._extract_transport(text),
            "max_distance": self._extract_max_distance(text),
            "min_rating": self._extract_min_rating(text),
            "max_price": self._extract_max_price(text)
        }

    def _extract_location(self, text):
        match = re.search(r"in ([A-Z][a-z]+(?:, [A-Z][a-z]+)?)", text)
        return match.group(1) if match else None

    def _extract_address(self, text):
        match = re.search(r"(street\s+\w+.*?\d+)", text, re.IGNORECASE)
        return match.group(1) if match else None

    def _extract_number_of_attractions(self, text):
        match = re.search(r"(\d+)\s*(attraction|places|spots)", text, re.IGNORECASE)
        return match.group(1) if match else None

    def _extract_transport(self, text):
        transport_options = WALKING_WORDS + DRIVING_WORDS + TRANSIT_WORDS
        text_lower = text.lower()
        for transport in transport_options:
            if transport in text_lower:
                return transport
        return None

    def _extract_max_distance(self, text):
        match = re.search(r"(?:at least|min|at most|max(?:imum)?)\s*(\d+)\s*(kilometers|km|meters|m)", text, re.IGNORECASE)
        return f"{match.group(1)} {match.group(2)}" if match else None


    def _extract_min_rating(self, text):
        match = re.search(r"(?:at least|min) (rating|stars|points)\s*(\d+(\.\d+)?)", text, re.IGNORECASE)
        return match.group(1) if match else None


    def _extract_max_price(self, text):
        match = re.search(r"(?:at most|max(?:imum)?)\s*\$?(\d+)", text, re.IGNORECASE)
        return match.group(1) if match else None