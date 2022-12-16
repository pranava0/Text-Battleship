class Player:
    def __init__(self, name : str, configs : dict) -> None:
        self.name = name
        self.Firing = Firing(configs['rows'], configs['cols'], name)
        self.Placement = Placement(configs['rows'], configs['cols'], name)

class Firing:

    def __init__(self, rows : int, cols : int, name : str) -> None:
        self.board = [["*" for i in range(cols)] for j in range(rows)]
        self.cols = cols
        self.rows = rows
        self.name = name
    
    def printboard(self):
        print(self.name + "'s Firing Board")
        printcols = " "
        for i in range(self.cols):
            printcols += " "
            printcols += str(i)
        print(printcols)
        for i in range(self.rows):
            print(str(i) + " " + " ".join(self.board[i]))

class Placement:
    
    def __init__(self, rows : int, cols : int, name : str) -> None:
        self.board = [["*" for i in range(cols)] for j in range(rows)]
        self.cols = cols
        self.rows = rows
        self.name = name
        self.shiplist = []
    
    def printboard(self):
        print(self.name + "'s Placement Board")
        printcols = " "
        for i in range(self.cols):
            printcols += " "
            printcols += str(i)
        print(printcols)
        for i in range(self.rows):
            print(str(i) + " " + " ".join(self.board[i]))

class Ship:

    def __init__(self, orient = "", name = "", loc = "", length = 0) -> None:
        self.orient = orient
        self.name = name
        self.location = loc
        self.length = length
        self.cords = dict()
