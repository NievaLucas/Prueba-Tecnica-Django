from django.urls import path
from . import views

urlpatterns = [
    path("accounts/", views.Account.as_view(), name = 'accounts'),
    path("accountsJSON/", views.jsonAccount, name = 'accountsTransaccion'),
    path("accountsSend/", views.SendTransaccion.as_view(), name = 'accountSend'),
    path("accountsUpdate/<int:id>/", views.UpdateTransaccion.as_view(), name = "accountUpdate")
]