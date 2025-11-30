# main.py / game.py
import datetime
import pygame
import sys

import constants
from utils import (
    WIDTH, HEIGHT, FPS, SCREEN_BG,
    draw_section, get_sections, load_font,
    update_api_data, setup_api_timer, setup_display_type_timer,
    API_UPDATE_EVENT, DISPLAY_TYPE_EVENT, get_station_options
)

pygame.init()

info = pygame.display.Info()
constants.WIDTH = info.current_w
constants.HEIGHT = info.current_h

import utils
utils.WIDTH = constants.WIDTH
utils.HEIGHT = constants.HEIGHT

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
    selection_mode = False
    station_options = get_station_options()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == API_UPDATE_EVENT:
                if not selection_mode:
                    departuresData = update_api_data()
                    print(f"data updated at time {datetime.datetime.now()}")

            if event.type == DISPLAY_TYPE_EVENT:
                if not selection_mode:
                    print("changing value")
                    displayDetails = not displayDetails

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos
                for i, rect in enumerate(sections):
                    x, y, w, h = rect
                    if x <= mx <= x + w and y <= my <= y + h:
                        if selection_mode:
                            selected_station = station_options[i]
                            constants.STATION = selected_station
                            utils.STATION = constants.STATION
                            departuresData = update_api_data()
                            selection_mode = False
                        else:
                            selection_mode = True
                        break

        screen.fill(SCREEN_BG)

        for i, rect in enumerate(sections):
            if selection_mode:
                left_text = station_options[i].upper()
                draw_section(
                    screen,
                    rect,
                    left_text,
                    "",
                    font,
                    False,
                    None
                )
            else:
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
