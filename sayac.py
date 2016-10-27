import datetime
import pygame
from pygame.locals import *
from datetime import date
while True:
    today = datetime.date.today()
    now = datetime.datetime.now()
    todayDay = now.day
    todayMonth = now.month
    todayYear = now.year
    todayMonthString = "x"
    months = [(1, "January"), (2, "February"), (3, "March"), (4, "April"), (5, "May"), (6, "June"), (7, "July"), (8, "August"), (9, "September"), (10, "October"), (11, "November"), (12, "December")]
    for x in range(len(months)):
        if months[x][0] == todayMonth:
            todayMonthString = months[x][1]
    dateToday = "%d %s %d" % (todayDay, todayMonthString, todayYear)

    frc = date(2016,11,13)
    daysUntil = frc-today
    countdown = daysUntil.days

    pygame.init()

    orange = (255,165,0)
    white = (255,255,255)
    black = (0,0,0)
    green = (0,255,0)

    width = 1000
    height = 1900

    screen = pygame.display.set_mode((width, height))
        
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_q:
                exit()
    
    pygame.display.set_caption('Basic Pygame program')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(orange)

    # Display some text
    myfont = pygame.font.SysFont("monospace", 72, bold = True)
    bigFont = pygame.font.SysFont("monospace", 444, bold = True)
    
    text = myfont.render("Today is", 1, (white))
    textpos = text.get_rect(center=(width/2, height/2-250))

    text1 = myfont.render(dateToday, 1, (white))
    text1pos = text.get_rect(center=(width/2-120, height/2-160))

    text2 = myfont.render("%d days left"%(countdown), 1, (black))
    text2pos = text.get_rect(center=(width/2-90, height/2-80))

    text3 = myfont.render("until Bag and Tag!", 1, (white))
    text3pos = text.get_rect(center=(width/2-210, height/2))

    text4 = bigFont.render(".)", 1, (white))
    text4pos = text.get_rect(center=(width/2-100, height/2+400))
    
    background.blit(text, textpos)
    background.blit(text1, text1pos)
    background.blit(text2, text2pos)
    background.blit(text3, text3pos)
    background.blit(text4, text4pos)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    pygame.display.update()


    
