'#Faça um programa em python que abra e reproduza o áudio de um arquivo Mp3'

import pygame

pygame.init()
pygame.mixer.music.load("teste.mp3")
pygame.mixer.music.play()
input() #Nas versões recentes tem que colocar isso antes do wait
pygame.event.wait()
