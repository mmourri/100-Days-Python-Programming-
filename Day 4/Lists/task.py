state1 = "Alabama"
state2 = "California"

states_of_america = [state1, state2, "Delaware", "Pennsylvania"]
print(states_of_america)
print(states_of_america[0])

states_of_america[1] = "New York"
print(states_of_america)

states_of_america.append("Illinois")
print(states_of_america)

states_of_america.extend(["Indiana", "New Jersey", "Michigan"])
print(states_of_america)
