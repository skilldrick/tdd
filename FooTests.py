#This is the refactor branch version

import unittest
import datetime

MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY = range(7)


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


class LastWeekdayInMonthPattern:
    def __init__(self, weekday):
        self.weekday = weekday

    def matches(self, date):
        nextWeek = date + datetime.timedelta(7)
        return (self.weekday == date.weekday() and
                nextWeek.month != date.month)
    
class NthWeekdayInMonthPattern:
    def __init__(self, n, weekday):
        self.n = n
        self.weekday = weekday

    def matches(self, date):
        if self.weekday != date.weekday():
            return False
        return self.n == self.getWeekdayNumber(date)

    def getWeekdayNumber(self, date):
        n = 1
        while True:
            previousDate = date - datetime.timedelta(7 * n)
            if previousDate.month == date.month:
                n += 1
            else:
                break
        return n

class LastDayInMonthPattern:
    def matches(self, date):
        tomorrow = date + datetime.timedelta(1)
        return tomorrow.month != date.month

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

    

class PatternTests(unittest.TestCase):
    def setUp(self):
        self.d = datetime.date(2004, 9, 29)

    def testYearMatches(self):
        yp = YearPattern(2004)
        self.failUnless(yp.matches(self.d))

    def testYearDoesNotMatch(self):
        yp = YearPattern(2003)
        self.failIf(yp.matches(self.d))

    def testMonthMatches(self):
        mp = MonthPattern(9)
        self.failUnless(mp.matches(self.d))

    def testMonthDoesNotMatch(self):
        mp = MonthPattern(8)
        self.failIf(mp.matches(self.d))

    def testDayMatches(self):
        dp = DayPattern(29)
        self.failUnless(dp.matches(self.d))

    def testDayDoesNotMatch(self):
        dp = DayPattern(28)
        self.failIf(dp.matches(self.d))

    def testWeekdayMatches(self):
        wp = WeekdayPattern(WEDNESDAY)
        self.failUnless(wp.matches(self.d))

    def testWeekdayDoesNotMatch(self):
        wp = WeekdayPattern(TUESDAY)
        self.failIf(wp.matches(self.d))

    def testCompositeMatches(self):
        cp = CompositePattern()
        cp.add(YearPattern(2004))
        cp.add(MonthPattern(9))
        cp.add(DayPattern(29))
        self.failUnless(cp.matches(self.d))

    def testCompositeDoesNotMatch(self):
        cp = CompositePattern()
        cp.add(YearPattern(2004))
        cp.add(MonthPattern(9))
        cp.add(DayPattern(28))
        self.failIf(cp.matches(self.d))

    def testCompositeWithoutYearMatches(self):
        cp = CompositePattern()
        cp.add(MonthPattern(9))
        cp.add(DayPattern(29))
        self.failUnless(cp.matches(self.d))


class LastWeekdayInMonthPatternTests(unittest.TestCase):
    def setUp(self):
        self.pattern = LastWeekdayInMonthPattern(WEDNESDAY)

    def testLastWednesdayMatches(self):
        lastWedOfSep2004 = datetime.date(2004, 9, 29)
        self.failUnless(self.pattern.matches(lastWedOfSep2004))

    def testLastWednesdayDoesNotMatch(self):
        firstWedOfSep2004 = datetime.date(2004, 9, 1)
        self.failIf(self.pattern.matches(firstWedOfSep2004))

                       
class NthWeekdayInMonthPatternTests(unittest.TestCase):
    def setUp(self):
        self.pattern = NthWeekdayInMonthPattern(1, WEDNESDAY)

    def testMatches(self):
        firstWedOfSep2004 = datetime.date(2004, 9, 1)
        self.failUnless(self.pattern.matches(firstWedOfSep2004))
    
    def testNotMatches(self):
        secondWedOfSep2004 = datetime.date(2004, 9, 8)
        self.failIf(self.pattern.matches(secondWedOfSep2004))
        

class LastDayInMonthPatternTests(unittest.TestCase):
    def setUp(self):
        self.pattern = LastDayInMonthPattern()

        
    def testMatches(self):
        lastDayInSep2004 = datetime.date(2004, 9, 30)
        self.failUnless(self.pattern.matches(lastDayInSep2004))

    def testNotMatches(self):
        secondToLastDayInSep2004 = datetime.date(2004, 9, 29)
        self.failIf(self.pattern.matches(secondToLastDayInSep2004))
        



def main():
    unittest.main()

if __name__ == '__main__':
    main()
