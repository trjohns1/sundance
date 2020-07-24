from django.urls import path
from django.conf.urls import include
from pinpoint.views import PointsetListView
from pinpoint.views import PointsetCreateView
from pinpoint.views import PointsetUpdateView
from pinpoint.views import PointsetDeleteView
from pinpoint.views import PointListView
from pinpoint.views import PointCreateView
from pinpoint.views import PointUpdateView
from pinpoint.views import PointDeleteView
from pinpoint.views import ErrorView
from pinpoint.views import HomeView
#from pinpoint.views import SignupView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('pointset/pointset_list/', PointsetListView.as_view(), name='pointset_list'),
    path('pointset/pointset_create/', PointsetCreateView.as_view(), name='pointset_create'),
    path('pointset/pointset_update/', PointsetUpdateView.as_view(), name='pointset_update'),
    path('pointset/pointset_delete/', PointsetDeleteView.as_view(), name='pointset_delete'),
    path('point/point_list/', PointListView.as_view(), name='point_list'),
    path('point/point_create/', PointCreateView.as_view(), name='point_create'),
    path('point/point_update/', PointUpdateView.as_view(), name='point_update'),
    path('point/point_delete/', PointDeleteView.as_view(), name='point_delete'),
    path('error/', ErrorView.as_view(), name='error'),
    #path('accounts/signup/', SignupView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    # django.contrib.auth.urls includes the following:
    #   accounts/login/ [name='login']
    #   accounts/logout/ [name='logout']
    #   accounts/password_change/ [name='password_change']
    #   accounts/password_change/done/ [name='password_change_done']
    #   accounts/password_reset/ [name='password_reset']
    #   accounts/password_reset/done/ [name='password_reset_done']
    #   accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
    #   accounts/reset/done/ [name='password_reset_complete']
]