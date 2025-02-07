from django.urls import path
from . import views

urlpatterns = {
    path("accounts/", views.accounts, name = 'accounts'),
    path("accountsJSON/", views.accountsTransaccion, name = 'accountsTransaccion'),
    path("sendAccounts/", views.sendTransaccion, name = 'sendTransaccion')
}