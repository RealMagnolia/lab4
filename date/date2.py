from datetime import datetime, timedelta

today = datetime.today()
yesterday = today - timedelta(1)
tomorrow = today + timedelta(1)

print(yesterday, end="\n")
print(today, end="\n")
print(tomorrow)