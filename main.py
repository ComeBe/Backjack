# This is my training project - Blackjack

import random
import pygame
import copy

pygame.init()

# Deck

listCard = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = 4 * listCard
decks = 1
game_deck = copy.deepcopy(decks * deck)

# Game settings
WIDTH = 600
HEIGHT = 900

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('GITjack')
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('timesbd.ttf', 44)
smaller_font = pygame.font.Font('timesbd.ttf', 34)

active = False
# KDA
record = [0, 0, 0]
dealer_score = 0
player_score = 0
initial_deal = False
my_hand = []
dealer_hand = []
outcome = 0
show_dealer = False
cards = 0

#
def deal_cards(current_hand, current_deck):
    card = random.randint(0, len(current_deck))
    current_hand.append(current_deck[card - 1])
    current_deck.pop(card - 1)
    print(current_hand, current_deck)
    return current_hand, current_deck

#draw score

def draw_scores(player,dealer):
    screen.blit(font.render(f"Score[{player}]", True, "white"), (350,  400))
    if show_dealer:
        screen.blit(font.render(f"Score[{dealer}]", True, "white"),  (350,  400))





# show drawn cards

def draw_cards(player, dealer, show):
    for i in range(len(player)):
        pygame.draw.rect(screen, "white", [70 + (70 * i), 460 + (5 * i), 120, 220], 0, 5)
        screen.blit(font.render(player[i], True, "black"), (80 + 70 * i, 465 + 5 * i))
        screen.blit(font.render(player[i], True, "black"), (80 + 70 * i, 625 + 5 * i))
        pygame.draw.rect(screen, "red", [70 + (70 * i), 460 + (5 * i), 120, 220], 5, 5)

    for i in range(len(dealer)):
        pygame.draw.rect(screen, "white", [70 + (70 * i), 160 + (5 * i), 120, 220], 0, 5)
        if i != 0 or show:
            screen.blit(font.render(dealer[i], True, "black"), (80 + 70 * i, 165 + 5 * i))
            screen.blit(font.render(dealer[i], True, "black"), (80 + 70 * i, 325 + 5 * i))
        else:
            screen.blit(font.render("", True, "black"), (80 + 70 * i, 165 + 5 * i))
            screen.blit(font.render("", True, "black"), (80 + 70 * i, 325 + 5 * i))
        pygame.draw.rect(screen, "blue", [70 + (70 * i), 160 + (5 * i), 120, 220], 5, 5)


# Score countnter


def calculated_score(hand):
    hand_score = 0
    aces_count = hand.count("A")
    for i in range(len(hand)):
        # 2-0
        for j in range(8):
            if hand[i] == listCard[j]:
                hand_score += int(hand[i])

        if hand[i] in ["10", "J", "Q", "K"]:
            hand_score += 10
        #Aces
        elif hand[i] == "A":
            hand_score += 11


    if hand_score > 21 and aces_count > 0:
        for i in range(aces_count):
            if hand_score > 21:
                hand_score -= 10
    return hand_score


# First screen
def draw_game(act, record):
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
        screen.blit(hit_text, (70, 725))
        button_lst.append(hit)

        stand = pygame.draw.rect(screen, "white", [300, 700, 300, 100], 0, 5)
        pygame.draw.rect(screen, "green", [300, 700, 300, 100], 3, 5)
        stand_text = font.render("STAND", True, "black")
        screen.blit(stand_text, (375, 725))
        button_lst.append(stand)
        score_text = smaller_font.render(f"Wins: {record[0]}   Losses: {record[1]}   Draws: {record[2]}", True, "white")
        screen.blit(score_text, (100, 840))

    return button_lst


# Game

run = True
while run:
    # game fps and background color
    timer.tick(fps)
    screen.fill('black')

    if initial_deal:
        for i in range(2):
            my_hand, game_deck = deal_cards(my_hand, game_deck)
            dealer_hand, game_deck = deal_cards(dealer_hand, game_deck)
        print(my_hand, dealer_hand)
        initial_deal = False
    # thing shown in active state, dran cards, calculated score
    if active:
        player_score = calculated_score(my_hand)
        draw_cards(my_hand, dealer_hand, show_dealer)
        if show_dealer:
            dealer_score = calculated_score(dealer_hand)
            if dealer_score < 17:
                dealer_hand, game_deck = deal_cards(dealer_hand, game_deck)
        draw_scores(player_score, dealer_score)
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
