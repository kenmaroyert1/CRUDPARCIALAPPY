# Importaciones de librerías:
# - sqlalchemy: Proporciona herramientas para trabajar con bases de datos relacionales en Python mediante ORM (Object Relational Mapping).
#   - Column, Integer, String: Permiten definir los tipos de columnas en los modelos de base de datos.
# - sqlalchemy.orm: Incluye utilidades para la gestión de relaciones y la declaración de modelos.
#   - declarative_base: Se utiliza para crear una clase base a partir de la cual se definen los modelos ORM.

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

"""
La clase Pokemon representa un Pokémon dentro del sistema. 
Cada instancia de esta clase corresponde a un Pokémon específico,
almacenando sus atributos principales como nombre, tipos y estadísticas base.
Esta clase está mapeada a la tabla 'pokemons' en la base de datos y permite
gestionar toda la información de los Pokémon.
"""
class Pokemon(Base):
    __tablename__ = 'pokemons'
    
    id = Column(Integer, primary_key=True, index=True)   # #: ID para cada Pokémon
    name = Column(String(255), nullable=False)           # Nombre del Pokémon
    type_1 = Column(String(50), nullable=False)          # Tipo principal
    type_2 = Column(String(50))                          # Tipo secundario (opcional)
    total = Column(Integer, nullable=False)              # Suma de estadísticas
    hp = Column(Integer, nullable=False)                 # Puntos de vida
    attack = Column(Integer, nullable=False)             # Ataque físico
    defense = Column(Integer, nullable=False)            # Defensa física
    sp_atk = Column(Integer, nullable=False)             # Ataque especial
    sp_def = Column(Integer, nullable=False)             # Defensa especial
    speed = Column(Integer, nullable=False)              # Velocidad
