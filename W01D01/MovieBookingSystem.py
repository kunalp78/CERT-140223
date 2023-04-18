# Create a python project which will enable to make a simple movie booking system
#  we will restrict ourselves to just booking the ticket and show ticket.
"""
    Functionalities: movie selection, add movie, 
    buy ticket(
        row and seat number, language, location, discount
        ), show movie timing,
    snack purchase, register user, login user, show ticket history
    Agenda:
    1) register
    2) login
    3) add show/movie
    4) book ticket
    5) show booked ticket history
    6) show all the movies
"""
import json
from json import JSONDecodeError
def register(user_json, user_id, name, password, age, email, phone): # user_json
    """
    returns True if registration is successful
    returns False if registration is unsuccessful
    
    {
    "user_id": <id>,
    "name": <name>,
    "password": <password>,
    "email": <email>,
    "phone": <phn>,
    "age": <age>,
    "booked shows": ["id1", "id2", "id3"]  # it will contain the history of the shows user booked
    }
    """
    d = {
        "user_id": user_id,
        "name": name,
        "password": password,
        "email": email,
        "phone": phone,
        "age": age,
        "booked shows": []
    }
    f = open(user_json, "r+")
    try:
        content = json.load(f) # it is a list
        if d not in content:
            content.append(d)
            f.seek(0)
            f.truncate()
            json.dump(content, f)
            f.close()
            return True
    except JSONDecodeError:
        l = []
        l.append(d)
        json.dump(l, f)
        f.close()
        return True
    f.close()
    return False

# print(register.__doc__)
register("user.json","5479", "Sanvi", "password", "20", "anvi07@gmail.com", "8745897965")
