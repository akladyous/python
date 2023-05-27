from typing import List, Tuple, Dict

empty_user = {
    "id": None,
    "name": None,
    "username": None,
    "email": None,
    "address": {
        "street": None,
        "suite": None,
        "city": None,
        "zipcode": None,
        "geo": {"lat": None, "lng": None},
    },
    "phone": None,
    "website": None,
    "company": {
        "name": None,
        "catchPhrase": None,
        "bs": None,
    },
}


user = {
    "id": 1,
    "name": "John Doe",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {"lat": "-37.3159", "lng": "81.1496"},
    },
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org",
    "company": {
        "name": "Romaguera-Crona",
        "catchPhrase": "Multi-layered client-server neural-net",
        "bs": "harness real-time e-markets",
    },
}
# current_user = input("insert user name : ")
current_user = "John Doe"
if current_user == user.get("name", None):
    print("Welcome  {} ".format(current_user))
else:
    print("({}) doesn't exists!".format(current_user))


def dict_keys_white_list(obj: dict[str, any], white_list: list = []) -> dict[str, any]:
    filtered = []
    for k in obj.keys():
        if k in white_list:
            filtered.append(k)
    return filtered


print("-" * 50)
print(dict_keys_white_list(user, ["name", "email"]))
