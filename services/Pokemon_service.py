from repositories.pokemon_repository import PokemonRepository
from models.pokemon_model import Pokemon
from sqlalchemy.orm import Session

"""
Librerías utilizadas:
- repositories.pokemon_repository: Proporciona la clase PokemonRepository para la gestión de Pokémon en la base de datos.
- models.pokemon_model: Define el modelo Pokemon que representa la entidad de un Pokémon.
- sqlalchemy.orm.Session: Permite manejar la sesión de la base de datos para realizar operaciones transaccionales.
"""

class PokemonService:
    """
    Capa de servicios para la gestión de Pokémon.
    Esta clase orquesta la lógica de negocio relacionada con los Pokémon,
    utilizando el repositorio para acceder a los datos.
    Permite mantener la lógica de negocio separada de la capa de acceso a datos y de la base de datos.
    """
    def __init__(self, db_session: Session):
        """
        Inicializa el servicio de Pokémon con una sesión de base de datos
        y un repositorio de Pokémon.
        """
        self.repository = PokemonRepository(db_session)

    def listar_pokemons(self):
        """
        Recupera y retorna todos los Pokémon registrados en el sistema.
        Utiliza el repositorio para obtener la lista completa de Pokémon.
        Es útil para mostrar catálogos o listados generales de Pokémon.
        """
        return self.repository.get_all_pokemons()

    def obtener_pokemon(self, pokemon_id: int):
        """
        Busca y retorna un Pokémon específico por su identificador único (ID).
        Utiliza el repositorio para acceder al Pokémon correspondiente.
        Es útil para mostrar detalles o realizar operaciones sobre un Pokémon concreto.
        """
        return self.repository.get_pokemon_by_id(pokemon_id)

    def crear_pokemon(self, name: str, type: str, generation: int):
        """
        Crea un nuevo Pokémon con el nombre, tipo y generación proporcionados.
        Utiliza el repositorio para almacenar el nuevo Pokémon en la base de datos.
        Es útil para registrar nuevos Pokémon en el sistema.
        """
        return self.repository.create_pokemon(name, type, generation)

    def actualizar_pokemon(self, pokemon_id: int, name: str = None, type: str = None, generation: int = None):
        """
        Actualiza la información de un Pokémon existente, permitiendo modificar su nombre,
        tipo o generación. Utiliza el repositorio para realizar la actualización en la base de datos.
        Es útil para mantener actualizada la información de los Pokémon.
        """
        return self.repository.update_pokemon(pokemon_id, name, type, generation)

    def eliminar_pokemon(self, pokemon_id: int):
        """
        Elimina un Pokémon del sistema según su identificador único (ID).
        Utiliza el repositorio para eliminar el Pokémon de la base de datos.
        Es útil para operaciones administrativas o de mantenimiento.
        """
        return self.repository.delete_pokemon(pokemon_id)
