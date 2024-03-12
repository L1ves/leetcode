def greet_developers(lst): 
    # your code here
    for greeting in lst:
        greeting["greeting"] = f"Hi {greeting['firstName']}, what do you like the most about {greeting['language']}?"
    return lst