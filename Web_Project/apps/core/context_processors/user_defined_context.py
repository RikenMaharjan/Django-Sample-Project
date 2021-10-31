import datetime

def time_now(request):
    dt = datetime.datetime.now()
    return {'date_now':dt}