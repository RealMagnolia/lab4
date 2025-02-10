from datetime import datetime, timedelta

cur = datetime.today()
print(cur.replace(microsecond=0))