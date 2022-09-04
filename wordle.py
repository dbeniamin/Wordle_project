import pygame
import random
import sys

from pygame.locals import *

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 0)
green = (0, 255, 0)
grey = (211, 211, 211)
navy = (0, 0, 128,)
lightBlue = (0, 255, 255)
red = (255, 0, 0)

font = pygame.font.SysFont("Helvetica neue", 40)
bigFont = pygame.font.SysFont("Helvetica neue", 80)
youWin = bigFont.render("You win!", True, green)
youLose = bigFont.render("You Lose!", True, red)
playAgain = bigFont.render("Play Again?", True, lightBlue)


def checkGuess(turns, word, userGuess, window):
    renderList = ["", "", "", "", ""]
    spacing = 0  # distance between letters
    guessCollorCode = [grey, grey, grey, grey, grey]

    for x in range(0, 5):
        if userGuess[x] in word:
            guessCollorCode[x] = yellow  # letter in the name but wrong pos
        if word[x] == userGuess[x]:
            guessCollorCode[x] = green  # letter in the name with right pos

    list(userGuess)
    for x in range(0, 5):
        renderList[x] = font.render(userGuess[x], True, navy)
        pygame.draw.rect(window, guessCollorCode[x], pygame.Rect(60 + spacing, 50 + (turns * 80), 50, 50))
        # drawing the 5 rectangles for each letter
        window.blit(renderList[x], (75 + spacing, 65 + (turns * 80)))  # drawing letters in the rectangles
        spacing += 80  # each box drawn 80px to the right

    if guessCollorCode == [green, green, green, green, green]:
        return True


def main():
    file = open("WordList.txt", "r")
    WordList = file.readlines()
    word = WordList[random.randint(0, len(WordList) - 1)].upper()

    height = 700
    width = 500

    FPS = 30
    clock = pygame.time.Clock()

    window = pygame.display.set_mode((width, height))
    window.fill(navy)

    guess = ""
    print(word)

    for x in range(0, 5):
        for y in range(0, 5):
            pygame.draw.rect(window, grey, pygame.Rect(60 + (x * 80), 50 + (y * 80), 50, 50),
                             2)  # defining rectangles, mode 2 - unfiled, blank - will fill the rectangles

    pygame.display.set_caption("Wordle Homework!")

    turns = 0
    win = False

    while True:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                guess += event.unicode.upper()  # detect if the key pressed is a leter , changes to upper case

                if event.key is K_RETURN and win is True:
                    main()

                if event.key is K_RETURN and turns == 6:
                    main()

                if event.key is pygame.K_BACKSPACE or len(guess) > 5:
                    guess = guess[:-1]
                    # typing more than 5 letters will remove the last typed letters
                if event.key is K_RETURN and len(guess) > 4:
                    win = checkGuess(turns, word, guess, window)
                    turns += 1
                    guess = ""
                    window.fill(navy, (0, 500, 500, 200))

        window.fill(navy, (0, 500, 500, 200))
        renderGuess = font.render(guess, True, grey)
        window.blit(renderGuess, (180, 530))

        if win is True:
            window.blit(youWin, (125, 500))
            window.blit(playAgain, (90, 600))

        if turns == 6 and win is not True:
            window.blit(youLose, (125, 525))
            window.blit(playAgain, (90, 600))

        pygame.display.update()
        clock.tick(FPS)


main()
