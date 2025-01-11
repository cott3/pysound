#pysound 0.2 beta build
#VERY barebones, dont expect too much
#by cott122

#libs, inits, variables and other stuff
from tkinter import ttk
import pygame
import tkinter as tk

pygame.init()
pygame.mixer.init()

current_sound = None
is_playing = False

#

#defining functions
def play_stop_sound():
    global current_sound, is_playing
    selected_sound = sound_listbox.get(tk.ACTIVE)

    if is_playing:
        current_sound.stop()
        current_sound = None
        is_playing = False
        status_label.config(text="Stopped")
    else:
        current_sound = pygame.mixer.Sound(selected_sound)
        current_sound.play()
        is_playing = True
        status_label.config(text=f"Playing: {selected_sound}")

def load_sounds():
    with open("sounds.txt", "r") as f:
        sound_files = f.readlines()
        for sound_file in sound_files:
            sound_file = sound_file.strip()
            sound_listbox.insert(tk.END, sound_file)
#

#gui stuff

window = tk.Tk()
window.title("pysound")
window.geometry("300x300")  


style = ttk.Style()
style.theme_use("clam") 
style.configure("TButton", padding=10, font=("Arial", 12))


sound_listbox = tk.Listbox(window, width=30, height=10)
sound_listbox.pack(pady=10)


status_label = tk.Label(window, text="", font=("Arial", 10))
status_label.pack(pady=5)


play_pause_button = ttk.Button(window, text="Play/Stop", command=play_stop_sound)
play_pause_button.pack(pady=5)


button_frame = tk.Frame(window)
button_frame.pack()


#you'll never guess what this does
load_sounds()
#

window.mainloop()