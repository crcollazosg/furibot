#!/usr/bin/python3
"""
Generador automático de sandeces políticas
"""
import random
import tweepy
from secrets import *

# Files
names_path = 'apellidos.txt'
ideology_path = 'ideologias.txt'
gender_path = 'genero.txt'
country_path = 'paises.txt'

# Phrases
# 0 - Doctrina: "Castrochavismo"
# 1 - Rima con Ideología: "Radiografía"
# 2 - Rima con Género: "stéreo"
# 3 - Doctrinario: "Castrochavista"
# 4 - País: "Venezuela"

phrase_base = [
        '¡El {0} quiere tomar el poder! No a la {1} de {2}.',
        '¡El {0} quiere tomar el poder!',
        '¡No a la {1} de {2}!',
        'Nos quieren implantar la {1} de {2}.',
        '{0} quiere introducir la {1} de {2}.',
        'Gobierno {3} nos volverá como {4}.',
        'Todo es un montaje, una persecución {3}.'
        ]

def doctrina(a, b):
    if len(b)<=4:
        return a.lower() + b.lower() + "ismo"
    if b[-1] in 'aeiou':
        return a.lower() + b[:-1].lower() + "ismo"
    if b[-2:] in ['es', 'ez']:
        return a.lower() + b[:-2].lower() + "ismo"
    return a.lower() + b.lower() + "ismo"

def doctrinario(a, b):
    if len(b)<=4:
        return a.lower() + b.lower() + "ista"
    if b[-1] in 'aeiou':
        return a.lower() + b[:-1].lower() + "ista"
    if b[-2:] in ['es', 'ez']:
        return a.lower() + b[:-2].lower() + "ista"
    return a.lower() + b.lower() + "ista"

def tweet_this(text):
    print(text)

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

    # Randomize all the things!
    rand_base = random.choice(phrase_base)
    rand_names = [random.choice(names), random.choice(names)]
    rand_doctrina = doctrina(rand_names[0], rand_names[1])
    rand_doctrinario = doctrinario(rand_names[0], rand_names[1])
    rand_country = random.choice(countries)
    rand_ideology = random.choice(ideologies)
    rand_gender = random.choice(genders)

    # Tweet it!
    tweet_this(rand_base.format(rand_doctrina,
        rand_ideology,
        rand_gender,
        rand_doctrinario,
        rand_country))

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    api.update_status('Volviendo de nuevo a la programación. Hay que cacharrear harto todavía.')
    
    #print(doctrina("Castro", "Chavez"))
    #print(doctrina("Uribe", "Pastrana"))
    #print(doctrinario("Cepeda", "Robledo"))
    #print(doctrinario("Zaa", "Botero"))
    #print(doctrinario("Samper", "Serpa"))
