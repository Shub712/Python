# DuckTyping : It is a concept where the type of an object is determined
#              by its behavior , not by its class

class InkJetPrinter:
    def printdocument(self,document):
        print("inkjet printer printing : ",document)

class LaserPrinter:
    def printdocument(self,document):
        print("laser printer printing : ",document)

class PDFWriter:
    def printdocument(self,document):
        print(f"Saving {document} as PDF")

def StartPrinting(Device):
    Device.printdocument("Marverllous Notes")

def main():

    StartPrinting(InkJetPrinter())
    StartPrinting(LaserPrinter())
    StartPrinting(PDFWriter())

main()