import sqlite3

CONNECTION = sqlite3.connect("./orm.db")
CURSOR = CONNECTION.cursor()


class Pet:
    def __init__(
        self, name: str, species: str, breed: str, temperament: str, id=None
    ) -> None:
        self.id = id
        self.name = name
        self.species = species
        self.temperament = temperament

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

    def drop_table():
        sql = """
          DROP TABLE IF EXISTS pets
        """
        res = CURSOR.execute(sql)
        return res


# Pet.create_table
print(Pet.__base__)
