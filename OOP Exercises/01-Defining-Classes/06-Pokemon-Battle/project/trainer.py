from project.pokemon import Pokemon


class Trainer:
    pokemon = []

    def __init__(self, name):
        self.name = name

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemon:
            return "This pokemon is already caught"
        self.pokemon.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name):
        for pokemon in self.pokemon:
            if pokemon.name == pokemon_name:
                self.pokemon.remove(pokemon)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        pokemons_caught = ""
        for el in self.pokemon:
            pokemons_caught += "- " + el.pokemon_details() + "\n"
        return f"Pokemon Trainer {self.name} \n " \
               f"Pokemon Count {len(self.pokemon)} \n" \
               f"{pokemons_caught}"
