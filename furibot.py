#!/usr/bin/python3
"""
Generador automático de sandeces políticas
No se asume ninguna responsabilidad por el uso de este programa
fuera de su 
"""
import random
import tweepy
import time
from secrets import *

# Files
names_path = 'apellidos.txt'
ideology_path = 'ideologias.txt'
gender_path = 'genero.txt'
country_path = 'paises.txt'
communication_path = 'comunicaciones.txt'
face_path = 'cara.txt'
mar_path = 'marica.txt'
log_path = 'furilog.log'

# Phrases
# 0 - Doctrina: "Castrochavismo"
# 1 - Rima con Ideología: "Radiografía"
# 2 - Rima con Género: "stéreo" 
# 3 - Doctrinario: "Castrochavista"
# 4 - País: "Venezuela"
# 5 - Rima con comunicaciones: "Consignaciones"
# 6 - "cara"
# 7 - "marica"

phrase_base = [
        '¡El {0} se quiere tomar el poder! No a la {1} de género.',
        '¡El {0} se quiere tomar el poder!',
        '¡No a la {1} de género!',
        'Nos quieren implantar la {1} de género.',
        '{0} quiere introducir la {1} de género.',
        'Gobierno {3} nos volverá como {4}.',
        'Todo es un montaje, una persecución {3}.',
        'Hacen daño los compañeros que no cuidan las {5}.',
        '¡Si lo veo le doy en la {6}, {7}!'
        ]

trans_table = ''.maketrans('áéíóú', 'aeiou', ' ')

def limpiar(apellido):
    global trans_table
    return apellido.translate(trans_table).lower()

def doctrina(a, b):
    if len(b)<=4:
        return limpiar(a) + limpiar(b) + "ismo"
    if b[-1] in 'aeiou':
        return limpiar(a) + limpiar(b)[:-1] + "ismo"
    if b[-2:] in ['es', 'ez']:
        return limpiar(a) + limpiar(b)[:-2] + "ismo"
    return limpiar(a) + limpiar(b) + "ismo"

def doctrinario(a, b):
    if len(b)<=4:
        return limpiar(a) + limpiar(b) + "ista"
    if b[-1] in 'aeiou':
        return limpiar(a) + limpiar(b)[:-1] + "ista"
    if b[-2:] in ['es', 'ez']:
        return limpiar(a) + limpiar(b)[:-2] + "ista"
    return limpiar(a) + limpiar(b) + "ista"

#def tweet_this(text):
#    print(text)

if __name__=="__main__":
    # Load dictionaries
    with open(names_path, 'r') as names_file:
        names = names_file.read().splitlines()
    with open(ideology_path, 'r') as ideology_file:
        ideologies = ideology_file.read().splitlines()
    with open(gender_path, 'r') as gender_file:
        genders = gender_file.read().splitlines()
    with open(country_path, 'r') as country_file:
        countries = country_file.read().splitlines()
    with open(communication_path, 'r') as communication_file:
        communications = communication_file.read().splitlines()
    with open(face_path, 'r') as face_file:
        faces = face_file.read().splitlines()
    with open(mar_path, 'r') as mar_file:
        mars = mar_file.read().splitlines()

    ## API set up
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    # Open log file
    my_log = open(log_path, 'w')

    while True:
        # Randomize all the things!
        rand_base = random.choice(phrase_base)
        rand_names = [random.choice(names), random.choice(names)]
        rand_doctrina = doctrina(rand_names[0], rand_names[1])
        rand_doctrinario = doctrinario(rand_names[0], rand_names[1])
        rand_country = random.choice(countries)
        rand_ideology = random.choice(ideologies)
        rand_gender = random.choice(genders)
        rand_communication = random.choice(communications)
        rand_face = random.choice(faces)
        rand_mar = random.choice(mars)
    
        # Tweet it!
        tweet_str = rand_base.format(rand_doctrina,
            rand_ideology,
            rand_gender,
            rand_doctrinario,
            rand_country,
            rand_communication,
            rand_face,
            rand_mar)
        api.update_status(tweet_str)
        my_log.write(tweet_str + '\n')
        #print(tweet_str)
        # Debug version
        #print(len(tweet_str), '-', tweet_str) 
        # Rest for 15 minutes and repeat
        time.sleep(900)
