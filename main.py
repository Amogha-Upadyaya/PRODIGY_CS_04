from KeyLogger import KeyLogger
import time

def main():
    keylogger = KeyLogger()
    while True:
        print("KEYLOGGER CONTROL MENU:\n1. Start Keylogger\n2. Stop Keylogger\n3 Exit")

        opt = int(input("Enter your choice (1-3): "))
        
        if opt == 1:
            if keylogger.listener is None or not keylogger.listener.running:
                keylogger.start()
                print("Keylogger Started")
            else:
                print("Keylogger is already running")
        
        elif opt == 2:
            if keylogger.listener is not None and keylogger.listener.running:
                keylogger.stop()
                print("Keylogger stopped")
            else:
                print("Keylogger is not running")
        
        elif opt == 3:
            if keylogger.listener is not None and keylogger.listener.running:
                keylogger.stop()
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")
        
        time.sleep(1)

if __name__ == "__main__":
    main()
