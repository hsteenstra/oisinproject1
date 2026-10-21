
import random
from pyscript import document

# DOG INFORMATION
dog_names = ["Buddy", "Luna", "Max", "Bella", "Charlie"]
dog_name = random.choice(dog_names)

# GAME VARIABLES
happiness = 0
hunger = 50
energy = 70
actions_taken = 0

# ACTIVITY JOURNAL
journal = []


# HELPER FUNCTION: UPDATE THE SCREEN
# You do not need to change this function!
def update_screen():
    document.getElementById("happiness").innerText = str(happiness)
    document.getElementById("hunger").innerText = str(hunger)
    document.getElementById("energy").innerText = str(energy)

    document.getElementById("happiness-bar").style.width = str(happiness) + "%"
    document.getElementById("hunger-bar").style.width = str(hunger) + "%"
    document.getElementById("energy-bar").style.width = str(energy) + "%"

    # Display hearts based on happiness
    hearts = ""
    for i in range(5):
        if happiness >= (i + 1) * 20:
            hearts = hearts + "♥ "
        else:
            hearts = hearts + "♡ "

    document.getElementById("hearts").innerText = hearts


# HELPER FUNCTION: ADD AN ENTRY TO THE JOURNAL
# You do not need to change this function!
def add_to_journal(icon, title, message):
    journal.append([icon, title, message])

    journal_html = ""

    for entry in journal[::-1]:
        journal_html += (
            '<div class="log-entry">'
            '<span>' + entry[0] + '</span>'
            '<div><b>' + entry[1] + '</b>'
            '<small>' + entry[2] + '</small></div></div>'
        )

    document.getElementById("journal-content").innerHTML = journal_html


# TODO 1: FEED THE DOG
def feed(event):
    global happiness, hunger, energy, actions_taken

    print("Time to feed " + dog_name + "!")

    # YOUR JOB:
    # 1. Subtract 20 from hunger.
    # 2. Add 10 to happiness.
    # 3. If hunger is below 0, set it to 0.
    # 4. If happiness is above 100, set it to 100.
    # 5. Add 1 to actions_taken.
    # 6. Update the screen using update_screen().
    # 7. Add a journal entry about feeding the dog.
    #
    # HINTS:
    # hunger = hunger - 20
    # happiness = happiness + 10
    # if hunger < 0:
    #     hunger = 0
    #
    # Example journal entry:
    # add_to_journal("🍖", "Fed the dog", "Your dog enjoyed a meal!")


# TODO 2: PLAY WITH THE DOG
def play(event):
    global happiness, hunger, energy, actions_taken

    print("Let's play!")

    # YOUR JOB:
    # 1. Add 15 to happiness.
    # 2. Add 10 to hunger.
    # 3. Subtract 20 from energy.
    # 4. Keep all three values between 0 and 100.
    # 5. Add 1 to actions_taken.
    # 6. Update the screen.
    # 7. Add a journal entry about playing.
    #
    # HINT:
    # If a value is above 100, set it to 100.
    # If a value is below 0, set it to 0.
    #
    # Example journal entry:
    # add_to_journal("🎾", "Played together", "Your dog had fun!")


# TODO 3: LET THE DOG REST
def rest(event):
    global happiness, hunger, energy, actions_taken

    print("Nap time!")

    # YOUR JOB:
    # 1. Add 25 to energy.
    # 2. Subtract 5 from hunger.
    # 3. Keep both values between 0 and 100.
    # 4. Add 1 to actions_taken.
    # 5. Update the screen.
    # 6. Add a journal entry about resting.
    #
    # HINT:
    # Use if statements to check whether values
    # are above 100 or below 0.
    #
    # Example journal entry:
    # add_to_journal("💤", "Time to rest", "Your dog took a nap!")


# TODO 4: CHECK THE DOG'S STATUS
def check_status():
    # YOUR JOB:
    # Use if, elif, and else.
    #
    # If hunger is greater than 70:
    #     Display "Your dog is hungry!"
    #
    # Otherwise, if energy is below 20:
    #     Display "Your dog is tired!"
    #
    # Otherwise:
    #     Display "Your dog is doing great!"
    #
    # HINT:
    # if hunger > 70:
    #     message = "Your dog is hungry!"
    # elif energy < 20:
    #     message = "Your dog is tired!"
    # else:
    #     message = "Your dog is doing great!"
    #
    # Display the message with:
    # document.getElementById("status-text").innerText = message


# TODO 5: A SURPRISE EVENT
def random_event():
    # YOUR JOB:
    # 1. Pick a random number from 1 to 3.
    # 2. If the number is 1, the dog finds a toy!
    # 3. If the number is 2, the dog gets a treat!
    # 4. Otherwise, the dog meets a new friend!
    #
    # HINT:
    # number = random.randint(1, 3)
    #
    # if number == 1:
    #     print("Your dog found a new toy!")
    # elif number == 2:
    #     print("Your dog got a treat!")
    # else:
    #     print("Your dog met a new friend!")
    #
    # BONUS:
    # Add 5 to happiness when a surprise happens!


# START THE GAME
document.getElementById("status-text").innerText = (
    dog_name + " is ready for an adventure!"
)

update_screen()

print("Welcome to Dog Adventure!")
print("Your dog's name is " + dog_name + "!")
print("Complete the TODOs to bring the game to life!")
