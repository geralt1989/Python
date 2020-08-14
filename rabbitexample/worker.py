import pika

print("Collegamento a RabbitMQ...")

params = pika.ConnectionParameters(host="localhost")
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='worker_queue')

print("...eseguito")

def callback(ch, method, properties, body):
    print("Ricevuto %s" % body)


channel.basic_consume('worker_queue', callback, auto_ack=True)

channel.start_consuming()