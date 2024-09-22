from csv import reader
from os import walk
import pygame


def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter=",")
        terrain_map = [list(row) for row in layout]

    return terrain_map


def import_folder(path):
    surface_list = []
    for _, __, img_files in walk(path):
        img_files.sort()
        surface_list = [
            pygame.image.load(path + "/" + image).convert_alpha() for image in img_files
        ]
    return surface_list
