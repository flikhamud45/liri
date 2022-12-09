import datetime


def gen_secs():
    x = 0
    while x <= 59:
        yield x
        x += 1


def gen_minutes():
    x = 0
    while x <= 59:
        yield x
        x += 1


def gen_hours():
    x = 0
    while x <= 23:
        yield x
        x += 1


def gen_time():
    sec_gen = gen_secs()
    min_gen = gen_minutes()
    hour_gen = gen_hours()

    sec = next(sec_gen)
    min = next(min_gen)
    hour = next(hour_gen)

    while hour <=23:
        yield ("%02d:%02d:%02d" % (hour, min, sec))

        try:
            sec = next(sec_gen)
        except:
            try:
                min = next(min_gen)

                sec_gen = gen_secs()
                sec = next(sec_gen)
            except:
                min_gen = gen_minutes()
                min = next(min_gen)

                hour = next(hour_gen)

                sec_gen = gen_secs()
                sec = next(sec_gen)


def gen_years(start=2019):
    x = datetime.datetime.now()

    while start <= int(x.strftime("%G")):
        if (start%4 == 0 or start%400) and start%100 != 0:
            yield start, True
        else:
            yield start, False
        start += 1

def gen_months():
    x = 1

    while x <= 12:
        yield x
        x += 1

def gen_days(month, leap_year=True):
    days_months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    if leap_year and month == 2:
        yield 29
    else:
        yield days_months[month]

def gen_date():
    year_gen = gen_years()
    month_gen = gen_months()
    day = 1

    year_touple = next(year_gen)
    year = year_touple[0]
    isleap = year_touple[1]
    month = next(month_gen)

    hour_gen = gen_time()
    hour = next(hour_gen)

    while True:

        yield ("%02d/%02d/%d" % (day, month, year) + " " + str(hour))

        try:
            hour = next(hour_gen)
        except:
            hour_gen = gen_time()
            hour = next(hour_gen)
            if day< next(gen_days(month, isleap)):
                day += 1
            else:
                try:
                    day = 1
                    hour_gen = gen_time()
                    hour = next(hour_gen)

                    month = next(month_gen)
                except:
                    day = 1
                    hour_gen = gen_time()
                    hour = next(hour_gen)

                    month_gen = gen_months()
                    month = next(month_gen)

                    year_touple = next(year_gen)
                    year = year_touple[0]
                    isleap = year_touple[1]


gen = gen_date()
for i in range (5):
    val = next(gen)
    for i in range (1000000):
        val = next(gen)
    print(val)

#y = gen_days(7)
#print(next(y))

