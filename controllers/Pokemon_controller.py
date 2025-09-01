from flask import Blueprint, request, jsonify
from services.Pokemon_service import PokemonService

# Definir el Blueprint
pokemon_bp = Blueprint('pokemon_bp', __name__)

# Importar la sesión de la base de datos desde config/database.py
from config.database import get_db_session

# Instancia global del servicio
service = PokemonService(get_db_session())


@pokemon_bp.route('/pokemons', methods=['GET'])
def get_pokemons():
    """
    GET /pokemons
    Recupera y retorna todos los Pokémon registrados en el sistema.
    """
    pokemons = service.listar_pokemones()
    return jsonify([
        {
            'id': p.id,
            'name': p.name,
            'type1': p.type1,
            'type2': p.type2,
            'total': p.total,
            'hp': p.hp,
            'attack': p.attack,
            'defense': p.defense,
            'sp_atk': p.sp_atk,
            'sp_def': p.sp_def,
            'speed': p.speed
        }
        for p in pokemons
    ]), 200


@pokemon_bp.route('/pokemons/<int:pokemon_id>', methods=['GET'])
def get_pokemon(pokemon_id):
    """
    GET /pokemons/<pokemon_id>
    Recupera la información de un Pokémon específico por su ID.
    """
    pokemon = service.obtener_pokemon(pokemon_id)
    if pokemon:
        return jsonify({
            'id': pokemon.id,
            'name': pokemon.name,
            'type1': pokemon.type1,
            'type2': pokemon.type2,
            'total': pokemon.total,
            'hp': pokemon.hp,
            'attack': pokemon.attack,
            'defense': pokemon.defense,
            'sp_atk': pokemon.sp_atk,
            'sp_def': pokemon.sp_def,
            'speed': pokemon.speed
        }), 200
    return jsonify({'error': 'Pokémon no encontrado'}), 404


@pokemon_bp.route('/pokemons', methods=['POST'])
def create_pokemon():
    """
    POST /pokemons
    Crea un nuevo Pokémon.
    Parámetros esperados (JSON): name, type1, type2, total, hp, attack, defense, sp_atk, sp_def, speed
    """
    data = request.get_json()
    name = data.get('name')
    type1 = data.get('type1')
    type2 = data.get('type2')
    total = data.get('total')
    hp = data.get('hp')
    attack = data.get('attack')
    defense = data.get('defense')
    sp_atk = data.get('sp_atk')
    sp_def = data.get('sp_def')
    speed = data.get('speed')

    if not name or not type1 or hp is None or attack is None:
        return jsonify({'error': 'Faltan datos obligatorios'}), 400

    pokemon = service.crear_pokemon(name, type1, type2, total, hp, attack, defense, sp_atk, sp_def, speed)
    return jsonify({
        'id': pokemon.id,
        'name': pokemon.name,
        'type1': pokemon.type1,
        'type2': pokemon.type2,
        'total': pokemon.total,
        'hp': pokemon.hp,
        'attack': pokemon.attack,
        'defense': pokemon.defense,
        'sp_atk': pokemon.sp_atk,
        'sp_def': pokemon.sp_def,
        'speed': pokemon.speed
    }), 201


@pokemon_bp.route('/pokemons/<int:pokemon_id>', methods=['PUT'])
def update_pokemon(pokemon_id):
    """
    PUT /pokemons/<pokemon_id>
    Actualiza la información de un Pokémon existente.
    """
    data = request.get_json()
    pokemon = service.actualizar_pokemon(
        pokemon_id,
        data.get('name'),
        data.get('type1'),
        data.get('type2'),
        data.get('total'),
        data.get('hp'),
        data.get('attack'),
        data.get('defense'),
        data.get('sp_atk'),
        data.get('sp_def'),
        data.get('speed')
    )
    if pokemon:
        return jsonify({
            'id': pokemon.id,
            'name': pokemon.name,
            'type1': pokemon.type1,
            'type2': pokemon.type2,
            'total': pokemon.total,
            'hp': pokemon.hp,
            'attack': pokemon.attack,
            'defense': pokemon.defense,
            'sp_atk': pokemon.sp_atk,
            'sp_def': pokemon.sp_def,
            'speed': pokemon.speed
        }), 200
    return jsonify({'error': 'Pokémon no encontrado'}), 404


@pokemon_bp.route('/pokemons/<int:pokemon_id>', methods=['DELETE'])
def delete_pokemon(pokemon_id):
    """
    DELETE /pokemons/<pokemon_id>
    Elimina un Pokémon específico por su ID.
    """
    pokemon = service.eliminar_pokemon(pokemon_id)
    if pokemon:
        return jsonify({'message': 'Pokémon eliminado'}), 200
    return jsonify({'error': 'Pokémon no encontrado'}), 404
