#This is my training project - Blackjack

import random
import pygame
import copy

pygame.init()
#Deck

listCard = ['2', '3', '4', '5','6','7','8','9','10','J', 'Q','K','A']
deck = 4 * listCard
decks = 1
game_deck = copy.deepcopy(decks * deck)

#Game settings
WIDTH = 600
HEIGHT = 900

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('GITjack')
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('timesbd.ttf', 44,)


#Game

run = True
while run:
    #game fps and background color
    timer.tick(fps)
    screen.fill('black')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.QUIT