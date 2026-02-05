import time
import datetime

def main():
    print(time.time())      # Epcho Time from 1 Jan 1970
    print(time.ctime())

    print(datetime.datetime.now())

if __name__ == "__main__":
    main()

