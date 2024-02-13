def validate_pin(pin):
    if pin.isdigit() and len(pin) == 4 or pin.isdigit() and len(pin) == 6:
        return True
    else:
        return False

def validate_pin(pin):
    #return true or false
    if pin.isdigit():
        if len(pin) in (4,6):
            return True
        else:
            return False
    else:
        return False

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

