import unittest
import datetime

class DatePattern:

    def __init__(self, year, month, day, weekday = 0):
        self.year  = year
        self.month = month
        self.day   = day
        self.weekday = weekday

    def matches(self, date):
        return (self.yearMatches(date) and
                self.monthMatches(date) and
                self.dayMatches(date) and
                self.weekdayMatches(date))

    def yearMatches(self, date):
        if not self.year: return True
        return self.year == date.year

    def monthMatches(self, date):
        if not self.month: return True
        return self.month == date.month

    def dayMatches(self, date):
        if not self.day: return True
        return self.day == date.day

    def weekdayMatches(self, date):
        if not self.weekday: return True
        return self.weekday == date.weekday()

                

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

    def testMatchesWeekday(self):
        p = DatePattern(0, 0, 0, 2)
        d = datetime.date(2004, 9, 29)
        self.failUnless(p.matches(d))

    def testMatchesLastWeekday(self):
        p = DatePattern(0, 0, 0, 3)
        #Finish this



class YearPattern:
    def __init__(self, year):
        self.year = year

    def matches(self, date):
        return self.year == date.year


class MonthPattern:
    def __init__(self, month):
        self.month = month

    def matches(self, date):
        return self.month == date.month


class DayPattern:
    def __init__(self, day):
        self.day = day

    def matches(self, date):
        return self.day == date.day


class WeekdayPattern:
    def __init__(self, weekday):
        self.weekday = weekday

    def matches(self, date):
        return self.weekday == date.weekday()


class CompositePattern:
    def __init__(self):
        self.patterns = []
    
    def add(self, pattern):
        self.patterns.append(pattern)

    def matches(self, date):
        for pattern in self.patterns:
            if not pattern.matches(date):
                return False
        return True

    
        


class NewTests(unittest.TestCase):

    def testYearMatches(self):
        yp = YearPattern(2004)
        d = datetime.date(2004, 9, 29)
        self.failUnless(yp.matches(d))

    def testYearDoesNotMatch(self):
        yp = YearPattern(2003)
        d = datetime.date(2004, 9, 29)
        self.failIf(yp.matches(d))

    def testMonthMatches(self):
        mp = MonthPattern(9)
        d = datetime.date(2004, 9, 29)
        self.failUnless(mp.matches(d))

    def testMonthDoesNotMatch(self):
        mp = MonthPattern(8)
        d = datetime.date(2004, 9, 29)
        self.failIf(mp.matches(d))

    def testDayMatches(self):
        dp = DayPattern(29)
        d = datetime.date(2004, 9, 29)
        self.failUnless(dp.matches(d))

    def testDayDoesNotMatch(self):
        dp = DayPattern(28)
        d = datetime.date(2004, 9, 29)
        self.failIf(dp.matches(d))

    def testWeekdayMatches(self):
        wp = WeekdayPattern(2) #Wed
        d = datetime.date(2004, 9, 29)
        self.failUnless(wp.matches(d))

    def testWeekdayDoesNotMatch(self):
        wp = WeekdayPattern(1) #Tue
        d = datetime.date(2004, 9, 29)
        self.failIf(wp.matches(d))

    def testCompositeMatches(self):
        cp = CompositePattern()
        cp.add(YearPattern(2004))
        cp.add(MonthPattern(9))
        cp.add(DayPattern(29))
        d = datetime.date(2004, 9, 29)
        self.failUnless(cp.matches(d))

    def testCompositeDoesNotMatch(self):
        cp = CompositePattern()
        cp.add(YearPattern(2004))
        cp.add(MonthPattern(9))
        cp.add(DayPattern(28))
        d = datetime.date(2004, 9, 29)
        self.failIf(cp.matches(d))

    def testCompositeWithoutYearMatches(self):
        cp = CompositePattern()
        cp.add(MonthPattern(4))
        cp.add(DayPattern(10))
        d = datetime.date(2005, 4, 10)
        self.failUnless(cp.matches(d))

    

                       
        
        


    


def main():
    unittest.main()

if __name__ == '__main__':
    main()
