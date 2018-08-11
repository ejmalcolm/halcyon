import pika
import dill as pickle
from planet import Planet
from task import ACTIVE_TASKS
from player import Player
from task import Task

def load_gamestate():
    global planets
    global tasks
    global players
    with open('gamestate.pickle', 'rb') as handle:
        superlist = pickle.load(handle)
    planets = superlist[0]
    tasks = superlist[1]
    players = superlist[2]

def save_to_file():
    tasks = {str(task): task for task in ACTIVE_TASKS}
    superlist = [planets, tasks, players]
    print([ACTIVE_TASKS[0].task_creator])
    print(planets['Dune'].octants['North'].contents)
    with open('gamestate.pickle', 'wb') as handle:
        pickle.dump(superlist, handle)

def process_action(serialized_action):
    load_gamestate()
    #call the serialized action
    action = pickle.loads(serialized_action)
    action_text = action[0]
    action_func = action[1]
    action_parameter = action[2]
    if action_parameter:
        print(action_func(action_parameter))
    else:
        action_func()
    #update the saved gamestate
    save_to_file()

def callback(ch, method, properties, body):
    #call process_action_dock on the body, which is the serialized ActionDock
    process_action(body)

def start_server():
    print(' [*] Waiting for messages. To exit press CTRL+C')
    try:
        channel.start_consuming()
    except Exception as e:
        print('Error: ' + str(e))
        start_server()

if __name__ == '__main__':
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='action')
    channel.basic_consume(callback, queue='action', no_ack=True)
    start_server()
    pass
