import pygame
import data
from constants import *
import datetime

API_UPDATE_EVENT = pygame.USEREVENT + 1
UPDATE_INTERVAL_MS = 60_000

def load_font(fontUrl):
    return pygame.font.Font(fontUrl, FONT_SIZE)

def get_sections():
    section_height = HEIGHT // SECTION_COUNT
    return [(0, i * section_height, WIDTH, section_height) for i in range(SECTION_COUNT)]

def draw_section(surface, rect, left_text, right_text, font):
    x, y, w, h = rect

    pygame.draw.rect(surface, BG_COLOR, rect)
    pygame.draw.rect(surface, BORDER_COLOR, rect, BORDER_WIDTH)

    left_surf = font.render(left_text, True, TEXT_COLOR)
    right_surf = font.render(right_text, True, TEXT_COLOR)

    left_y = y + h / 2 - left_surf.get_height() / 2
    right_y = y + h / 2 - right_surf.get_height() / 2

    surface.blit(left_surf, (x + PADDING, left_y))
    surface.blit(right_surf, (x + w - right_surf.get_width() - PADDING, right_y))

def update_api_data():
    departures = data.getDeparturesData("GLC")

    departuresData = []

    for d in departures[:5]:
        print(f"\n\nThis is d: {d}")
        departure = {
            "origin": d["origin"][0]["locationName"],
            "destination": d["destination"][0]["locationName"],
            "scheduledDepatureTime": d["std"],
            "actualDepartureTime": d["etd"]
        }
        departuresData.append(departure)

    return departuresData

def setup_api_timer():
    """Start a repeating 60s timer event."""
    pygame.time.set_timer(API_UPDATE_EVENT, UPDATE_INTERVAL_MS)
