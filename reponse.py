#Exercice1#
import math
from abc import ABC, abstractmethod
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

# Classe Circle dérivée de Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


# Classe Rectangle dérivée de Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

#Exercice2
class BankAccount:
    def __init__(self, initial_balance):
        # Initialisation du solde avec un solde initial donné
        self.balance = initial_balance

    # Surcharge de l'opérateur += pour ajouter un montant
    def __add__(self, amount):
        self.balance += amount  # Ajoute le montant au solde
        return self

    # Surcharge de l'opérateur -= pour retirer un montant
    def __sub__(self, amount):
        self.balance -= amount  # Soustrait le montant du solde
        return self

#Exercice3
# Définition du décorateur
def check_positive(func):
    def wrapper(x):
        if x < 0:  # Vérifie si l'argument est négatif
            raise ValueError("Le nombre doit être positif")
        return func(x)  # Appelle la fonction originale si l'argument est positif
    return wrapper

# Fonction utilisant le décorateur @check_positive
@check_positive
def check_positive(x):
    return x * 2

#Exercice4
class Car:
    def __init__(self):
        # Attribut privé pour stocker la vitesse
        self._speed = 0

    # Getter pour lire la vitesse
    @property
    def speed(self):
        return self._speed

    # Setter pour modifier la vitesse
    @speed.setter
    def speed(self, value):
        if value <= 0 or value > 200:
            raise ValueError("La vitesse doit être entre 0 et 200 km/h")
        self._speed = value

#Exercice5
class AgeError(Exception):
    """Exception levée lorsque l'âge est invalide."""
    pass

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age  # Utilisation du setter pour valider l'âge

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0 or value > 150:
            raise AgeError("L'âge doit être entre 0 et 150 ans")
        self._age = value

#Exercice6
class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.entries = []  # Liste pour simuler la base de données
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):  # Pour éviter de réinitialiser l'instance
            self.initialized = True

    def remove_by_id(self, id):
        # Supprime une entrée par ID
        self.entries = [entry for entry in self.entries if entry['id'] != id]

    def drop_all(self):
        # Vide toutes les entrées
        self.entries.clear()

    def create_context(self):
        return DbContext(self)

class DbContext:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.temp_entries = []  # Stocke les entrées temporairement

    def add_entry(self, entry):
        self.temp_entries.append(entry)  # Ajoute l'entrée temporairement

    def flush(self):
        # Ajoute toutes les entrées temporaires à la base de données
        self.db_connection.entries.extend(self.temp_entries)
        self.temp_entries.clear()  # Vide les entrées temporaires

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.flush()  # Flush les entrées quand on quitte le contexte

#Exercice7

# Classe abstraite Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Classe Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# Classe Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Classe ShapeFactory
class ShapeFactory:
    @staticmethod
    def create(shape, **kwargs):  # Changement de shape_type à shape
        if shape == "circle":
            return Circle(kwargs.get('radius'))
        elif shape == "rectangle":
            return Rectangle(kwargs.get('width'), kwargs.get('height'))
        else:
            raise ValueError("Unknown shape type")

#Exercice9
class Matrix:
    def __init__(self, values):
        self.values = values  # Utiliser 'values' au lieu de 'data'
        self.rows = len(values)
        self.cols = len(values[0]) if values else 0

    def __add__(self, other):
        # Vérifie si les dimensions des matrices sont compatibles pour l'addition
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Les matrices doivent avoir les mêmes dimensions pour l'addition.")

        # Effectue l'addition
        result = [[self.values[i][j] + other.values[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __mul__(self, other):
        # Vérifie si les dimensions des matrices sont compatibles pour la multiplication
        if self.cols != other.rows:
            raise ValueError(
                "Le nombre de colonnes de la première matrice doit être égal au nombre de lignes de la seconde.")

        # Effectue la multiplication
        result = [[sum(self.values[i][k] * other.values[k][j] for k in range(self.cols)) for j in range(other.cols)]
                  for i in range(self.rows)]
        return Matrix(result)


#Exercice10
from abc import ABC, abstractmethod

# Classe abstraite Animal
class Animal(ABC):
    def __init__(self, name):
        self.name = name  # Attribut pour le nom de l'animal

    @abstractmethod
    def speak(self):
        pass

# Classe dérivée Dog
class Dog(Animal):
    def speak(self):
        return "Woof"

# Classe dérivée Cat
class Cat(Animal):
    def speak(self):
        return "Meow"

# Factory pour créer des instances d'Animal
class AnimalFactory:
    @staticmethod
    def create(animal_type, name):
        if animal_type.lower() == "dog":
            return Dog(name)
        elif animal_type.lower() == "cat":
            return Cat(name)
        else:
            raise ValueError("Animal type must be 'dog' or 'cat'.")

#Exercice12
class Account:
    def __init__(self, initial_balance=0):
        # Initialisation du solde à un montant donné (par défaut à 0)
        self._balance = initial_balance

    @property
    def balance(self):
        # Getter pour obtenir le solde
        return self._balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Le dépôt doit être positif")
        self._balance += amount  # Ajoute le montant au solde

    def withdraw(self, amount):
        if self._balance - amount < 0:
            raise ValueError("Solde insuffisant pour le retrait")
        self._balance -= amount  # Soustrait le montant du solde

#Exercice11
class Product:
    def __init__(self, name, price):
        self.name = name  # Nom du produit
        self.price = price  # Prix du produit

    # Surcharge de l'opérateur ==
    def __eq__(self, other):
        if isinstance(other, Product):
            return self.price == other.price
        return NotImplemented

    # Surcharge de l'opérateur <
    def __lt__(self, other):
        if isinstance(other, Product):
            return self.price < other.price
        return NotImplemented

    # Surcharge de l'opérateur >
    def __gt__(self, other):
        if isinstance(other, Product):
            return self.price > other.price
        return NotImplemented

    # Surcharge de l'opérateur <=
    def __le__(self, other):
        if isinstance(other, Product):
            return self.price <= other.price
        return NotImplemented

    # Surcharge de l'opérateur >=
    def __ge__(self, other):
        if isinstance(other, Product):
            return self.price >= other.price
        return NotImplemented

    # Surcharge de l'opérateur !=
    def __ne__(self, other):
        if isinstance(other, Product):
            return self.price != other.price
        return NotImplemented

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price})"


















