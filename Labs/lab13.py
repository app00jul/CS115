#Julian Noeske
#Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# 21fa-cs115bc
# lab13.py
# A.Nicolosi
# 20211201
# Practice with classes.


# TODO: Write a bare-bone class InvalidDateError that inherits from ValueError
# Your constructor should allow for up to three argument (for the month,
# day, and year).  Hint: recall the syntax for default parameter values.
class InvalidDateError(Exception):
    def __init__(self, month=0, day=0, year=0):
        super().__init__("Invalid date!")
        self.month = month
        self.day = day
        self.year = year

        
# Fill in the missing part in the class Date below
class Date:
    '''
    Date abstraction

    Demonstrate getter/setter methods and operator overloading
    '''
    daysInMonth = [31,          # not really using index 0 (dec of prev year)
                   31, 28, 31,  # jan, (non-leap) feb, mar
                   30, 31, 30,  # apr, may, jun
                   31, 31, 30,  # jul, aug, sep
                   31, 30, 31]  # oct, nov, dec

    def isLeapYear(year):
        # Every fourth year is a leap year,
        # except that every one-hundreth year it isn't,
        # but every four-hundreth year is a leap year after all!
        #
        # TODO
        if (year%4) == 0:
            return True
        elif (year%100) == 0:
            if (year%400) == 0:
                return True
        

    def __init__(self, month=1, day=1, year=1970):
        # Call self.validate to ensure that the parameters
        # make a valid date.  Raise an InvalidDateError if not.
        # If all is good, initialize the attributes _month, _day, and
        # _year
        #
        # TODO
        if Date.validate_params(month,day,year):
            self.month = month
            self.day = day
            self.year = year
        else:
            raise InvalidDateError

    def __repr__(self):
        # Make sure to return a string that looks like a valid
        # call to the class constructor
        # Ex: Date(12, 31, 2021)
        #
        # TODO
        return f"Date({self.month}, {self.day}, {self.year})"

    def __str__(self):
        # Return a string in the format mm/dd/yyyy
        #
        # TODO
        if self.month > 12 or self.month < 0:
            raise InvalidDateError
        elif self.month > 10 and self.month < 13:
            pass
        else:
            self.month = str(0) + str(self.month)
        
        if self.day > Date.daysInMonth[int(self.month)] or self.day < 0:
            raise InvalidDateError

        if self.day > 10:
            pass
        else:
            self.day = str(0) + str(self.day)

        if self.year > 1000:
            pass
        elif self.year >= 100 and self.year < 1000:
            self.year = str(0) + str(self.year)
        elif self.year >= 10 and self.year < 100:
            self.year = str(00) + str(self.year)
        else:
            self.year = str(000) + str(self.year)
        
        date = f"{self.month}/{self.day}/{self.year}"
        return date

    def _validateCheckFeb29(m, d, y):
        return 2 == m and 29 == d and Date.isLeapYear(y)

    def validate_params(m, d, y):
        # Return True if m, d, y represent a valid date
        # Start by checking if that's a valid Feb 29 (see
        # helper above); then check if d is a valid day
        # in month m
        #
        # TODO
        return Date._validateCheckFeb29(m,d,y) \
            or (1 <= m <= 12) \
            or (1 <= d <= 31) \
            or (1583 <= y)


        
    # Write getters and setters
    # TODO: get_month, get_day, get_year, set_month, set_day, set_year
    # NB: Setter should check that the resulting date is valid
    # *before* affecting the change
    
    def get_month(self):
        # TODO
        return self._month

    def get_day(self):
        # TODO
        return self._day

    def get_year(self):
        # TODO
        return self.year

    def set_month(self, month):
        # TODO
        tmp = self.month
        self.month = month 
        if not self.validate_params():
            self.month= tmp
            raise InvalidDateError(month, self.day, self.year)

    def set_day(self, day):
        # TODO
        tmp = self.day
        self.day = day 
        if not self.validate_params():
            self.day= tmp
            raise InvalidDateError(self.month, day, self.year)

    def set_year(self, year):
        # TODO
        tmp = self.year
        self.year = year 
        if not self.validate_params():
            self.year= tmp
            raise InvalidDateError(self.month, self.day, year)

    # Date arithmetic!

    def __eq__(self, other):
        # TODO
        if self.month == other.month \
            and self.day == other.day \
            and self.year == other.year:
            return True
        else: 
            return False

    def __ne__(self, other):
        # TODO
        if self.month == other.month \
            and self.day == other.day \
            and self.year == other.year:
            return False
        else: 
            return True

    def __lt__(self, other):
        # TO DO
        if self.year < other.year:
            return True
        elif self.year > other.year:
            return False
        else:
            if self.month < other.month:
                return True
            elif self.month > other.month:
                return False
            else:
                if self.day < other.day:
                    return True
                else:
                    return False
                

    def __ge__(self, other):
        # TODO
        if self.year < other.year:
            return False
        else: 
            if self.month < other.month:
                return False
            else:
                if self.day >= other.day:
                    return True
                else:
                    return False


    def __le__(self, other):
        # TODO
        if self.year > other.year:
            return False
        else: 
            if self.month > other.month:
                return False
            else:
                if self.day <= other.day:
                    return True
                else:
                    return False

    def __gt__(self, other):
        # TODO
        if self.year > other.year:
            return True
        elif self.year < other.year:
            return False
        else:
            if self.month > other.month:
                return True
            elif self.month < other.month:
                return False
            else:
                if self.day > other.day:
                    return True
                else:
                    return False

    def __add__(self, deltaInDays):
        '''Computes the date following `self` by the specified number of days'''
        # TODO
        if type(self) != int and type(self) != Date or (type(deltaInDays) != int and type(deltaInDays) != Date):
            raise TypeError
        if type(self) == Date:
            day = self.day
            month = self.month
            year = self.year
            deltaInDays = deltaInDays
        if type(deltaInDays) != int:
            raise TypeError
        days_to_add = deltaInDays
        while days_to_add > 0:
            day+=1
            if day == Date.daysInMonth[int(month)]:
                day = 0
                month += 1
                if month > 12:
                    day = 0
                    month = 1
                    year += 1
            days_to_add -=1
        return(Date(month,day,year))

trial = Date(6,13,2002)
print(trial.__str__())
print(Date.isLeapYear(trial.get_year()))

Person_1 = Date(6,13,2002)
Person_2 = Date(7,31,2002)

print(Date.__eq__(Person_1,Person_2)) #false
print(Date.__ne__(Person_1,Person_2)) #true
print(Date.__lt__(Person_1,Person_2)) #true
print(Date.__ge__(Person_1,Person_2)) #false
print(Date.__gt__(Person_1,Person_2)) #false
print(Date.__le__(Person_1,Person_2)) #true

print(Date.__add__(Person_1,23))

false_date = Date(5,32,2002)

print(Date.__str__(false_date))

trial_date = Date(12,30,2002)
print(Date.__add__(trial_date,33))