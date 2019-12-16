from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('base_handles/', views.BaseListView.as_view(), name='base-handles'),
    path('base_handles/<str:handle>', views.SimilarListView.as_view(), name='similar-handles'),
]

urlpatterns += [
        #path('handles/<char:handle>/', views.get_handle, name='get-handle'),
        ]