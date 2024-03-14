def get_first_python(users):
    # for i in users:
    #     if i["language"] == 'Python':
    #         return f"{i['first_name']}, {i['country']}"
    # return f"There will be no Python developers"

    return next((f"{i['first_name']}, {i['country']}" for i in users if i["language"] == 'Python'), "There will be no Python developers")