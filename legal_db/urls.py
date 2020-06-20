from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path(
        "case/", views.case_detail, name="case_detail"
    ),  # !! Temporary route just to show the layout
    path("cases/", views.case_index, name="case_index"),
    path(
        "scholarship/", views.case_detail, name="scholarship_detail"
    ),  # !! Temporary routes just to show the layout
    path("scholarships/", views.scholarship_index, name="scholarship_index"),
    path("faq/", views.temp, name="faq"),
]
