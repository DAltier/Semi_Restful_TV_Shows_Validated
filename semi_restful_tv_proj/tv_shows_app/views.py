from django.shortcuts import render, HttpResponse, redirect
from .models import *
from datetime import datetime, time, timezone
from time import gmtime, strftime
from django.contrib import messages


# POST Root route redirects to /shows
def index(request):
  return redirect('/shows')


# GET /shows
def view_all_shows(request):
  context = {
    'all_shows': Show.objects.all()
  }
  return render(request, 'index.html', context)


# GET /shows/new
def add_new_show(request):
  return render(request, 'add_show.html')


# POST /shows/create
def create_new_show(request):
  errors = Show.objects.create_validator(request.POST)
  if len(errors) > 0:
    for key, value in errors.items():
      messages.error(request, value)
    return redirect("/shows/new")
  else:
    new_show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], description=request.POST['description'])
    return redirect(f"/shows/{new_show.id}")



# GET /shows/id
def view_show(request, show_id):
  new_show = Show.objects.get(id=show_id)
  format_release = new_show.release_date.strftime('%d %B, %Y')
  context = {
    "release_date": format_release,
    "show": new_show,
  }
  return render(request, 'view_show.html', context)


# GET /shows/id
def edit_show(request, show_id):
  context = {
    'show': Show.objects.get(id=show_id),
  }
  return render(request, 'edit_show.html', context)


# POST shows/id/update
def update_show(request, show_id):
  errors = Show.objects.update_validator(request.POST)
  if len(errors) > 0:
    for key, value in errors.items():
      messages.error(request, value)
    return redirect(f"/shows/{show_id}/edit")
  else:
    show = Show.objects.get(id=show_id)
    show.title = request.POST['title']
    show.network = request.POST['network']
    show.release_date = request.POST['release_date']
    show.description = request.POST['description']
    show.save()
    return redirect(f"/shows/{show_id}")


# POST shows/<id>/destroy
def delete_show(reqest, show_id):
  show = Show.objects.get(id=show_id)
  show.delete()
  return redirect('/shows')