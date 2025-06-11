import re
from helpers.transport_word_lists import WALKING_WORDS, DRIVING_WORDS, TRANSIT_WORDS
from helpers.quantity_word_lists import FEW_WORDS, MID_WORDS, MANY_WORDS
from helpers.location_word_lists import CITIES, STATES, TYPE_MAP
from helpers.numbers_word_lists import WORD_TO_NUMBER
from forex_python.converter import CurrencyRates

class TripDetailConverter:
    def __init__(self):
        self.currency_converter = CurrencyRates()
        self.FEW, self.MID, self.MANY = 2, 5, 8
        self.defaults = {"location": "bucharest",
                         "address": None,
                         "number_of_attractions": 5,
                         "transport": "WALKING",
                         "max_distance": 10,
                         "min_rating": 3.5,
                         "max_price": 200}

    def convert(self, raw_text):
        if not raw_text:
            return self.defaults
        return {
            "location": self.convert_location(raw_text.get("location")),
            "address": self.convert_address(raw_text.get("address")),
            "number_of_attractions": self.convert_number_of_attractions(raw_text.get("number_of_attractions")),
            "transport": self.convert_transport(raw_text.get("transport")),
            "max_distance": self.convert_max_distance(raw_text.get("max_distance")),
            "min_rating": self.convert_min_rating(raw_text.get("min_rating")),
            "max_price": self.convert_max_price(raw_text.get("max_price"))
        }

    def convert_location(self, raw_location):
        if not raw_location:
            return {"city": None, "state": self.defaults["location"]}
        raw_location = raw_location.lower()
        city, state = None, self.defaults["location"]
        for c in CITIES:
            if c in raw_location:
                city = c
                break
        for s in STATES:
            if s in raw_location:
                state = s
                break
        return {"city": city, "state": state}

    def convert_address(self, raw_address):
        if not raw_address:
            return self.defaults["address"]
        for eng, ro in TYPE_MAP.items():
            if eng in raw_address:
                raw_address = raw_address.replace(eng, ro)
                return raw_address.strip()
        return raw_address.strip()

    def convert_number_of_attractions(self, raw_text):
        if not raw_text:
            return self.defaults["number_of_attractions"]
        raw_text = raw_text.lower()
        match = re.search(r'\d+', raw_text)
        if match:
            return int(match.group())
        for word, val in WORD_TO_NUMBER.items():
            if word in raw_text:
                return val
        for word in FEW_WORDS:
            if word in raw_text:
                return self.FEW
        for word in MID_WORDS:
            if word in raw_text:
                return self.MID
        for word in MANY_WORDS:
            if word in raw_text:
                return self.MANY
        return self.defaults["number_of_attractions"]

    def convert_transport(self, raw_text):
        if not raw_text:
            return self.defaults["transport"]
        raw_text = raw_text.lower()
        if raw_text in WALKING_WORDS:
            return "WALKING"
        if raw_text in DRIVING_WORDS:
            return "DRIVING"
        if raw_text in TRANSIT_WORDS:
            return "TRANSIT"
        return self.defaults["transport"]

    def convert_max_distance(self, raw_text):
        if not raw_text:
            return self.defaults["max_distance"]
        raw_text = raw_text.lower().strip()
        match = re.search(r'(\d+(?:\.\d+)?)', raw_text)
        value = self.defaults["max_distance"]
        if not match:
            for word, val in WORD_TO_NUMBER.items():
                if word in raw_text:
                    value = val
                    break
        else:
            value = float(match.group(1))

        # regex to detect units accurately
        if re.search(r'\bm\b|\bmeters?\b|\bmeteres\b', raw_text):
            return round(value / 1000, 2)
        elif re.search(r'\bmiles?\b', raw_text):
            return round(value * 1.60934, 2)
        else:  # assume km by default
            return round(value, 2)

    def convert_min_rating(self, raw_text):
        if not raw_text:
            return self.defaults["min_rating"]

        raw_text = raw_text.lower().strip()

        # Replace comma with dot for float parsing
        match = re.search(r'(\d+(?:[\.,]\d+)?)', raw_text)
        value = self.defaults["min_rating"]

        if match:
            num_str = match.group(1).replace(",", ".")
            try:
                num = float(num_str)
                if num <= 5:
                    value = num
                elif 5 < num <= 10:
                    value = round((num / 10) * 5, 2)
                elif num > 10:
                    value = round((num / 100) * 5, 2)
            except ValueError:
                pass

        return round(value, 2)

    def convert_max_price(self, raw_text):
        if not raw_text:
            return round(self.defaults["max_price"])

        raw_text = raw_text.lower().strip()
        match = re.search(r'(\d+(?:[\.,]\d+)?)', raw_text)
        value = self.defaults["max_price"]

        if match:
            num_str = match.group(1).replace(",", ".")
            try:
                price = float(num_str)
            except ValueError:
                return round(value, 2)
        else:
            return round(value, 2)

        # Currency detection & conversion
        if re.search(r'\$|usd|dollars?', raw_text):
            return round(price, 2)
        elif re.search(r'€|eur|euros?', raw_text):
            return round(self.currency_converter.convert('EUR', 'USD', price), 2)
        elif re.search(r'\bron\b|\blei?\b', raw_text):
            return round(self.currency_converter.convert('RON', 'USD', price), 2)
        else:
            # default to USD
            return round(price, 2)
