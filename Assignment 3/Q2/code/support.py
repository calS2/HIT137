import os
from os import walk
import pygame

def import_folder(path):
    surface_list = []

    for _,__,img_file in walk(path):
        for image in img_file:
            full_path = path + '/' + image
            print(path,image)
            print(full_path)
            image_surf = pygame.image.load(full_path)
            print('prin')
            surface_list.append(image_surf)

    return surface_list