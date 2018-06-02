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
from collections import namedtuple

# Dune = planet.Planet('Arrakis', 5, 5)
#
# ##dont delete above this plzty
#
# bldng = building.Building('Wood Craft Factory', Dune, Dune.octants['North'], ['Refinery: Stone', 'Factory: Wood Crafts'], player.GM)
#
# spcshp = vehicle.SpaceShip('Halcyon', Dune, Dune.octants['North'], 100000)
#
# crtr = creature.Creature('a', Dune, Dune.octants['North'], 0, 1)
#
# labor = creature.Laborer('bob', Dune, Dune.octants['North'], build_rate=5, player=player.GM)
#
# bplan = building.Building_Plan('buh', Dune, Dune.octants['North'], ['Wood', 'Metal'], player.GM)

class ActionDock():

    def __init__(self):
        self.dock = []
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='action')

    def dock_action(self, action):
        #check validity?
        self.dock.append(action)

    def launch_actions(self):
        #need to launch the action to the rabbitmq queue
        #first serializes the action with dill
        #then sends the serialized text to the queue
        #serialize the action dock
        serialized_dock = pickle.dumps(self.dock)
        ##RabbitMQ queue##
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='action')
        channel.basic_publish(exchange='',
                              routing_key='action',
                              body=serialized_dock)
        print("Sent serialized action dock to server")
        connection.close()

a = ActionDock()
for action in range(25):
    a.dock_action(action)
a.launch_actions()
