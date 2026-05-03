from datetime import datetime

a=input()
b=input()

fs=datetime.strptime(a,'%Y-%m-%d')
ss=datetime.strptime(b,'%Y-%m-%d')

x=ss-fs
days=x.days

print(days)
