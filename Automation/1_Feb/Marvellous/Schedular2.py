import time
import datetime
import schedule

def fun():
    print("Inside fun at : ",datetime.datetime.now())

def main():
    print("Inside Marvellous Automation Script at : ",datetime.datetime.now())

    schedule.every(20).seconds.do(fun)
    
    # Problem -> Program gets execute completly withpout waiting for schedular

if __name__ == "__main__":
    main()

