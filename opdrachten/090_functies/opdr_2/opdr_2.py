# Opdracht 1 functies
# Naam student: Rick van de Mars
# Groep: 97031008


def kilometers_naar_miles(km):
    return km * 0.621371192

def miles_naar_kilometers(miles):
    return miles * 1.609344

kilometers = 1223
miles = 867

print(f"{kilometers} kilometers = {kilometers_naar_miles(kilometers)}")
print(f"{miles} miles = {miles_naar_kilometers(miles)}")