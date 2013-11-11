from datetime import datetime

def is_programmer_day(date):
    return date.timetuple().yearday == 256
    #return date.timetuple().tm_yday == 256

if __name__ == '__main__':
    if is_programmer_day(datetime.today()):
        print "It's programmers day!"