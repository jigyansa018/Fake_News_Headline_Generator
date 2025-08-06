# import the random module 
import random

# create subjects
subjects = [
    "Sidhant Mohapatra",
    "Rohit Sharma",
    "CM Mohan Majhi",
    "Rickshawwala from Puri",
    "A group of Monkeys"
]

# create actions
actions = [
    "is moving to Hollywood",
    "cancels Bhubaneswar concert",
    "dances with aliens",
    "sings with dolphins",
    "declares war on street food vendors"
]

# create places
places = [
    "at Puri Sea Beach",
    "in Bhubaneswar Ama Bus",
    "with Alan Walker",
    "alongside Shakti Kapoor",
    "during IPL Match"
]

# Starts the Headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)
    
    print(f"\nBREAKING NEWS: {subject} {action} {place}")

    user_input = input("\nDo you want Another Headline? (yes/no): ").strip().lower()
    if user_input == "no":
        # print good bye msg
        print("\nThanks for generating Headlines with me. Have a fun day!!")
        break

