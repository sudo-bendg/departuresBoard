# main.py
import datetime
import pygame
import sys

from utils import (
    WIDTH, HEIGHT, FPS, SCREEN_BG,
    draw_section, get_sections, load_font,
    update_api_data, setup_api_timer,
    API_UPDATE_EVENT
)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("5 Section Layout")

font = load_font("digital_7/digital-7.ttf")
clock = pygame.time.Clock()
sections = get_sections()

setup_api_timer()  # start the 1-minute update timer

def main():
    departuresData = update_api_data()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Timer event → refresh API data
            if event.type == API_UPDATE_EVENT:
                departuresData = update_api_data()
                print(f"data updated at time {datetime.datetime.now()}")

        screen.fill(SCREEN_BG)

        # draw UI
        for i, rect in enumerate(sections):
            draw_section(screen, rect, departuresData[i]["destination"], departuresData[i]["scheduledDepatureTime"], font)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
