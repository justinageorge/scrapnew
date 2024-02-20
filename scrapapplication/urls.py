
from django.contrib import admin
from django.urls import path
from scrapapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path("scraps/all",views.ScrapListView.as_view(),name="scrap-all"),
    path("scraps/<int:pk>/detail",views.ScrapDetailView.as_view(),name="scrap-detail"),
    path("scraps/<int:pk>/remove",views.ScrapDeleteView.as_view(),name="scrap-remove"),
    path("scraps/add",views.ScrapCreateView.as_view(),name="scrap-add"),
    path("scraps/<int:pk>/change",views.ScrapUpdateView.as_view(),name="scrap-change"),
    path("register",views.SignUpView.as_view(),name="register"),
    path("",views.SignInView.as_view(),name="signin"),
    path("category/",views.CategoryView.as_view(),name="categories"),
    path('scrapfilter/<int:pk>/',views.filterView.as_view(),name="filter"),
    path('signout/',views.SignOutView.as_view(),name="signout"),
    path('scrap/feauture/',views.ScrapFeautureView.as_view(),name="scrapfeauture"),
    path('scrap/feautures',views.ScrapFeautureViews.as_view(),name="display"),
    path('review/<int:pk>/',views.ReviewView.as_view(),name="review")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
