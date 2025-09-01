from models.pokemon_model import Pokemon, Trainer
from sqlalchemy.orm import Session

class PokemonRepository:
    """
    Repositorio para la gestión de Pokémon en la base de datos.
    Proporciona métodos para crear, consultar, actualizar y eliminar Pokémon,
    así como para interactuar con los entrenadores asociados.
    """

    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all_pokemons(self):
        """
        Recupera todos los Pokémon almacenados en la base de datos.
        Utiliza una consulta ORM para obtener todas las instancias de la clase Pokemon,
        permitiendo listar todos los Pokémon registrados en el sistema.
        """
        return self.db.query(Pokemon).all()

    def get_pokemon_by_id(self, pokemon_id: int):
        """
        Busca y retorna un Pokémon específico según su identificador único (ID).
        Realiza una consulta filtrando por el campo 'id' de la tabla Pokemon.
        Devuelve la instancia de Pokemon si existe, o None si no se encuentra.
        """
        return self.db.query(Pokemon).filter(Pokemon.id == pokemon_id).first()

    def create_pokemon(self, name: str, type: str, level: int = 1, trainer_id: int = None):
        """
        Crea y almacena un nuevo Pokémon en la base de datos.
        Recibe el nombre, tipo, nivel (por defecto 1) y opcionalmente el id de un entrenador.
        Retorna la nueva instancia creada con su ID asignado automáticamente.
        """
        new_pokemon = Pokemon(name=name, type=type, level=level, trainer_id=trainer_id)
        self.db.add(new_pokemon)
        self.db.commit()
        self.db.refresh(new_pokemon)
        return new_pokemon

    def update_pokemon(self, pokemon_id: int, name: str = None, type: str = None, level: int = None):
        """
        Actualiza la información de un Pokémon existente en la base de datos.
        Permite modificar el nombre, tipo o nivel del Pokémon identificado por su ID.
        Devuelve la instancia del Pokémon actualizada o None si no se encuentra.
        """
        pokemon = self.get_pokemon_by_id(pokemon_id)
        if pokemon:
            if name:
                pokemon.name = name
            if type:
                pokemon.type = type
            if level:
                pokemon.level = level
            self.db.commit()
            self.db.refresh(pokemon)
        return pokemon

    def delete_pokemon(self, pokemon_id: int):
        """
        Elimina un Pokémon de la base de datos según su identificador único (ID).
        Si existe, lo elimina y confirma la transacción.
        Devuelve la instancia del Pokémon eliminado o None si no se encuentra.
        """
        pokemon = self.get_pokemon_by_id(pokemon_id)
        if pokemon:
            self.db.delete(pokemon)
            self.db.commit()
        return pokemon
