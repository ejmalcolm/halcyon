import pika
import dill as pickle
from initialize_game import save_to_file

def load_gamestate():
    global planets
    global tasks
    global players
    with open('gamestate.pickle', 'rb') as handle:
        superlist = pickle.load(handle)
    planets = superlist[0]
    tasks = superlist[1]
    players = superlist[2]
    for class_dict in superlist:
        obj_list = [class_dict[key] for key in class_dict]
        for class_obj in obj_list:
            class_obj.instances.append(class_obj)

def process_action(serialized_action):
    #call the serialized action
    action = pickle.loads(serialized_action)
    action_text = action[0]
    action_func = action[1]
    action_parameter = action[2]
    print(action_text)
    if action_parameter:
        action_func(action_parameter)
    else:
        action_func()
    #update the saved gamestate
    load_gamestate()
    save_to_file()

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='action')

def callback(ch, method, properties, body):
    #call process_action_dock on the body, which is the serialized ActionDock
    process_action(body)

channel.basic_consume(callback,
                      queue='action',
                      no_ack=True)

def start_server():
    print(' [*] Waiting for messages. To exit press CTRL+C')
    try:
        channel.start_consuming()
    except Exception as e:
        print('Error: ' + str(e))
        start_server()

if __name__ == '__main__':
    start_server()
