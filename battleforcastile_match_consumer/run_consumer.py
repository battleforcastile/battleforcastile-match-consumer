import os
import pika
import requests

credentials = pika.PlainCredentials(
    os.getenv('RABBITMQ_USER', 'user').rstrip(), os.getenv('RABBITMQ_PASSWORD', '').rstrip())
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='matches_pending')

def callback(ch, method, properties, body):
    match_recorder_service_port = os.getenv('MATCH_RECORDER_SERVICE_PORT', 5000)
    print("[x] Received %r" % body)
    r = requests.post(
        f'http://battleforcastile-match-recorder-service:{match_recorder_service_port}/api/v1/matches/', data=body)

    if r.status_code == 201:
        print(f'Match successfully created')
    else:
        print(r.content)

channel.basic_consume(queue='matches_pending', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()