import pika
import sys
import syslog
import time
from threading import Thread
from abc import abstractmethod
import callback_message as msg
import callback_db as db


class Callback:

    @abstractmethod
    def callback(self, ch, method, properties, body):
        pass
        

class StartConsume:

    instruction = {
                   'queue_one': {'callback': db.CallbackOne, 'no_ack': False, 'arguments': {"x-priority": 5}},
                   'queue_two': {'callback': db.CallbackTwo, 'no_ack': False, 'arguments': None},
                   'queue_three': {'callback': db.CallbackThree, 'no_ack': False, 'arguments': None},
                   'queue_mail': {'callback': msg.CallbackMail, 'no_ack': True, 'arguments': None},
                   'queue_sms': {'callback': msg.CallbackSMS, 'no_ack': True, 'arguments': None},
                   'queue_tlgrm': {'callback': msg.CallbackTelegram, 'no_ack': True, 'arguments': None}
                  }

    def __init__(self, queue):
        self.queue = queue
        
    def start_consume(self):
        callback = self.instruction[self.queue]['callback']().callback
        no_ack = self.instruction[self.queue]['no_ack']
        arguments = self.instruction[self.queue]['arguments']

        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host='localhost')
            )

            channel = connection.channel()
            channel.queue_declare(queue=self.queue, durable=True)
            channel.basic_consume(callback, queue=self.queue, no_ack=no_ack, arguments=arguments)

            channel.basic_qos(prefetch_count=1)
            channel.start_consuming()
        except Exception as exc:
            channel.stop_consuming()
            syslog.syslog("Error while consuming queue one: %s" % exc)

        connection.close()
        sys.exit(1)



def Supervisor(thr_list):
    thr = []

    for thread_name in thr_list:
        thr.append(None)

    while True:
        i = 0
        for thread_name in thr_list:
            if not thr[i] or not thr[i].is_alive():
                thr[i] = Thread(target=thread_name)
                thr[i].daemon = True
                thr[i].start()
                syslog.syslog("Starting thread for: %s" % str(thread_name))
            thr[i].join(1)
            i = i + 1

        time.sleep(10)


if __name__ == "__main__":
    syslog.openlog('some_tag', syslog.LOG_PID, syslog.LOG_NOTICE)

    try:
        thr_list = []
        for x in ['queue_one', 'queue_two', 'queue_three', 'queue_mail', 'queue_sms', 'queue_tlgrm']:
            thr_list.append(StartConsume(x).start_consume)

        Supervisor(thr_list)

    except KeyboardInterrupt:
        print("EXIT")
        raise

