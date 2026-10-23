capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested a list in a dictionary
# travle_log = {
#     "France": ["Paris", "Lille", "Marseille"],
#     "Germany": ["Berlin", "Hamburg", "Munich"]
# }

# Accessing the nested list
# print(travle_log["France"][1])

nested_list = ["A", "B", ["C", "D", "E"]]

print(nested_list[2][1])  # Output: D

travle_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Marseille"],
        "total_visits": 4
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Munich"],
        "total_visits": 3
    }
}

print(travle_log["Germany"]["cities_visited"][2])  # Output: Munich
