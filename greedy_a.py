stations = {
    'kone': {'id', 'nv', 'ut'},
    'ktwo': {'wa', 'id', 'mt'},
    'kthree': {'or', 'nv', 'ca'},
    'kfour': {'nv', 'ut'},
    'kfive': {'ca', 'az'},
}

states_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}

final_stations = set()

while states_needed:
    best_station = None
    best_station_states = set()
    for station, station_states in stations.items():
        states_covered = states_needed & station_states
        if states_covered > best_station_states:
            best_station = station
            best_station_states = station_states
    final_stations.add(best_station)
    states_needed -= best_station_states

print(final_stations)
