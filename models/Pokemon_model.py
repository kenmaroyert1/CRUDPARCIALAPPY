# Importaciones de librerías:
# - sqlalchemy: Proporciona herramientas para trabajar con bases de datos relacionales en Python mediante ORM (Object Relational Mapping).
#   - Column, Integer, String: Permiten definir los tipos de columnas en los modelos de base de datos.
# - sqlalchemy.orm: Incluye utilidades para la declaración de modelos.
#   - declarative_base: Se utiliza para crear una clase base a partir de la cual se definen los modelos ORM.

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

"""
La clase Pokemon representa un Pokémon dentro del sistema. 
Cada instancia de esta clase corresponde a un Pokémon específico, 
almacenando información relevante como su nombre, tipo y generación. 
Esta clase está mapeada a la tabla 'pokemons' en la base de datos 
y permite gestionar la información de los Pokémon de forma estructurada.
"""
class Pokemon(Base):
    __tablename__ = 'pokemons'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    type = Column(String(100), nullable=False)
    generation = Column(Integer, nullable=False)
