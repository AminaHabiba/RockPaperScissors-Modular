# Game Logic
import random # Import Random Module
Choices=["Rock","Paper","Scissors"] # Choices for the game
# Game Scores and Move Tracking
userScore=0
computerScore=0
tieScore=0
movesPlayed=0
maxMoves=10
# These will be passed from the main file
labels={}
buttons=[]
# This function will receive labels and button objects from main.py
def set_gui(guiLabels, guiButtons):
    global labels, buttons
    labels=guiLabels
    buttons=guiButtons
def play(userChoice):
    global userScore, computerScore, tieScore, movesPlayed
    if movesPlayed >= maxMoves:
        return
    computerChoice = random.choice(Choices)
    movesPlayed += 1
# Updating Moves Count
    labels["moves"].config(text=f"Moves Played: {movesPlayed} / {maxMoves}")
# Determining Result
    if userChoice == computerChoice:
        result = "It is a tie 🤝"
        tieScore += 1
    elif (userChoice == "Rock" and computerChoice == "Scissors") or \
         (userChoice == "Paper" and computerChoice == "Rock") or \
         (userChoice == "Scissors" and computerChoice == "Paper"):
        result = "You are the winner 🎉"
        userScore += 1
    else:
        result = "You lost the level. Better luck for next time!"
        computerScore += 1
# Updating Labels
    labels["user"].config(text=f"You chose: {userChoice}")
    labels["computer"].config(text=f"Computer chose: {computerChoice}")
    labels["result"].config(text=result)
    labels["score"].config(text=f"Score ➤ You: {userScore} | Computer: {computerScore} | Ties: {tieScore}")
# After Final Move
    if movesPlayed == maxMoves:
        for btn in buttons:
            btn.config(state="disabled")
        if userScore > computerScore:
            finalResult = "Congratulations! You won the game 🎉!"
        elif computerScore > userScore:
            finalResult = "You lost the game. Better luck next time 😞!"
        else:
            finalResult = "It's a draw overall 🤝!"
        labels["final"].config(text=finalResult)
def reset():
    global userScore, computerScore, tieScore, movesPlayed
    userScore = computerScore = tieScore = movesPlayed = 0
    # Clearing Labels
    labels["user"].config(text="")
    labels["computer"].config(text="")
    labels["result"].config(text="")
    labels["score"].config(text="Score ➤ You: 0 | Computer: 0 | Ties: 0")
    labels["moves"].config(text=f"Moves Played: 0 / {maxMoves}")
    labels["final"].config(text="")
def restart():
    reset()
    for btn in buttons:
        btn.config(state="normal")
