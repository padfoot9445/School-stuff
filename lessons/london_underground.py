STATIONS = [
    "Brixton",
    "Stockwell",
    "Vauxhall",
    "Pimlico",
    "Victoria",
    "Green Park",
    "Oxford Circus",
    "Warren Street",
    "Euston",
    "King's Cross",
    "Highbury & Islington",
    "Finsbury Park",
    "Seven Sisters",
    "Tottenham Hale",
    "Blackhorse Road",
    "Walthamstow Central",
]
STATIONS_SET = set(STATIONS)
def get_station() -> str:
    """|returns station|"""
    __input = None
    while not __input in STATIONS_SET:
        __input = input()
    return __input
def calculate_stops(tst:list[str]):
    return abs(STATIONS.index(tst[0]) - STATIONS.index(tst[1]))