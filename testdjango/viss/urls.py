from django.urls import path
from . import views

app_name='viss'
urlpatterns = [
    # ex: /viss/
    path('<int:result_id>/', views.result1, name='result'),
    path('Drivetrain/InternalCombustionEngine/RPM/', views.RPM, name='RPM'),
    path('Speed/', views.SPEED, name='SPEED'),
]