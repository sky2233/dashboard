from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from tickets.models import Internship, Comment
from .forms import formID, formComment

from datetime import datetime

# Create your views here.

template = 'main.html'
detailTemplate = 'details.html'

def get(request):
    data = Internship.objects.all()
    total = Internship.objects.all().count()
    open = Internship.objects.filter(ticket_status = "open")
    close = Internship.objects.filter(ticket_status = "closed")

    level1 = Internship.objects.filter(ticket_status = "open", ticket_priority = 1)
    level2 = Internship.objects.filter(ticket_status = "open", ticket_priority = 2)
    level3 = Internship.objects.filter(ticket_status = "open", ticket_priority = 3)

    prioDec = Internship.objects.order_by("-ticket_priority")
    prioAsc = Internship.objects.order_by("ticket_priority")

    context = {
        "tickets" : data,
        "total" : total,
        "open" : open,
        "close" : close,

        "level1" : level1,
        "level2" : level2,
        "level3" : level3,

        "priority_dec" : prioDec,
        "priority_asc" : prioAsc,
    }

    return render(request, template, context)

def details(request):
    if request.method == 'GET':
        form = formID(request.GET)
        if form.is_valid():
            ticketID = form.cleaned_data['ticketID']
            details = Internship.objects.filter(demisto_id = ticketID).first()
            data = Internship.objects.all()

            comment = Comment.objects.filter(demisto_id = ticketID)

            context = {
                "id" : ticketID,
                "details" : details,
                "tickets" : data,
                "comment" : comment,
            }

            return render(request, detailTemplate, context)
    else:
        form = formID()
    return render(request, template, {'form': form,})
    

def comments(request):
    url = "http://127.0.0.1:8000/"
    if request.method == 'POST':
        form = formComment(request.POST)
        if form.is_valid():
            print("ok")
            parentID = form.cleaned_data['parentID']
            commentText = form.cleaned_data['commentText']

            dateNow = datetime.now()
            commentDate = dateNow.strftime("%Y-%m-%d %H:%M:%S")

            post = Comment(demisto_id=parentID, comment_details=commentText, comment_date=commentDate)
            post.save()

            newurl = "http://127.0.0.1:8000/details/?ticketID="+ parentID
            return HttpResponseRedirect(newurl)
    else:
        form = formComment()
    # return HttpResponse(request.POST.items())
    return HttpResponse(form.errors)

def delete(request, commentID):
    commentID = commentID

    Comment.objects.filter(comment_details=commentID).delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
