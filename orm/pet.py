import sqlite3

CONNECTION = sqlite3.connect("./orm.db")
CURSOR = CONNECTION.cursor()


class Pet:
    all: list["Pet"] = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(
        self: object, name: str, species: str, temperament: str, id: str = None
    ) -> None:
        self.name = name
        self.species = species
        self.temperament = temperament
        self.id = id
        Pet.all.append(self)

    @classmethod
    def create_table():
        sql = """
        CREATE TABLE IF NOT EXISTS pets
        (id INTEGER PRIMARY KEY,
        name TEXT,
        species TEXT,
        breed TEXT,
        temperament TEXT)
      """
        res = CURSOR.execute(sql)
        return res

    @classmethod
    def drop_table() -> None:
        sql = """DROP TABLE IF EXISTS pets;"""
        res = CURSOR.execute(sql)


pet1 = Pet(
    "pet one",
    "dog",
)
