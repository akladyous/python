import datetime as dt

print(dt.datetime.utcnow())
print(dt.datetime.now())
print(dt.datetime.now().hour - dt.datetime.utcnow().hour)
print('-'*60)
x=dt.datetime.now()
print(x.strftime('%a'))
# 
print(f"giorno {dt.date.today().year } mese {dt.date.today().month} giorno {dt.date.today().day}")


print(dt.date.year())