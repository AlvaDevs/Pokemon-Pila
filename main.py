# Implementación de una pila para guardar objetos Pokémon
class PilaPokemones:
    def __init__(self):
        self.stack = []  # Inicialmente la pila está vacía

    def apilar_pokemon(self, pokemon):
        # Apila un Pokémon (lo agrega a la parte superior de la pila)
        self.stack.append(pokemon)
        print(f"{pokemon} ha sido añadido a la pila.")

    def desapilar_pokemon(self):
        # Desapila un Pokémon (elimina y devuelve el Pokémon en la parte superior)
        if self.stack:
            pokemon = self.stack.pop()
            print(f"{pokemon} ha sido removido de la pila.")
            return pokemon
        else:
            print("La pila está vacía.")
            return None

    def mostrar_pila(self):
        # Muestra el contenido de la pila
        if not self.stack:
            print("La pila está vacía.")
        else:
            print("Pokémon en la pila:")
            for pokemon in reversed(self.stack):
                print(f"- {pokemon}")


# Programa principal
if __name__ == "__main__":
    pila_pokemones = PilaPokemones()

    # Apilando Pokémon
    pila_pokemones.apilar_pokemon("Sprigatito")
    pila_pokemones.apilar_pokemon("Fuecoco")
    pila_pokemones.apilar_pokemon("Quaxly")

    # Mostrando la pila actual
    pila_pokemones.mostrar_pila()

    # Desapilando Pokémon
    pila_pokemones.desapilar_pokemon()
    pila_pokemones.desapilar_pokemon()

    # Mostrando la pila después de desapilar
    pila_pokemones.mostrar_pila()
