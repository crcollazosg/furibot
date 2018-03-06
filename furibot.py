#!/usr/bin/python3
"""
Generador automático de sandeces políticas
No se asume ninguna responsabilidad por el uso de este programa 
"""
import random
import tweepy
import time
import os
from secrets import *

# SET TO 0 FOR NORMAL OPERATION
# SET TO 1 FOR DEBUG (TURNS TWEETING OFF)
DEBUG = 0

# Files
#names_path = 'apellidos.txt'
#ideology_path = 'ideologias.txt'
#gender_path = 'genero.txt'
#country_path = 'paises.txt'
#communication_path = 'comunicaciones.txt'
#face_path = 'cara.txt'
#mar_path = 'marica.txt'
#work_path = 'trabajar.txt'
#ext_path = 'extorsion.txt'
log_path = 'my/log/path.log'

# Phrases
#  0 - Doctrina: "Castrochavismo"
#  1 - Doctrinario: "Castrochavista"
#  2 - Rima con Ideología: "Radiografía"
#  3 - Rima con Género: "stéreo" 
#  4 - País: "Venezuela"
#  5 - Rima con comunicaciones: "Consignaciones"
#  6 - "cara"
#  7 - "marica"
#  8 - Rima con trabajar: "nadar"
#  9 - Rima con extorsión (termina en 'sión'): comisión
# 10 - Rima con pregunta
# 11 - rima con periodista
# 12 - lugares (con artículo): "la cárcel"
# 13 - termina en "ismo"
# 14 - termina en "ada": llamada
# 15 - termina en "ando": escuchando
# 16 - hijuep***s
# 17 - comunicación, para reemplazar paz

order_single = [
        'ideologias',
        'genero',
        'paises',
        'comunicaciones',
        'cara',
        'mk',
        'trabajar',
        'extorsion',
        'pregunta',
        'periodista',
        'lugares',
        'terr',
	'llamada',
	'escuchando',
	'hps',
	'comunicacion'
        ]

phrase_base = [
        #'¡El {x[0]} quiere llegar al poder! No a la {x[2]} de género.',
        '¡El {x[0]} se quiere tomar el poder!',
        '{x[1]}s quieren implantar la {x[2]} de género.',
        'No a la {x[2]} de género.',
        'Gobierno {x[1]} nos volverá como {x[4]}.',
        'Hacen daño los compañeros que no cuidan las {x[5]}.',
        '¡Y si lo veo le voy a dar en la {x[6]}, {x[7]}!',
        'Entro a un Carulla y otro compatriota me aborda y me dice que para poder {x[8]} tiene que pagar {x[9]}',
        'Siguiente {x[10]}, amigo {x[11]}',
        'Se escudan en su condición de {x[11]}s para ser permisivos cómplices del {x[13]}',
        'Les pido a los {x[11]}s que nos han apoyado, que mientras no estén en {x[12]}, voten los proyectos del Gobierno',
	'Esta {x[14]} la están {x[15]} esos {x[16]}.',
	'{x[17]} sí, pero no así'
        ]

trans_table = ''.maketrans('áéíóú', 'aeiou', ' ')

def limpiar(apellido):
    global trans_table
    return apellido.translate(trans_table).lower()

def doctrina(a, b):
    if len(b)<=4:
        return limpiar(a) + limpiar(b) + 'ismo'
    if b[-1] in 'aeiou':
        return limpiar(a) + limpiar(b)[:-1] + 'ismo'
    if b[-2:] in ['es', 'ez', 'os']:
        return limpiar(a) + limpiar(b)[:-2] + 'ismo'
    return limpiar(a) + limpiar(b) + 'ismo'

def doctrinario(a, b):
    if len(b)<=4:
        return limpiar(a) + limpiar(b) + 'ista'
    if b[-1] in 'aeiou':
        return limpiar(a) + limpiar(b)[:-1] + 'ista'
    if b[-2:] in ['es', 'ez', 'os']:
        return limpiar(a) + limpiar(b)[:-2] + 'ista'
    return limpiar(a) + limpiar(b) + 'ista'

def get_dictionaries():
    dicts = dict()
    for root, dirs, files in os.walk('/home/alarm/bin/furibot/dict'):
        for file in files:
            with open(os.path.join(root, file), 'r') as f:
                dicts[file] = f.read().splitlines()
                f.close()
    return dicts

#def tweet_this(text):
#    print(text)

if __name__=="__main__":
    # Load dictionaries
    dicts = get_dictionaries()

    ## API set up
    if not DEBUG:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        api = tweepy.API(auth)

    # Open log file
    my_log = open(log_path, 'a')

    # while True:
    # Randomize all the things!
    rand_base = random.choice(phrase_base)
    rand_names = [random.choice(dicts['apellidos']),
            random.choice(dicts['apellidos'])]
    rand_params = [
            doctrina(rand_names[0], rand_names[1]),
            doctrinario(rand_names[0], rand_names[1])
            ]
    for item in order_single:
        rand_params.append(random.choice(dicts[item]))
    
    # Prepare
    tweet_str = rand_base.format(x=rand_params)

    # Aim
    # if len(tweet_str) > 140: continue

    # Fire!, I mean, Tweet!
    if DEBUG:
        print(len(tweet_str), '-', tweet_str)
        # time.sleep(5)
        # continue
        exit()
    try:
        api.update_status(tweet_str)
        my_log.write(tweet_str + '\n')
        # time.sleep(1800)
    except TweepError:
        print('ERROR -' + str(TweepError.message[0]['code']) + '-' + TweepError.message[0]['message'])
        my_log.write('ERROR -' + str(TweepError.message[0]['code']) + tweet_str + '\n')
        # time.sleep(300)
