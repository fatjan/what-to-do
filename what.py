import random

what_to_do = {
    "a": "Read a book.",
    "b": "Scroll through Instagram.",
    "c": "Scroll through LinkedIn.",
    "d": "Create an app.",
    "e": "Call your Mom.",
    "f": "Chat with a friend.",
}

bored = input("Are you bored? y/n : ")

if bored.lower() == "y":
    print("You should ... ")
    keys_list = list(what_to_do.keys())
    chosen_activity = random.choice(keys_list)
    print(what_to_do[chosen_activity])
