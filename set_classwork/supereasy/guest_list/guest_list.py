def add_guest(guests, name):
    if name in guests:
        return False
    else:
        guests.add(name)
        return True

def remove_guest(guests, name):
    if name in guests:
        guests.remove(name)
        return True
    else:
        return False
