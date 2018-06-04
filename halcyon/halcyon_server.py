import pika
import dill as pickle

def process_action_dock(serialized_dock):
    dock = pickle.loads(serialized_dock)
    for action in dock:
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
    print(" [x] Received %r" % body)
    #call process_action_dock on the body, which is the serialized ActionDock
    process_action_dock(body)

channel.basic_consume(callback,
                      queue='action',
                      no_ack=True)

def start_server():
    print(' [*] Waiting for messages. To exit press CTRL+C')
    try:
        channel.start_consuming()
    except Exception as e:
        print(e)
        start_server()

if __name__ == '__main__':
    start_server()
