import requests
import tkinter as tk
from tkinter import ttk

# Function to fetch and display a random joke
def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    
    if response.status_code == 200:
        joke = response.json()
        joke_text = f"{joke['setup']}\n\n{joke['punchline']}"
    else:
        joke_text = "Couldn't retrieve a joke at the moment. Try again later."
    
    # Update the joke text in the label
    joke_label.config(text=joke_text)

# Initialize the main Tkinter window
app = tk.Tk()
app.title("Random Joke Generator")
app.geometry("500x300")
app.configure(bg="#f5f5f5")  # Light background color for better appearance

# Title label
title_label = tk.Label(app, text="Enjoy a Random Joke!", font=("Helvetica", 18, "bold"), fg="#4b8bbe", bg="#f5f5f5")
title_label.pack(pady=10)

# Label to display the joke
joke_label = tk.Label(app, text="", wraplength=450, font=("Arial", 12), fg="#333333", bg="#f5f5f5", justify="center")
joke_label.pack(padx=20, pady=20)

# Fetch the first joke initially
get_random_joke()

# "Next Joke" button
next_joke_button = ttk.Button(app, text="Next Joke", command=get_random_joke, style="TButton")
next_joke_button.pack(pady=10)

# Apply a style to make the button visually appealing
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=6)

# Run the main event loop
app.mainloop()
