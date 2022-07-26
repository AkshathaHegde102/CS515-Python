'''
Created on 4/23/2022
@author:   Akshatha Vasant Hegde
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 12 - Date class
'''
import math
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).
            Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing selfs value.'''
        
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    def __repr__(self):
        '''This method also returns a string representation for the object.'''
        return self.__str__()

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def copy(self):
         '''Returns a new object with the same month, day, year
         as the calling object (self).'''
         dnew = Date(self.month, self.day, self.year)
         return dnew

    def equals(self, other):
         '''Decides if self and d2 represent the same calendar date,
         whether or not they are the in the same place in memory.'''
         return self.year == other.year and self.month == other.month and \
                self.day == other.day

    def tomorrow(self):
        '''This method should NOT RETURN ANYTHING! Rather, it should
        change the calling object so that it represents one calendar
        day after the date it originally represented.'''
        DIM = (0,31,28,31,30,31,30,31,31,30,31,30,31)
        D = self.day
        M = self.month
        Y = self.year
        if self.isLeapYear() :
            DIM = (0,31,29,31,30,31,30,31,31,30,31,30,31)
        if D == DIM[M]:
            if M == 12:
                self.day = 1
                self.month = 1
                self.year +=1
            else:
                self.day = 1
                self.month += 1
        else:
            self.day += 1
        
    def yesterday(self):
        '''Like tomorrow, this method should not return anything. Again,
        it should change the calling object so that it represents one
        calendar day before the date it originally represented. '''
        DIM = (0,31,28,31,30,31,30,31,31,30,31,30,31)
        D = self.day
        M = self.month
        Y = self.year
        if self.isLeapYear() :
            DIM = (0,31,29,31,30,31,30,31,31,30,31,30,31)
        if D == 1:
            if M == 1:
                self.day = 31
                self.month = 12
                self.year -= 1
            else:
                self.day = DIM[M-1]
                self.month -= 1
        else:
            self.day -= 1

    def addNDays(self, N):
        ''' it should change the calling object so that it represents
        N calendar days after the date it originally represented.'''
        print(self)
        for i in range(0,N):
            self.tomorrow()
            print(self)
        
    def subNDays(self, N):
        '''Like the addNDays method, this method should not return anything.
        Rather, it should change the calling object so that it represents N
        calendar days before the date it originally represented.'''
        print(self)
        for i in range(0,N):
            self.yesterday()
            print(self)

    def isBefore(self, d2):
        '''This method should return True if the calling object is a
        calendar date before the input named d2 (which will always be
        an object of type Date). If self and d2 represent the same day,
        this method should return False. Similarly, if self is after d2,
        this should returnFalse.'''
        if self.year < d2.year :
            return True
        elif self.year == d2.year :
            if self.month < d2.month :
                return True
            elif self.month == d2.month :
                if self.day < d2.day :
                    return True
                else :
                    return False
            else :
                return False
        else:
            return False
        
    def isAfter(self, d2):
        '''This method should return True if the calling object is a
        calendar date before the input named d2 (which will always be an
        object of type Date). If self and d2 represent the same day, this
        method should return False. Similarly, if self is after d2, this
        should returnFalse.'''
        if self.year > d2.year :
            return True
        elif self.year == d2.year :
            if self.month > d2.month :
                return True
            elif self.month == d2.month :
                if self.day > d2.day :
                    return True
                else :
                    return False
            else :
                return False
        else:
            return False
        
    def diff(self, d2):
        '''This method should return an integer representing the number
        of days between self and d2. '''
        day1 = self.copy()
        day2 = d2.copy()
        sign = -1
        cnt = 0
        if day1.equals(day2) :
            return 0
        else :
            if day1.isBefore(day2):
                while day1.isBefore(day2):
                    day2.yesterday()
                    cnt = cnt + 1
                sign = -1
            else :
                while day1.isAfter(day2):
                    day2.tomorrow()
                    cnt = cnt + 1
                sign = 1
        return sign*cnt

    def dow(self):
        '''This method should return a string that indicates the day of
        the week (dow) of the object (of type Date) that calls it.'''
        DayList = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        D = self.copy()
        Ref = Date(11,7,2011)
        if D.equals(Ref):
            return DayList[0]
        
        if D.isBefore(Ref):
            Num = D.diff(Ref)
            Num = math.sqrt(Num*Num)
            Num = Num - 1
            Num = int(Num % 7)
            DayL = DayList[::-1]
            return DayL[Num]
        else:
            Num = D.diff(Ref)
            Num = int((math.sqrt(Num*Num)) % 7)
            return DayList[Num]






        







                   
