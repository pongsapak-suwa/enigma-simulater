import pygame

def draw(enigma, path, screen, width, height, margins, gap, font):
    w = (width - margins["left"] - margins["right"] - 5*gap) / 6
    h = height - margins["top"] - margins["bottom"]

    y = [margins["top"]+(signal+1)*h/27 for signal in path]
    x = [width-margins["right"] - w/2]
    for i in [4, 3, 2, 1, 0]:
        x.append(margins["left"]+i*(w+gap)+w*3/4)
        x.append(margins["left"]+i*(w+gap)+w*1/4)
    x.append(margins["left"]+i*(w+gap)+w*3/4)

    for i in [1, 2, 3, 4]:
        x.append(margins["left"]+i*(w+gap)+w*1/4)
        x.append(margins["left"]+i*(w+gap)+w*3/4)
    x.append([width-margins["right"] - w/2])

    if len(path) > 0:
        for i in range(1, 20):
            color = "#43aa8b" if i < 12 else "#e63946"
            start = (x[i-1],y[i-1])
            end = (x[i],y[i])
            pygame.draw.line(screen, color, start, end, width=4)
    
    x = margins["left"]
    y = margins["top"]
    y2 = margins["top"]*0.9
    i = 0
    names = ["Reflector", "Left", "Middle", "Right", "Plugboard", "Key/Lamp"]

    for component in [enigma.re, enigma.r1, enigma.r2, enigma.r3, enigma.pb, enigma.kb]:
        component.draw(screen, x, y, w, h, font)

        x2 = x + w/2
        title = font.render(names[i], True, "yellow")
        text_box = title.get_rect(center = (x2,y2))
        screen.blit(title, text_box)
        x += w +gap
        i += 1

