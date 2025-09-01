from flask import Blueprint, request, jsonify
from services.pokemon_service import PokemonService

# Importar la sesión de la base de datos desde config/database.py
from config.database import get_db_session

# Instancia global de servicio (en producción usar contexto de app o request)
service = PokemonService(get_db_session())

pokemon_bp = Blueprint('pokemon_bp', __name__)


@pokemon_bp.route('/pokemons', methods=['GET'])
def get_pokemons():
    """
    GET /pokemons
    Recupera y retorna todos los Pokémon registrados en el sistema.
    Utiliza la capa de servicios para obtener la lista completa de Pokémon.
    No recibe parámetros.
    Respuesta: JSON con la lista de Pokémon.
    """
    pokemons = service.listar_pokemons()
    return jsonify([
        {'id': p.id, 'name': p.name, 'type': p.type, 'generation': p.generation}
        for p in pokemons
    ]), 200


@pokemon_bp.route('/pokemons/<int:pokemon_id>', methods=['GET'])
def get_pokemon(pokemon_id):
    """
    GET /pokemons/<pokemon_id>
    Recupera la información de un Pokémon específico por su ID.
    Parámetros:
        pokemon_id (int): ID del Pokémon a consultar (en la URL).
    Respuesta: JSON con los datos del Pokémon o 404 si no existe.
    """
    pokemon = service.obtener_pokemon(pokemon_id)
    if pokemon:
        return jsonify({
            'id': pokemon.id,
            'name': pokemon.name,
            'type': pokemon.type,
            'generation': pokemon.generation
        }), 200
    return jsonify({'error': 'Pokémon no encontrado'}), 404


@pokemon_bp.route('/pokemons', methods=['POST'])
def create_pokemon():
    """
    POST /pokemons
    Crea un nuevo Pokémon.
    Parámetros esperados (JSON):
        name (str): Nombre del Pokémon.
        type (str): Tipo del Pokémon.
        generation (int): Generación a la que pertenece.
    Respuesta: JSON con los datos del Pokémon creado.
    """
    data = request.get_json()
    name = data.get('name')
    type_ = data.get('type')
    generation = data.get('generation')

    if not name or not type_ or generation is None:
        return jsonify({'error': 'Nombre, tipo y generación son obligatorios'}), 400

    pokemon = service.crear_pokemon(name, type_, generation)
    return jsonify({
        'id': pokemon.id,
        'name': pokemon.name,
        'type': pokemon.type,
        'generation': pokemon.generation
    }), 201


@pokemon_bp.route('/pokemons/<int:pokemon_id>', methods=['PUT'])
def update_pokemon(pokemon_id):
    """
    PUT /pokemons/<pokemon_id>
    Actualiza la información de un Pokémon existente.
    Parámetros:
        pokemon_id (int): ID del Pokémon a actualizar (en la URL).
        name (str): Nuevo nombre del Pokémon (en el cuerpo JSON).
        type (str): Nuevo tipo del Pokémon (en el cuerpo JSON).
        generation (int): Nueva generación del Pokémon (en el cuerpo JSON).
    Respuesta: JSON con los datos del Pokémon actualizado o error si no existe.
    """
    data = request.get_json()
    name = data.get('name')
    type_ = data.get('type')
    generation = data.get('generation')

    pokemon = service.actualizar_pokemon(pokemon_id, name, type_, generation)
    if pokemon:
        return jsonify({
            'id': pokemon.id,
            'name': pokemon.name,
            'type': pokemon.type,
            'generation': pokemon.generation
        }), 200
    return jsonify({'error': 'Pokémon no encontrado'}), 404


@pokemon_bp.route('/pokemons/<int:pokemon_id>', methods=['DELETE'])
def delete_pokemon(pokemon_id):
    """
    DELETE /pokemons/<pokemon_id>
    Elimina un Pokémon específico por su ID.
    Parámetros:
        pokemon_id (int): ID del Pokémon a eliminar (en la URL).
    Respuesta: JSON con mensaje de éxito o error si no existe.
    """
    pokemon = service.eliminar_pokemon(pokemon_id)
    if pokemon:
        return jsonify({'message': 'Pokémon eliminado'}), 200
    return jsonify({'error': 'Pokémon no encontrado'}), 404
