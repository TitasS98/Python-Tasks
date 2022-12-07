# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# wasExpensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False. 


class Movie:
    def __init__(self, title, direction, budget):
        self.title = title
        self.direction = direction
        self.budget = budget
        movie1 = Movie("Wednesday", "Alfred Gough" 162200000)
        movie2 = Movie("Matrica", "Lana Wachowski" 63000000)
    def wasExpensive(self, budget):
        if budget >= 100000000:     
            print(True)
            if not budget >= 100000000:
                print(False)
                

movie1.wasExpensive()
