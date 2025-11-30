import pygame
import data
from constants import *
import datetime

API_UPDATE_EVENT = pygame.USEREVENT + 1
UPDATE_INTERVAL_MS = 60_000
DISPLAY_TYPE_EVENT = pygame.USEREVENT + 2
DISPLAY_TYPE_MS = 20_000

def load_font(fontUrl):
    return pygame.font.Font(fontUrl, int(HEIGHT * 0.1))

def get_sections():
    section_height = HEIGHT // SECTION_COUNT
    return [(0, i * section_height, WIDTH, section_height) for i in range(SECTION_COUNT)]

def draw_section(surface, rect, left_text, right_text, font, displayDetails, alt_right_text = None):
    x, y, w, h = rect

    pygame.draw.rect(surface, BG_COLOR, rect)
    pygame.draw.rect(surface, BORDER_COLOR, rect, BORDER_WIDTH)

    left_surf = font.render(left_text, True, TEXT_COLOR)
    right_surf = font.render(right_text, True, TEXT_COLOR)

    if (displayDetails and alt_right_text):
        right_surf = font.render(alt_right_text, True, TEXT_COLOR)
        if alt_right_text.lower() != "on time":
            right_surf = font.render(F"EXPECTED {alt_right_text}", True, TEXT_COLOR)
    else:
        right_surf = font.render(right_text, True, TEXT_COLOR)

    if alt_right_text.lower() == "cancelled":
        left_surf = font.render(left_text, True, DANGER_COLOR)
        right_surf = font.render("CANCELLED", True, DANGER_COLOR)

    left_y = y + h / 2 - left_surf.get_height() / 2
    right_y = y + h / 2 - right_surf.get_height() / 2

    surface.blit(left_surf, (x + PADDING + BORDER_WIDTH, left_y))
    surface.blit(right_surf, (x + w - right_surf.get_width() - PADDING - BORDER_WIDTH, right_y))

def update_api_data():
    departures = data.getDeparturesData(data.stations[STATION])

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

def setup_display_type_timer():
    pygame.time.set_timer(DISPLAY_TYPE_EVENT, DISPLAY_TYPE_MS)