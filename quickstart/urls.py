from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from quickstart.views import (
        registration_view,pledge_view,pledge_list_view,pledge_detail
)
app_name = "funderProject"

urlpatterns = [
    path('register/', registration_view, name="register"),
    path('login/', TokenObtainPairView.as_view(), name="login"),
    path('refresh/', TokenRefreshView.as_view(), name="refreshtoken"),
    path('pledge/', pledge_view, name="pledge"),
    path('pledgelist/', pledge_list_view, name="pledgelist"),
    path('pledge/<int:pk>', pledge_detail, name="pledge"),


]
