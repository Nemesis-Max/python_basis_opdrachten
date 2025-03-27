# Opdracht 1 functies
# Naam student: Rick van de Mars
# Groep: 97031008


def volledige_naam(lijst_met_namen):
    for naam in lijst_met_namen:
        if naam["tussenvoegsel"] == "":
            print(naam["voornaam"] + " " + naam["achternaam"])
        else:
            print(naam["voornaam"] + " " + naam["tussenvoegsel"] + " " + naam["achternaam"])



namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]

volledige_naam(namen)