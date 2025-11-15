a =['1h 45m','360s','25m','30m 120s','2h 60s']

hours = 0
count_h = 0
count_m = 0
count_s = 0

for str_t in a:
    chapter = str_t.split(' ')

for c in chapter:
    if 'h' in c:
        count_h = int(c.replace('h', ''))
    elif 'm' in c:
        count_m = int(c.replace('m', ''))
    elif 's' in c:
        count_s = int(c.replace('s', ''))
    
hours = count_h*60+count_m+count_s//60

print(hours)

