# Opdracht 1 functies
# Naam student: Rick van de Mars
# Groep:97031008


def write_to_file(afile, atext):
   with open(afile, "a") as file:
         file.write(atext + "\n")     
      

my_tekst = "Schrijf dit maar even in een bestandje"
my_file = "test.txt"
write_to_file(my_file, my_tekst)
