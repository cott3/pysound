#pysound 0.2 beta build
#VERY barebones, dont expect too much
#by cott122

#libs, inits, variables and other stuff
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

sound_listbox = tk.Listbox(window)
sound_listbox.pack()


status_label = tk.Label(window, text="")
status_label.pack()

play_pause_button = tk.Button(window, text="Play/Stop", command=play_stop_sound)
play_pause_button.pack()
#

#you'll never guess what this does
load_sounds()
#

window.mainloop()