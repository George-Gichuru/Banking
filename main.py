import random

last_picked = None

def pick_random():
    global last_picked
    
    numbers = [1, 2, 3, 4, 5]

    if numbers is not None:
        numbers.remove(last_picked)

    picked = random.choice(numbers)
    last_picked = picked
    return picked
        
