__author__ = 'suren'

import pika
import traceback

class Publisher:
    def __init__(self, config, rmq_queue_name, rmq_routing_key):
        self.config = config
        self.rmq_queue_name = rmq_queue_name
        self.rmq_routing_key = rmq_routing_key

    def publish(self, message):
        connection = None
        try:
            connection = self._create_connection()
            channel = connection.channel()
            #
            # channel.exchange_declare(exchange=self.config['exchangeName'],
            #                              passive=True)
            # channel.queue_declare(queue=self.config.get_common_param('RMQ_CLI2SRV_QUEUE_NAME'))
            channel.queue_declare(queue=self.rmq_queue_name)
            channel.basic_publish(exchange='',
                                      routing_key=self.rmq_routing_key,
                                      body=message)

            # print(" [x] Sent message %r" % message)
            print(" [x] Sent message")
        except Exception as e:
            print(repr(e))
            traceback.print_exc()
            raise e
        finally:
            if connection:
                connection.close()

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
