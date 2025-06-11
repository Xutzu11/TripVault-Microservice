from math import radians, sin, cos, sqrt, atan2


def haversine(coord1, coord2):
    r = 6371000  # meters
    lat1, lon1 = map(radians, coord1)
    lat2, lon2 = map(radians, coord2)

    d_lat = lat2 - lat1
    d_lon = lon2 - lon1

    a = sin(d_lat / 2)**2 + cos(lat1) * cos(lat2) * sin(d_lon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return r * c


def region_query(attractions, point_idx, eps):
    neighbors = []
    lat1, lon1 = attractions[point_idx].latitude, attractions[point_idx].longitude
    for i, other in enumerate(attractions):
        lat2, lon2 = other.latitude, other.longitude
        if haversine((lat1, lon1), (lat2, lon2)) <= eps:
            neighbors.append(i)
    return neighbors


def expand_cluster(attractions, labels, point_idx, cluster_id, eps, min_samples):
    neighbors = region_query(attractions, point_idx, eps)

    if len(neighbors) < min_samples:
        labels[point_idx] = -1  # mark as noise
        return False

    labels[point_idx] = cluster_id
    i = 0
    while i < len(neighbors):
        neighbor_idx = neighbors[i]
        if labels[neighbor_idx] == -1:
            labels[neighbor_idx] = cluster_id  # change noise to border point
        elif labels[neighbor_idx] is None:
            labels[neighbor_idx] = cluster_id
            new_neighbors = region_query(attractions, neighbor_idx, eps)
            if len(new_neighbors) >= min_samples:
                neighbors.extend(new_neighbors)
        i += 1
    return True


def dbscan(attractions, eps=50, min_samples=1):
    labels = [None] * len(attractions)
    cluster_id = 0

    for i in range(len(attractions)):
        if labels[i] is not None:
            continue
        if expand_cluster(attractions, labels, i, cluster_id, eps, min_samples):
            cluster_id += 1

    # Build list of clusters using labels
    clusters = {}
    for idx, label in enumerate(labels):
        if label == -1:
            continue  # skip noise if desired
        clusters.setdefault(label, []).append(attractions[idx])
    return list(clusters.values())
