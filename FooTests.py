import unittest
import datetime

#This is the class we're testing
class DatePattern:

    def __init__(self, year, month, day):
        self.year  = year
        self.month = month
        self.day   = day

    def matches(self, date):
        return ((self.year and self.year == date.year or True) and
                (self.month and self.month == date.month or True) and
                self.day   == date.day)
                

#This is the testing class
class FooTests(unittest.TestCase):
    
    def testMatches(self):
        p = DatePattern(2004, 9, 28)
        d = datetime.date(2004, 9, 28)
        self.failUnless(p.matches(d))

    def testMatchesFalse(self):
        p = DatePattern(2004, 9, 28)
        d = datetime.date(2004, 9, 29)
        self.failIf(p.matches(d))

    def testMatchesYearAsWildCard(self):
        p = DatePattern(0, 4, 10)
        d = datetime.date(2009, 4, 10)
        self.failUnless(p.matches(d))

    def testMatchesYearAndMonthAsWildCards(self):
        p = DatePattern(0, 0, 1)
        d = datetime.date(2004, 10, 1)
        self.failUnless(p.matches(d))

    


def main():
    unittest.main()

if __name__ == '__main__':
    main()
