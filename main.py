import tkinter as tk
import GameLogic    # Importing Custom Module
root=tk.Tk()
root.title("Rock, Paper, Scissors Game🎮")
root.geometry("430x400")
root.config(bg="white")
# Heading
tk.Label(root, text="Rock✊, Paper🖐, Scissors✌ Game", font=("Arial", 16, "bold"), bg="white").pack(pady=10)
# Buttons to play
buttonFrame=tk.Frame(root,bg="white")
buttonFrame.pack()
rockBtn=tk.Button(buttonFrame, text="Rock", width=10, font=("Arial", 12), command=lambda: GameLogic.play("Rock"))
paperBtn=tk.Button(buttonFrame, text="Paper", width=10, font=("Arial", 12), command=lambda: GameLogic.play("Paper"))
scissorsBtn=tk.Button(buttonFrame, text="Scissors", width=10, font=("Arial", 12), command=lambda: GameLogic.play("Scissors"))
rockBtn.grid(row=0, column=0, padx=5)
paperBtn.grid(row=0, column=1, padx=5)
scissorsBtn.grid(row=0, column=2, padx=5)
# Labels to display Game Information
userLabel=tk.Label(root, text="", font=("Arial", 12), bg="white")
userLabel.pack()
computerLabel=tk.Label(root, text="", font=("Arial", 12), bg="white")
computerLabel.pack()
resultLabel=tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue", bg="white")
resultLabel.pack(pady=10)
scoreLabel = tk.Label(root, text="Score ➤ You: 0 | Computer: 0 | Ties: 0", font=("Arial", 12), bg="white")
scoreLabel.pack()
finalResultLabel = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="green", bg="white")
finalResultLabel.pack()
movesLabel = tk.Label(root, text="Moves Played: 0 / 10", font=("Arial", 12), bg="white")
movesLabel.pack()
# Passing Labels and Buttons to GameLogic
GameLogic.set_gui(
    {
    "user":userLabel,
    "computer": computerLabel,
    "result": resultLabel,
    "score": scoreLabel,
    "final": finalResultLabel,
    "moves": movesLabel
    },
    [rockBtn, paperBtn, scissorsBtn])
# Control Buttons
controlFrame = tk.Frame(root, bg="white")
controlFrame.pack(pady=10)
tk.Button(controlFrame, text="Restart Game", font=("Arial", 12), command=GameLogic.restart).grid(row=0, column=0, padx=10)
tk.Button(controlFrame, text="Reset Scores", font=("Arial", 12), command=GameLogic.reset).grid(row=0, column=1, padx=10)
root.mainloop()