#pysound 0.1 beta build
#VERY barebones, dont expect too much
#by cott122


#import libraries
import pygame
import tkinter as tk    
#

#init stuff
pygame.init()
pygame.mixer.init()
#

#stop func

def stop_sound():
    pygame.mixer.stop()
#

#import sounds
sound1 = pygame.mixer.Sound("sounds/sound1.mp3")
sound2 = pygame.mixer.Sound("sounds/sound2.mp3")
# ... and so on for more sounds
#



#gui stuff
window = tk.Tk()
window.title("pysound")


button1 = tk.Button(window, text="Sound 1", command=sound1.play)
button1.pack()

button2 = tk.Button(window, text="Sound 2", command=sound2.play)
button2.pack()


stop_button = tk.Button(window, text="Stop", command=stop_sound)
stop_button.pack()

window.mainloop()
#
