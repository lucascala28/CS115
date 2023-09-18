'''
Created on 12/7/2022
@author:   Luca SCala
Pledge:    I pledge my honor that I have abided by the stevens honor systme

CS115 - Hw 12 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

import math
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

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
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
         dnew = Date(self.month, self.day, self.year)
         return dnew
    def equals(self, d2):
         return self.year == d2.year and self.month == d2.month and self.day == d2.day
    def tomorrow(self):
        DIM = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        if self.isLeapYear():
            DIM[2] = 29
        else:
            DIM[2]=28
        if self.day + 1 > DIM[self.month]:
            self.day = 1
            if self.month + 1> 12:
                self.month = 1
                self.year += 1
            else:
                self.month += 1
        else:
            self.day +=1
    def yesterday(self):
        DIM = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        if self.isLeapYear():
            DIM[2] = 29
        else:
            DIM[2] = 28
        if self.day == 1:
            if self.month != 1:
                self.month -= 1
                self.day = DIM[self.month]
            else:
                self.month = 12
                self.day = DIM[self.month]
                self.year -=1
        else:
            self.day -= 1
    def addNDays(self,n):
        for i in range(1, n+1):
            print(self)
            self.tomorrow()
    def subNDays(self,n):
        for i in range(1,n+1):
            print(self)
            self.yesterday()
    def isBefore(self, d2):
        if self.year == d2.year:
            if self.month == d2.month:
                if self.day < d2.day:
                    return True
                return False
            elif self.month < d2.month:
                return True
            return False
        elif self.year < d2.year:
            return True
        return False
    def isAfter(self,d2):
        if self.day == d2.day and self.month == d2.month and self.year == d2.year:
            return False
        return not self.isBefore(d2)

    def diff(self,d2):
        copySelf = self.copy()
        days = 0
        if copySelf.isBefore(d2):
            while copySelf.isBefore(d2):
                copySelf.tomorrow()
                days -=1
        elif copySelf.isAfter(d2):
             while copySelf.isAfter(d2):
                 copySelf.yesterday()
                 days +=1
        return days
    def dow(self):
        knownDate = Date(12,7,2022)
        Diff = abs(self.diff(knownDate))
        print(Diff)
        remainder = Diff % 7
        if remainder == 0:
            return 'Wednesday'
        if remainder == 1:
            return 'Thursday'
        if remainder == 2:
            return 'Friday'
        if remainder == 3:
            return 'Saturday'
        if remainder == 4:
            return 'Sunday'
        if remainder == 5:
            return 'Monday'
        if remainder == 6:
            return 'Tuesday'
        

d1 = Date(2, 26, 1980)
d2 = Date(12, 16, 2011)
d1.addNDays(5)
print(d1)

