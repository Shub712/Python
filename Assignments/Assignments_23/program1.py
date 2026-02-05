class BookStore:
    NoOfBooks = 0

    def __init__(self,A,B):
        self.BookName = A 
        self.Author = B
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Display(self):
        print(self.BookName,"by",self.Author,"No of books : ", BookStore.NoOfBooks)

def main():
    obj1 = BookStore("Hidden hindu","Akshat gupta")
    obj1.Display()

    obj2 = BookStore("Hakamari","Hrishikesh Gupte")
    obj2.Display()

    obj3 = BookStore("Khekda","Ratnakar Matkari")
    obj3.Display()
    


if __name__ == "__main__":
    main()