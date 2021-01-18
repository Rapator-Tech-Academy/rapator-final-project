from .models import ActiveUserDetail
from datetime import datetime, timedelta, date
from django.utils.timezone import get_current_timezone


def subject_renderer(request):
   
    ipaddress = request.META.get('REMOTE_ADDR')
    active_user = ActiveUserDetail()
    active_user.ip= ipaddress
    active_user.visited_time = datetime.now(tz=get_current_timezone()) 

    if request.user.is_authenticated:
        active_user.is_user = True
    else:
        active_user.is_user = False
    
    active_user.save()
    
    last_day = (datetime.now() - timedelta(days=1)).strftime('%d')
    ActiveUserDetail.objects.filter(visited_time__day = last_day).delete() 
    #guest = str(ActiveUserDetail.objects.filter(is_user=False).count())   #qeydiyyatda olmayanlarin sayi
    #users = str(ActiveUserDetail.objects.filter(is_user=True).count())    #qeydiyyatdan kecenlerin sayi
    
    total =  str(ActiveUserDetail.objects.all().count())                   #umumi istifadecilerin sayi


    return {
        'active_users': total,  # avoid naming it `user` as this is
                                # the current signed in user
    }