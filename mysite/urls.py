"""
遷移先のurlの設定
includeをすることでその先のファイルのurlに派生する
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('accounts.urls')),
    path('equipments/', include('equipments.urls')),
    path('login/equipments/', include('equipments.urls')),
    path('login/login/equipments/',include('equipments.urls')),
    path('admin/', admin.site.urls),
]
