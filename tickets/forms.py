from django import forms

from datetime import datetime

class formID(forms.Form):
    ticketID = forms.CharField(label='ticketID', max_length=255)

class formComment(forms.Form):
    parentID = forms.CharField(label='parentID')
    commentText = forms.CharField(label='commentText')
    # dateNow = datetime.now()
    # commentDate = dateNow.strftime("%Y-%m-%d %H:%M:%S")

class commentDel(forms.Form):
    commentID = forms.CharField(label='commentID')
