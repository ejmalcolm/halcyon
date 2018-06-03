import pika
import dill as pickle

def process_action_dock(serialized_dock):
    dock = pickle.loads(serialized_dock)
    print(dock)

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
print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()
