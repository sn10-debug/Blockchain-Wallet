from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Sign-In',views.sign_in_page_load,name="Sign-In-Page-Load"),
    path('get_words',views.words_provider,name="Words-Provider"),
    path('new-account-cred',views.New_Account,name="New-Account"),
    path('Account-Summary',views.display_account_summary,name="Display-Account-Summary"),
    path('get-info',views.provide_info,name="Provide Information"),
    path('import-wallet',views.import_wallet,name="Importing Wallet")
]
