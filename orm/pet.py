import sqlite3


CONNECTION = sqlite3.connect("./orm.db")
CURSOR = CONNECTION.cursor()


class PetType(Enum):
    dog = 1
    cat = 2
    rodent = 3
    bird = 4
    reptile = 5
    exotic = 6


class Pet:
    PET_TYPES = Enum("Pet_Type", ["dog", "cat", "rodent", "bird", "reptile", "exotic"])
    x = PET_TYPES.cat

    def __init__(
        self, name: str, pet_type: PetType, breed: str, temperament: str, id=None
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


lulu = Pet(
    "lulu",
    1,
)
# Pet.create_table
print(Pet.__base__)
