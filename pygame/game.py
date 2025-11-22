# main.py / game.py
import datetime
import pygame
import sys

import constants    # <-- import the module, not the symbols
from utils import (
    WIDTH, HEIGHT, FPS, SCREEN_BG,
    draw_section, get_sections, load_font,
    update_api_data, setup_api_timer, setup_display_type_timer,
    API_UPDATE_EVENT, DISPLAY_TYPE_EVENT
)

pygame.init()

# Update WIDTH/HEIGHT stored in constants.py
info = pygame.display.Info()
constants.WIDTH = info.current_w
constants.HEIGHT = info.current_h

# Now update utils.WIDTH/HEIGHT too
# (because utils imported WIDTH/HEIGHT earlier from constants.py)
import utils
utils.WIDTH = constants.WIDTH
utils.HEIGHT = constants.HEIGHT

# Apply fullscreen using the updated values
screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT), pygame.FULLSCREEN)

pygame.display.set_caption("5 Section Layout")

font = load_font("digital_7/digital-7.ttf")
clock = pygame.time.Clock()
sections = get_sections()

setup_api_timer()
setup_display_type_timer()

def main():
    displayDetails = False
    departuresData = update_api_data()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == API_UPDATE_EVENT:
                departuresData = update_api_data()
                print(f"data updated at time {datetime.datetime.now()}")

            if event.type == DISPLAY_TYPE_EVENT:
                print("changing value")
                displayDetails = not displayDetails

        screen.fill(SCREEN_BG)

        for i, rect in enumerate(sections):
            draw_section(
                screen,
                rect,
                departuresData[i]["destination"],
                departuresData[i]["scheduledDepatureTime"],
                font,
                displayDetails,
                departuresData[i]["actualDepartureTime"]
            )

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
