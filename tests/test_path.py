import unittest
from path.best_path import haversine, compute_total_distance, best_path
from path.clustering import dbscan
from input_models import Attraction


class TestTripPlanner(unittest.TestCase):

    def setUp(self):
        self.attractions = [
            Attraction(name="Museum A", latitude=46.77, longitude=23.59, price=0, rating=4.5),
            Attraction(name="Museum B", latitude=46.771, longitude=23.591, price=5, rating=4.2),
            Attraction(name="Park C", latitude=46.772, longitude=23.592, price=10, rating=3.9),
            Attraction(name="Gallery D", latitude=46.778, longitude=23.58, price=2, rating=4.8)
        ]

    def test_haversine_distance(self):
        dist = haversine((46.77, 23.59), (46.771, 23.591))
        self.assertTrue(0 < dist < 500, "Distance should be under 500 meters")

    def test_total_distance(self):
        total_km = compute_total_distance(self.attractions)
        self.assertGreater(total_km, 0)
        self.assertLess(total_km, 5)

    def test_clustering(self):
        clusters = dbscan(self.attractions, eps=150, min_samples=1)
        self.assertIsInstance(clusters, list)
        self.assertTrue(all(isinstance(c, list) for c in clusters))
        self.assertGreaterEqual(len(clusters), 1)

    def test_best_path(self):
        start_point = Attraction(name="Start", latitude=46.77, longitude=23.59, price=0, rating=0)
        clusters = dbscan(self.attractions, eps=150, min_samples=1)
        path = best_path(start_point, clusters, max_distance=5, max_attractions=4)
        self.assertIsInstance(path, list)
        self.assertTrue(all(isinstance(p, Attraction) for p in path))
        self.assertLessEqual(len(path), 4)