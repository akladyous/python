
def groups_per_user(group_dictionary):
    user_groups = {}
    for key, group in group_dictionary.items():
        for user in group:
            if not user in user_groups:
                user_groups[user]=[]
                user_groups[user].append(key)
            else:
                user_groups[user].append(key)
    return(user_groups)

print(groups_per_user({ "local": ["admin", "userA"],
		                "public":  ["admin", "userB"],
		                "administrator": ["admin"],
                        "network": ["admin", "userB"]}))


