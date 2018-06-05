import pika
import dill as pickle

def process_action(serialized_action):
    action = pickle.loads(serialized_action)
    action_text = action[0]
    action_func = action[1]
    action_parameter = action[2]
    print(action_text)
    if action_parameter:
        action_func(action_parameter)
    else:
        action_func()

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
