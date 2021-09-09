class Hw1q1:  # defines Hw1q1 class with the trait of time for the input
    def __init__(self, time):
        self.time = time

    #timeConvert Function#

    def timeConvert(self):
        days = self.time // 86400; time = self.time % 86400 # floor-divides seconds by number of seconds in a day, saves remainder
        if days == 0: day_str = '' # formats the string output for the number of days to be grammatically correct
        elif days == 1: day_str = '1 day,'
        else: day_str = str(days)+' days,'
        # same repeats for hours, minutes, and seconds
        hours = time // 3600; time = time % 3600
        if hours == 0: hour_str = ''
        elif hours == 1: hour_str = ' 1 hour,'
        else: hour_str = " "+str(hours)+' hours,'
        minutes = time // 60; time = time % 60
        if minutes == 0: min_str = ''
        elif minutes == 1: min_str = ' 1 minute,'
        else: min_str = " "+str(minutes)+' minutes,'
        seconds = time
        if seconds == 0: sec_str = ''
        elif seconds == 1: sec_str = ' 1 second'
        else: sec_str = " "+str(seconds)+' seconds'
        new_time = day_str + hour_str + min_str + sec_str # combines all the time instances into one string to return
        new_time = new_time.lstrip(" ")
        return new_time



