string = '1h 45m,360s,25m,30m 120s,2h 60s'

parts = string.replace(' ', '').split(',')
total_minutes = 0

for t in parts:
    mins = 0
    if 'h' in t:
        h = int(t.split('h')[0])
        mins += h * 60
    if 'm' in t:
        m = int(t.split('h')[-1].split('m')[0])
        mins += m
    if 's' in t:
        # отрезаем и часы, и минуты, берём то, что перед 's'
        sec = int(t.split('h')[-1].split('m')[-1].split('s')[0])
        mins += sec // 60  
    total_minutes += mins

print(total_minutes)  
# 289