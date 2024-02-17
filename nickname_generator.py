def nickname_generator(name):
    if str(name) and name.capitalize() and len(name) < 4:
        return "Error: Name too short"
    if name[2] not in 'euioa':
        return name[:3]
    else:
        return name[:4]