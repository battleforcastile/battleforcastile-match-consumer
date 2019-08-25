import os
import pika
import requests

credentials = pika.PlainCredentials(os.getenv('RABBITMQ_USER').rstrip(), os.getenv('RABBITMQ_PASSWORD').rstrip())
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='matches_pending')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    requests.post('http://battleforcastile-match-recorder-service/api/v1/matches/', data=body)

channel.basic_consume(queue='matches_pending', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()