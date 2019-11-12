from django.core.checks import messages
from django.shortcuts import render, get_object_or_404, redirect
from flask import request

from lmn.models import Note


def homepage(request):
    return render(request, 'lmn/home.html')


def delete_own_note(request):
 id = request.POST['comment_id']
 pk = request.POST['blogs_id']
 if request.method == 'POST':
    note = get_object_or_404(Note, id=id, pk=pk)
    try:
        note.delete()
        messages.success(request, 'You have successfully deleted the comment')

    except:
        messages.warning(request, 'The comment could not be deleted.')

    return redirect('get_posts')