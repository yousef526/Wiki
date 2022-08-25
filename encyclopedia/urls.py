from unicodedata import name
from django.urls import path

from encyclopedia import util

from . import views



urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>",views.select_Page,name="select_Page"),
    path("encyclopedia/View_content.html",views.random1,name="random1"),
    path("encyclopedia/new_entry.html",views.create_entry,name="create_entry"),
    path("encyclopedia/search_result.html",views.search,name="search"),
    path("encyclopedia/edit_content.html",views.edit,name="edit"),
    path("encyclopedia/save_edit.html",views.save_edit,name="save_edit")
]
