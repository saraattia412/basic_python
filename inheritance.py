class date():
    def get_date(self):
        return '20-5-2019'
class time(date):
    def get_time(self):
        return "11:41:5"

t=time()
print("time: ",t.get_time(),"\n","date:",t.get_date())