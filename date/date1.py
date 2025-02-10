from datetime import datetime, timedelta    #вычитаем из нынешней даты пять дней 

cur = datetime.today()
print(cur - timedelta(5))