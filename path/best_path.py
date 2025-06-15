from heapq import heappush, heappop
from math import radians, sin, cos, sqrt, atan2
from input_models import Attraction


def haversine(coord1, coord2):
    r = 6371000  # meters
    lat1, lon1 = map(radians, coord1)
    lat2, lon2 = map(radians, coord2)

    d_lat = lat2 - lat1
    d_lon = lon2 - lon1

    a = sin(d_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(d_lon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return r * c


def compute_total_distance(path):
    total = 0.0
    prev = (path[0].latitude, path[0].longitude)
    for p in path[1:]:
        total += haversine(prev, (p.latitude, p.longitude))
        prev = (p.latitude, p.longitude)
    return total / 1000


def attraction_scoring_function(attraction: Attraction,
                                max_price=100):
    w_price = 0.5
    w_rating = 0.3
    return (max_price if attraction.price == 0 else max_price / attraction.price) * w_price + attraction.rating * w_rating


def path_scoring_function(distance, price, rating, count,
                          max_dist=100, max_price=1000, min_rating=2.5, max_attractions=5):
    w_dist = 0.7
    w_price = 0.5
    w_rating = 0.3
    w_count = 0.4
    score_dist = 1 - (abs(max_dist - distance) / max_dist) * (1 if distance <= max_dist else 2)
    score_price = 1 - (abs(max_price - price) / max_price) * (1 if price <= max_price else 3)
    score_rating = 1 - (abs(min_rating - rating) / (5 - min_rating)) * (1 if rating >= min_rating else 2)
    score_count = 1 - (abs(max_attractions - count) / max_attractions) * (1 if count <= max_attractions else 2)

    return (
            w_dist * score_dist +
            w_price * score_price +
            w_rating * score_rating +
            w_count * score_count
    )


def best_path(start_point, clusters,
              max_distance=100, min_rating=2.5, max_price=1000, max_attractions=5,
              max_steps=100):
    initial_state = {
        'path': [start_point],
        'visited_clusters': set(),
        'total_distance': 0.0,
        'total_price': 0.0,
        'avg_rating': 0.0
    }

    beam = [(0, initial_state)]

    for step in range(max_steps):
        new_beam = []
        for _, state in beam:
            for cluster_index, cluster in enumerate(clusters):
                if cluster_index in state['visited_clusters']:
                    continue

                # sort the cluster by attraction scoring function
                sorted_cluster = sorted(cluster, key=lambda x: -attraction_scoring_function(x, max_price))

                # create new state
                new_path = state['path'] + sorted_cluster[:3]
                new_clusters = state['visited_clusters'] | {cluster_index}
                new_total_distance = (state['total_distance'] +
                                      compute_total_distance([state['path'][-1]] + sorted_cluster[:3])
                                      )
                new_total_price = state['total_price'] + sum(a.price for a in sorted_cluster[:3])
                new_avg_rating = (state['avg_rating'] * len(state['path']) + sum(
                    a.rating for a in sorted_cluster[:3])) / len(new_path)
                new_state = {
                    'path': new_path,
                    'visited_clusters': new_clusters,
                    'total_distance': new_total_distance,
                    'total_price': new_total_price,
                    'avg_rating': new_avg_rating
                }
                heappush(new_beam,
                         (path_scoring_function(new_total_distance, new_total_price, new_avg_rating, len(new_path),
                                                max_distance, max_price, min_rating, max_attractions), new_state))
        while len(new_beam) > 0:
            beam.append(heappop(new_beam))
        while len(beam) > max_steps:
            heappop(beam)

    while len(beam) > 1:
        heappop(beam)
    return heappop(beam)[1]['path'][1:]  # Exclude the start point from the path
