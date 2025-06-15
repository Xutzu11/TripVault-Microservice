import unittest
from extractors.CustomNERTripDetailsExtractor import CustomNERTripDetailsExtractor
from converters.TripDetailsConverter import TripDetailConverter
from helpers.transport_word_lists import WALKING_WORDS, DRIVING_WORDS, TRANSIT_WORDS
from helpers.location_word_lists import STATES, CITIES

class TestNERExtraction(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ner = CustomNERTripDetailsExtractor()
        cls.converter = TripDetailConverter(
            walking_words=WALKING_WORDS,
            driving_words=DRIVING_WORDS,
            transit_words=TRANSIT_WORDS,
            city_list=CITIES,
            state_list=STATES
        )

    def test_basic_extraction(self):
        prompt = "I want to visit about five attractions in Cluj. I will walk and go max 7 kms. Staying on Strada Campului 42."

        raw = self.ner.extract_details(prompt)
        cleaned = self.converter.convert(raw)

        self.assertEqual(cleaned["number_of_attractions"], 5)
        self.assertEqual(cleaned["transport"], "WALKING")
        self.assertEqual(cleaned["max_distance"], 7)
        self.assertEqual(cleaned["location"]["city"], "cluj")
        self.assertIn("campului", cleaned["address"].lower())

    def test_unspecific_attractions(self):
        prompt = "I want to see some attractions in Oradea. I plan to walk."
        raw = self.ner.extract_details(prompt)
        cleaned = self.converter.convert(raw)

        self.assertEqual(cleaned["number_of_attractions"], -1)  # Or None if you prefer
        self.assertEqual(cleaned["transport"], "WALKING")
        self.assertEqual(cleaned["location"]["city"], "oradea")

    def test_miles_conversion(self):
        prompt = "I want to drive no more than 3 miles. Starting from Piata Avram Iancu 2, Cluj."
        raw = self.ner.extract_details(prompt)
        cleaned = self.converter.convert(raw)

        self.assertEqual(cleaned["transport"], "DRIVING")
        self.assertAlmostEqual(cleaned["max_distance"], 4.83, places=1)  # 3 miles ≈ 4.83 km
