from models.pokemon_model import Pokemon
from sqlalchemy.orm import Session

class PokemonRepository:
    """
    Repositorio para la gestión de Pokémon en la base de datos.
    Proporciona métodos para crear, consultar, actualizar y eliminar Pokémon,
    permitiendo así administrar de forma estructurada la información de estos.
    """

    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all_pokemons(self):
        """
        Recupera todos los Pokémon almacenados en la base de datos.
        Utiliza una consulta ORM para obtener todas las instancias de la clase Pokemon,
        permitiendo listar todos los Pokémon registrados en el sistema.
        Es útil para mostrar catálogos, listados generales o para operaciones que
        requieran acceder a la colección completa de Pokémon.
        """
        return self.db.query(Pokemon).all()

    def get_pokemon_by_id(self, pokemon_id: int):
        """
        Busca y retorna un Pokémon específico según su identificador único (ID).
        Realiza una consulta filtrando por el campo 'id' de la tabla Pokemon.
        Devuelve la instancia de Pokemon si existe, o None si no se encuentra.
        Es útil para obtener detalles de un Pokémon concreto.
        """
        return self.db.query(Pokemon).filter(Pokemon.id == pokemon_id).first()

    def create_pokemon(self, name: str, type_: str, generation: int):
        """
        Crea y almacena un nuevo Pokémon en la base de datos.
        Recibe el nombre, tipo y generación como parámetros, instancia un nuevo objeto Pokemon
        y lo agrega a la sesión de la base de datos. Tras confirmar la transacción,
        retorna el nuevo Pokémon creado, incluyendo su ID asignado automáticamente.
        Es útil para registrar nuevos Pokémon en el sistema.
        """
        new_pokemon = Pokemon(name=name, type=type_, generation=generation)
        self.db.add(new_pokemon)
        self.db.commit()
        self.db.refresh(new_pokemon)
        return new_pokemon

    def update_pokemon(self, pokemon_id: int, name: str = None, type_: str = None, generation: int = None):
        """
        Actualiza la información de un Pokémon existente en la base de datos.
        Permite modificar el nombre, tipo y generación del Pokémon identificado por su ID.
        Si el Pokémon existe y se proporcionan nuevos valores, se actualiza el registro
        y se guarda el cambio en la base de datos.
        Devuelve la instancia del Pokémon actualizado o None si no se encuentra.
        Es útil para mantener actualizada la información de los Pokémon.
        """
        pokemon = self.get_pokemon_by_id(pokemon_id)
        if pokemon:
            if name:
                pokemon.name = name
            if type_:
                pokemon.type = type_
            if generation is not None:
                pokemon.generation = generation
            self.db.commit()
            self.db.refresh(pokemon)
        return pokemon

    def delete_pokemon(self, pokemon_id: int):
        """
        Elimina un Pokémon de la base de datos según su identificador único (ID).
        Busca el Pokémon correspondiente y, si existe, lo elimina de la base de datos
        y confirma la transacción. Devuelve la instancia del Pokémon eliminado
        o None si no se encuentra.
        Es útil para operaciones administrativas o de mantenimiento donde se requiera
        remover Pokémon del sistema.
        """
        pokemon = self.get_pokemon_by_id(pokemon_id)
        if pokemon:
            self.db.delete(pokemon)
            self.db.commit()
        return pokemon
