from gtts import gTTS
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from ttkthemes import ThemedTk

# Manually define a list of available voices
available_voices = ["en", "es", "fr", "de", "it"]
vocals = ["English - Emily", "Spanish - Maria", "French - Adele", "German - Lina", "Italian - Isabella"]

# Function to display available voices
def show_available_voices():
    available_voices_str = "\n".join(vocals)
    tk.messagebox.showinfo("Available Voices", available_voices_str)

def text_to_speech():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

    if file_path:
        # Read the text from the selected file
        with open(file_path, 'r') as file:
            text = file.read()

        # Voice (language) selection
        voice = voice_var.get().split(" - ")[0]

        # Create a progress bar
        progress_bar = ttk.Progressbar(root, length=200, mode='indeterminate')
        progress_bar.pack(pady=10)
        progress_bar.start()

        # Saving the converted audio in a file
        tts = gTTS(text=text, lang=voice, slow=False)
        tts.save("output.mp3")

        # Stop the progress bar
        progress_bar.stop()
        progress_bar.pack_forget()

        # Playing the converted file
        os.system("mpg123 output.mp3")  # You may need to install 'mpg123' if not already installed

        # Display the text with highlighted letters
        text_widget.delete('1.0', tk.END)  # Clear previous text
        text_widget.insert('1.0', text)

        # Enable the "Play Again" button
        play_again_button["state"] = "normal"

def play_again():
    # Playing the converted file again
    os.system("mpg123 output.mp3")

# Create the main window with the "Equilux" theme
root = ThemedTk(theme="equilux")

root.title("Text to Speech Converter")

# Create a frame for voice (language) selection
voice_frame = ttk.Frame(root)
voice_frame.pack(pady=10)

# Voice (language) selection label and dropdown
voice_label = ttk.Label(voice_frame, text="Select Voice:")
voice_label.pack(side=tk.LEFT)
voice_var = tk.StringVar()

# Create a button to show available voices
show_voices_button = ttk.Button(voice_frame, text="Show Available Voices", command=show_available_voices)
show_voices_button.pack(side=tk.LEFT)

# OptionMenu for voice (language) selection
voice_dropdown = ttk.Combobox(voice_frame, textvariable=voice_var, values=vocals, state="readonly")
voice_dropdown.pack(side=tk.LEFT)

# Create a button to select the text file
select_button = ttk.Button(root, text="Select Text File", command=text_to_speech)
select_button.pack(pady=10)

# Create a "Play Again" button
play_again_button = ttk.Button(root, text="Play Again", command=play_again, state="disabled")
play_again_button.pack(pady=10)

# Create a text widget to display the text with highlighted letters
text_widget = tk.Text(root, wrap=tk.WORD, height=10, width=40)
text_widget.pack()

# Run the GUI application
root.geometry("400x400")
root.mainloop()
