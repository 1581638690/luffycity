
from django.urls import path,re_path,include

from app01.table import course,userLogin

urlpatterns = [
    re_path(r"^course/$",course.CourseView.as_view({"get":"list"})),
    path("course/<int:id>/",course.CourseView.as_view({"get":"retrieve"})),
    path("test/",course.test.as_view({"get":"list"})),
    re_path(r"^login/$",userLogin.LoginView.as_view()),
    re_path(r"^article/$",course.ArticleView.as_view({"get":"list"})),
    path('article/<int:id>/', course.ArticleView.as_view({"get": "retrieve"})),
    path('article/<int:id>/', course.ArticleViewAgree.as_view({"post": "post"}))
]