from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt

from docutils.nodes import note
from werkzeug.wrappers import json

from lmn.forms import PhotoDirectForm
from .models import Photo

from lmn.models import Note


def homepage(request):
    return render(request, 'lmn/home.html')


def cl_init_js_callbacks(param):
    pass


'''
The views.py file defines a view named upload_prompt, which initializes the direct 
form and defines the required callback URL:
'''
def upload_prompt(request):
    context = dict(direct_form = PhotoDirectForm())
    cl_init_js_callbacks(context['direct_form', request])
    return render(request, 'upload_prompt.html', context)

''' processes the received identifier, verifies the signature
 (concatenated to the identifier) and updates a model entity with the identifiers of the uploaded image
 '''
@csrf_exempt
def direct_upload_complete(request):
  form = PhotoDirectForm(request.POST)
  if form.is_valid():
    form.save()
    ret = dict(photo_id = form.instance.id)
  else:
    ret = dict(errors = form.errors)

  return HttpResponse(json.dumps(ret), content_type='application/json')


@login_required
def delete_own_note(request, slug=None):
    instance = get_object_or_404(Note, slug=slug)
    if request.user == Note.user:
        instance.delete()  # or save edits
        messages.success(request, "Successfully Deleted")
        return redirect("notes:feed")
    else:
        raise PermissionDenied  # import it from django.core.exceptions
        return redirect("notes:feed")