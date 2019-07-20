from pyquil.quil import Program
from pyquil.api import QVMConnection
from pyquil.gates import H
from functools import reduce

qvm = QVMConnection()

def randomq():
    circ = Program(H(0), H(1), H(2), H(3))
    mes = circ.measure_all()
    result = qvm.run(mes)
    value = reduce(lambda x, y: 2*x+y, result[0], 0)
    return value


board = list(range(16))


def printboard(board):
    print(f"|{board[0]} |{board[1]} |{board[2]} |{board[3]} |")
    print("---------------")
    print(f"|{board[4]} |{board[5]} |{board[6]} |{board[7]} |")
    print("---------------")
    print(f"|{board[8]} |{board[9]} |{board[10]}|{board[11]}|")
    print("---------------")
    print(f"|{board[12]}|{board[13]}|{board[14]}|{board[15]}|")
    print()


def line(char, a, b, c,d):
    if board[a] == char and board[b] == char and board[c] == char and board[d] == char:
        return True



def check(char):
    if line(char, 0,1,2,3):
        return True
    if line(char, 4,5,6,7):
        return True
    if line(char, 8,9,10,11):
        return True
    if line(char, 12,13,14,15):
        return True

    if line(char, 0,4,8,12):
        return True
    if line(char, 1,5,9,13):
        return True
    if line(char, 2,6,10,14):
        return True
    if line(char, 3,7,11,15):
        return True
        
    if line(char, 0,5,10,15):
        return True
    if line(char,3,6,9,12):
        return True

    for i in range(len(board)-1):
        if board[i] == i:
            return False
    else:
        print("Game ended in a draw!!!")


printboard(board)

while(1):
    pos = int(input("Choose a position: "))
    print()
    if board[pos] != 'o' and board[pos] != 'x':
        board[pos] = 'o'
        

        if check('o') == True:
            print ("You Win!!!")
            break

        
        while(1):
            computer = randomq()
            print(f"Computer chose position: {computer} \n")
            if board[computer] != 'x' and board[computer] != 'o':
                board[computer] = 'x'
              
                if check('x') == True:
                    print ("Computer Wins!!!")
                    break
              
                break

    else:
        print("Choose another position ")
    printboard(board)