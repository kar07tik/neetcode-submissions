import bisect

class MyCalendar:

    def __init__(self):
      
        self.calendar = []

    def book(self, startTime: int, endTime: int) -> bool:
 
        idx = bisect.bisect_right(self.calendar, (startTime, endTime))

        if idx > 0 and self.calendar[idx - 1][1] > startTime:
            return False

        if idx < len(self.calendar) and self.calendar[idx][0] < endTime:
            return False
 
        self.calendar.insert(idx, (startTime, endTime))
        return True

