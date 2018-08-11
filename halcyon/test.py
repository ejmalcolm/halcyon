import dill as pickle
import pika
import planet
import building
import vehicle
import creature
import tags
import player
import task
import inspect
import datetime
import dill as pickle

Dune = planet.Planet('Arrakis')
Hoth = planet.Planet('Hoth')

##dont delete above this plzty

#bldng = building.BuildingPlan('Cradle', Dune, Dune.octants['North'], ['Wood', 'Spawn|Automaton'], player.GM)
#
# spcshp = vehicle.SpaceShip('Halcyon', Dune, Dune.octants['North'], 100000)
#
# crtr = creature.Creature('a', Dune, Dune.octants['North'], 0, 1)
#
# labor = creature.Laborer('bob', Dune, Dune.octants['North'], build_rate=5, player=player.GM)
#
# bplan = building.BuildingPlan('buh', Dune, Dune.octants['North'], ['Wood', 'Metal'], player.GM)

def load_gamestate():
    global planets
    global tasks
    global players
    with open('gamestate.pickle', 'rb') as handle:
        superlist = pickle.load(handle)
    planets = superlist[0]
    tasks = superlist[1]
    players = superlist[2]

def launch_action(action_ship):
    #need to launch the action to the rabbitmq queue
    #first serializes the action with dill
    #then sends the serialized text to the queue
    #serialize the action ship
    serialized_action = pickle.dumps(action_ship)
    ##RabbitMQ queue##
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='action')
    channel.basic_publish(exchange='',
                          routing_key='action',
                          body=serialized_action)
    print("Sent serialized action to server")
    connection.close()

load_gamestate()
labor = planets['Dune'].octants['North'].contents[1]
launch_action(('abc', labor.move_octant, 'East'))
