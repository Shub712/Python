import time
import datetime
import schedule

def fun():
    print("Inside fun at : ",datetime.datetime.now())

def main():
    print("Inside Marvellous Automation Script at : ",datetime.datetime.now())

    schedule.every(20).seconds.do(fun)

    while True:
        schedule.run_pending()  # check pending work
        time.sleep(1)           # sleep for 1 second

if __name__ == "__main__":
    main()
