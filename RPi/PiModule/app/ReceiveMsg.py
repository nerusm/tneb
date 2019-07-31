__author__ = 'suren'

import pika

class Consumer:
    def __init__(self, config, rmq_queue_name, rmq_routing_key):
        print("in init")
        self.config = config
        self.rmq_queue_name = rmq_queue_name
        self.rmq_routing_key = rmq_routing_key

    def __enter__(self):
        print("in enter")
        self.connection = self._create_connection()
        return self

    def __exit__(self, *args):
        print("in exit")
        self.connection.close()

    def consume(self,message_received_callback):
        self.message_received_callback = message_received_callback

        channel = self.connection.channel()
        channel.queue_declare(queue=self.rmq_queue_name)
        # self._create_exchange(channel)
        # self._create_queue(channel)

        # channel.queue_bind(queue=self.config.get_common_param('RMQ_CLI2SRV_QUEUE_NAME'),
        #                    exchange='',
        #                    routing_key=self.config.get_common_param('RMQ_ROUTING_KEY'))

        channel.basic_consume(self._consume_message, queue=self.rmq_queue_name, no_ack=True)
        print(" [x] Waiting to receive messages...")
        channel.start_consuming()

    def _create_exchange(self, channel):
        exchange_options = self.config['exchangeOptions']
        channel.exchange_declare(exchange=self.config['exchangeName'],
                                 exchange_type=self.config['exchangeType'],
                                 passive=exchange_options['passive'],
                                 durable=exchange_options['durable'],
                                 auto_delete=exchange_options['autoDelete'],
                                 internal=exchange_options['internal'])

    def _create_queue(self, channel):
        # queue_options = self.config['queueOptions']
        channel.queue_declare(queue=self.config.get_common_param('RMQ_CLI2SRV_QUEUE_NAME'))
                              # passive=queue_options['passive'],
                              # durable=queue_options['durable'],
                              # exclusive=queue_options['exclusive'],
                              # auto_delete=queue_options['autoDelete'])

    def _create_connection(self):
        credentials = pika.PlainCredentials(self.config.get_env_param('RMQ_USER'),
                                            self.config.get_env_param('RMQ_PASS'))
        print(self.config.get_env_param('RMQ_SERVER_HOST'))
        parameters = pika.ConnectionParameters(host=str(self.config.get_env_param('RMQ_SERVER_HOST')),
                                               credentials=credentials)

        connection = pika.BlockingConnection(parameters)
        if connection:
            print("Conn establised")
        return connection

    def _consume_message(self, channel, method, properties, body):
        print(" [x] Msg Received:")
        print(" [x] Executing Callback Method..")
        self.message_received_callback(body)
        # channel.basic_ack(delivery_tag=method.delivery_tag)
