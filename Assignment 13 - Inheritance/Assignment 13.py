'''
Created on 4/27/2022
@author:   Akshatha Vasant Hegde
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 13 - Board class

'''
class Board:
    

    def __init__(self, width=7, height=6):
        ''' Initializing '''
        self.w = width
        self.h = height
        self.BoardSize = 7*6
        self.BoardPiece = [' ']*self.BoardSize
        
    def __repr__(self):
        ''' Used to represent string'''
        return str(self)

    def __str__(self):
        '''  This method returns a string (it does not print a string)
        representing the Board object that calls it.''' 
        newList = []
        for i in range(0,self.h):
            newList = newList + ['|']
            for j in range(0,self.w):
                index = (i*(self.w))+j
                newList = newList + [self.BoardPiece[index]]
                newList = newList + ['|']
            newList = newList + ['\n']
        newList = newList + ["---------------\n"]
        newList = newList + [" 0 1 2 3 4 5 6 "]
        return "".join(newList)

    def allowsMove(self, col):
        ''' return True if the calling Board object can allow a move
        into column c (because there is space available). It returns
        False if c does not have space available or if it is not a valid
        column. '''
        num = int(self.w-1)
        col = int(col)
        if (col > num):
            return False
        for i in range(0,self.h):
            index = (i*(self.w))+col
            if self.BoardPiece[index] == ' ' :
                return True
        return False

    def addMove(self, col, ox):
        ''' ox is a variable holding a string that is either "X" or "O",
        into column col.code will have to find the highest row number
        available in the column col and put the checker in that row.'''
        if self.allowsMove(col) == False :
            print("Not possible. Try again.")
            return self
        col = int(col)
        if self.BoardPiece[((self.h-1)*(self.w)) + col] == ' ' :
            self.BoardPiece[((self.h-1)*(self.w)) + col] = ox
            #Check 
            return self
        for i in range(0,self.h):
            index = (i*(self.w))+col
            if self.BoardPiece[index] != ' ':
                self.BoardPiece[((i-1)*(self.w)) + col] = ox
                #Check 
                return self

    def delMove(self,col):
        ''' remove the top checker from the column col. If the column is
        empty, then delMove should do nothing.'''
        if self.BoardPiece[((self.h-1)*(self.w)) + col] == ' ' :
            print("Not possible. Row empty.")
            return self
        for i in range(0,self.h):
            index = (i*(self.w))+col
            if self.BoardPiece[index] != ' ':
                self.BoardPiece[index] = ' '
                return self

    def horizontal(self, ox, row, col):
        ''' Helper function for winsFor() '''
        cnt = 0
        for column in range(0,self.w):
            index = (row*self.w) + column
            if self.BoardPiece[index] == ox:
                cnt = cnt + 1
                if cnt == 4 :
                    return True
            else:
                cnt = 0
        return False
                    

    def vertical(self, ox, row, col):
        ''' Helper function for winsFor() '''
        cnt = 0
        for i in range(0,self.h):
            index = i*(self.w) + col
            if self.BoardPiece[index] == ox:
                cnt = cnt + 1
                if cnt == 4 :
                    return True
            else:
                cnt = 0
        return False
        

    def diagonal_1(self, ox, i, j):
        ''' Helper function for winsFor() '''
        cnt = 0
        if i == j :
            i,j = 0,0
        elif i < j :
            j = j - i
            i = 0
        else : #i > j
            i = i - j
            j = 0            
        while (i < self.h) and (j < self.w) :
            index = i*(self.w) + j
            if self.BoardPiece[index] == ox:
                cnt = cnt + 1
                if cnt == 4 :
                    return True
            else:
                cnt = 0
            i += 1
            j += 1     
        return False

    def diagonal_2(self, ox, i, j):
        ''' Helper function for winsFor() '''
        cnt = 0
        j = i + j
        i = 0
        if (j >= self.w):
            i = j - (self.w - 1)
            j = self.w - 1
        while (i < self.h) and (j < self.w) :
            index = i*(self.w) + j
            if self.BoardPiece[index] == ox:
                cnt = cnt + 1
                if cnt == 4 :
                    return True
            else:
                cnt = 0
            i += 1
            j -= 1     
        return False



    def winsFor(self, ox):
        ''' return True if the given checker, 'X' or 'O', held in ox, has
        won the calling Board. It should return False otherwise.'''
        Flag = False
        for i in range(0,self.h):
            for j in range(0,self.w):
                index = i*(self.w) + j
                if self.BoardPiece[index] == ox:
                    if self.horizontal(ox,i,j) or self.vertical(ox,i,j) or self.diagonal_1(ox,i,j) or self.diagonal_2(ox,i,j):
                        Flag = True
                    if Flag is True:
                        print("win")
                        return Flag  
        return Flag


    def hostGame(self):
        "To play the game"
        print("Welcome to Connect Four!")
        WinFlag = False
        print(self)
        
        while True:
            
            col = int(input("\nX's choice: "))
            ox = 'X'
            Xturn = self.addMove(col, ox)
            print(Xturn)
            WinFlag = self.winsFor(ox)
            if WinFlag is True :
                print("X wins -- Congratulations!")
                break

            col = input("\nO's choice: ")
            ox = 'O'
            Oturn = self.addMove(col, ox)
            print(Oturn)
            WinFlag = self.winsFor(ox)
            if WinFlag is True :
                print("O wins -- Congratulations!")
                break
        #print("won")

    def setBoard(self, moveString):
        """ takes in a string of columns and places alternating checkers
        in those columns, starting with 'X' For example, call
        b.setBoard('012345') to see 'X's and 'O's alternate on the bottom
        row, or b.setBoard('000000') to see them alternate in the left
        column.nmoveString must be a string of integers
        """
        nextCh = 'X' #start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.w:
                self.addMove(col, nextCh)
            if nextCh == 'X':
                nextCh = 'O'
            else:
                nextCh = 'X'

