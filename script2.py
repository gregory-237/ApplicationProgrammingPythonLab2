dates_courses = []
f = open("dataset.csv", 'r')
for row in f:
    dates_courses.append(row.replace("\n", "").replace("-", ""))
dates_courses.reverse()
list_dates = []
for i in range (1, len(dates_courses)):
    if dates_courses[i-1][:4] == dates_courses[i][:4]:
        list_dates.append(dates_courses[i-1])
    else:
        list_dates.append(dates_courses[i-1])
        with open(f"script2/{list_dates[0][:8]}_{list_dates[-1][:8]}.csv", 'w') as d:
            for row in list_dates:
                d.write(f'{row[:4]}/{row[4:6]}/{row[6:8]}{row[8:]}\n')
            list_dates = []
        continue












