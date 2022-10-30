from django.urls import path
from . import views
app_name = "blog"
urlpatterns = [
    path('', views.BlogHome.as_view(), name='home' ),
    path('generator/', views.BlogGenerator.as_view(), name='generator'),
    path('detail/<int:pk>', views.BlogDetail.as_view(), name='detail'),
    path('crear', views.BlogCreate.as_view(), name='crear'),
    path('update/<int:pk>', views.BlogUpdate.as_view(), name='update'),
]