import datetime

y1, m1, d1 = input().split()
y2, m2, d2 = input().split()

first = datetime.date(int(y1), int(m1), int(d1))
second = datetime.date(int(y2), int(m2), int(d2))

diff = first - second
print(diff.total_seconds())