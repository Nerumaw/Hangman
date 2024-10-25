import tkinter as tk
from tkinter.messagebox import showinfo
import random

root = tk.Tk()
root.title("Hangman")
root.geometry("800x600")

words = ["hangman", "python", "programming", "coding", "project", "challenge", "germany", "tribalism", ""]

secretWord = random.choice(words)
guessed = []
attempts = 6

def is_game_over():
    return checkWin() or checkLoss()

def checkWin():
    return all(letter in guessed for letter in secretWord)

def checkLoss():
    return attempts == 0

def on_button_enter_click():
    global attempts
    letter = letter_entry.get().lower()
    #check if only letters
    if letter.isalpha() and len(letter) == 1:
        if letter in guessed:
            showinfo("Hangman", f"You've already guessed {letter}!")
        elif letter in secretWord:
            guessed.append(letter)
            updateWordDisplay()
            if checkWin():
                showinfo("Hangman", "Congratulations! You win.")
                resetGame()
        else:
            guessed.append(letter)
            attempts -= 1
            updateAttemptsDisplay()
            drawHangman()
            if checkLoss():
                showinfo("Hangman", f"You lose! The word was {secretWord}.")
                resetGame()
        letter_entry.delete(0, tk.END)
    else:
        showinfo("Hangman", "Please enter a single letter.")

def resetGame():
    global secretWord, guessed, attempts
    secretWord = random.choice(words)
    guessed = []
    attempts = 6
    updateWordDisplay()
    updateAttemptsDisplay()
    drawHangman()

def updateAttemptsDisplay():
    attemptsLabel.config(text=f"Attempts left: {attempts}")

def updateWordDisplay():
    displayWord = ""
    for letter in secretWord:
        if letter in guessed:
            displayWord += letter
        else:
            displayWord += "_"
        displayWord += " "
    wordLabel.config(text=displayWord)

def drawHangman():
    canvas.delete("Hangman")
    if attempts < 6:
        canvas.create_oval(125, 125, 175, 175, width= 4, tags="Hangsman")
    if attempts < 5:
        canvas.create_line(150, 175, 150, 225, width= 4, tags="Hangsman")
    if attempts < 4:
        canvas.create_line(150, 200, 125, 175, width= 4, tags="Hangsman")
    if attempts < 3:
        canvas.create_line(150, 200, 175, 175, width= 4, tags="Hangsman")
    if attempts < 2:
        canvas.create_line(150, 225, 125, 250, width= 4, tags="Hangsman")
    if attempts < 1:
        canvas.create_line(150, 225, 175, 250, width= 4, tags="Hangsman")

wordLabel = tk.Label(root, text="")
attemptsLabel = tk.Label(root, text="")
letter_entry = tk.Entry(root, width=5)
buttonGuess = tk.Button(root, text="Guess", command=on_button_enter_click)
buttonReset = tk.Button(root, text="Reset", command=resetGame)
canvas = tk.Canvas(root, width=300, height=300)
canvas.create_line(50, 250, 250, 250, width= 4)
canvas.create_line(200, 250, 200, 100, width= 4)
canvas.create_line(100, 100, 200, 100, width= 4)
canvas.create_line(150, 100, 150, 120, width= 4)
canvas.pack()

wordLabel.pack()
attemptsLabel.pack()
letter_entry.pack()
buttonGuess.pack()
buttonReset.pack()

updateWordDisplay()
updateAttemptsDisplay()
drawHangman()

root.mainloop()