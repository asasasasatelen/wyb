from django.http import HttpResponseRedirect
def outlogin(request):
    if request.session.get('username')!=None:
        del request.session['username']
    return HttpResponseRedirect('/')
