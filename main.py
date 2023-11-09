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
font = pygame.font.Font('timesbd.ttf', 44)
smaller_font = pygame.font.Font('timesbd.ttf', 34)

active = False
#KDA
record = [0, 0, 0]
dealer_score = 0
player_score = 0
initial_deal = False
my_hand = []
dealer_hand = []
outcome = 0

#
def deal_cards(current_hand, current_deck):
    card = random.randint(0, len(current_deck))
    current_hand.append(current_deck[card-1])
    current_deck.pop(card-1)
    print(current_hand, current_deck)
    return current_hand, current_deck



#First screen
def draw_game(act, records):
    button_lst = []

    if not act:
        deal = pygame.draw.rect(screen, "white", [150, 20, 300, 100], 0, 5)
        pygame.draw.rect(screen, "green", [150, 20, 300, 100], 3, 5)
        deal_text = font.render("DEAL HAND", True, "black")
        screen.blit(deal_text, (165, 50))
        button_lst.append(deal)
# 2nd screen
    else:
        hit = pygame.draw.rect(screen, "white", [0, 700, 300, 100], 0, 5)
        pygame.draw.rect(screen, "green", [0, 700, 300, 100], 3, 5)
        hit_text = font.render("HIT ME", True, "black")
        screen.blit(hit_text, (55, 735))
        button_lst.append(hit)
        stand = pygame.draw.rect(screen, "white", [300, 700, 300, 100], 0, 5)
        pygame.draw.rect(screen, "green", [300, 700, 300, 100], 3, 5)
        stand_text = font.render("STAND", True, "black")
        screen.blit(stand_text, (355, 735))
        button_lst.append(stand)
        score_text = smaller_font.render(f"Wins: {record[0]}   Losses: {record[1]}   Draws: {record[2]}", True, "white")
        screen.blit(score_text, (100, 840))

    return button_lst

#Game

run = True
while run:
    #game fps and background color
    timer.tick(fps)
    screen.fill('black')

    if initial_deal:
        for i in range(2):
            my_hand, dealer_hand = deal_cards(my_hand, game_deck)
            dealer_hand, game_deck = deal_cards(dealer_hand, game_deck)
        print(my_hand, dealer_hand)
        initial_deal = False
    buttons = draw_game(active, record)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            if not active:
                if buttons[0].collidepoint(event.pos):
                    active = True
                    initial_deal = True
                    my_hand = []
                    dealer_hand = []
                    outcome = 0

    pygame.display.flip()
pygame.QUIT