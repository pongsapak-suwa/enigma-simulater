import pygame

from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma
from draw import draw

pygame.init()
pygame.font.init()
pygame.display.set_caption("Enigma simulator")

MONO = pygame.font.SysFont("FreeMono", 20)
BOLD = pygame.font.SysFont("FreeMono", 20, bold=True)

WIDTH = 1280
HEIGHT = 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
MARGINS = {"top":160, "bottom":160, "left":80, "right":80}
GAP = 100
PATH = []

INPUT = ""
OUTPUT = ""

I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")
KB = Keyboard() 
PB = Plugboard (["AR", "GK", "OX"])

ENIGMA = Enigma(A,I,II,III,PB,KB)
ENIGMA.set_rings((1,1,1))
ENIGMA.set_key("DOG")

"""
mass = "TEST"
cipher_text = ""
for letter in mass:
    cipher_text = cipher_text + ENIGMA.encipher(letter)
print(cipher_text)
"""
# print(ENIGMA.encipher("A"))

animating = True
while animating:
    SCREEN.fill("#333333")

    text = BOLD.render(INPUT, True, "white")
    text_box = text.get_rect(center = (WIDTH/2 ,MARGINS["top"]/2))
    SCREEN.blit(text, text_box)

    text = MONO.render(OUTPUT, True, "white")
    text_box = text.get_rect(center = (WIDTH/2 ,MARGINS["top"]/2+20))
    SCREEN.blit(text, text_box)

    draw(ENIGMA, PATH, SCREEN, WIDTH, HEIGHT, MARGINS, GAP, BOLD)
    
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                II.rotate()
            else:
                key = event.unicode
                if key in "abcdefghijklmnopqrstuvwxyz":
                    letter = key.upper()
                    INPUT = INPUT + letter
                    PATH, cipher = ENIGMA.encipher(letter)
                    OUTPUT = OUTPUT + cipher
