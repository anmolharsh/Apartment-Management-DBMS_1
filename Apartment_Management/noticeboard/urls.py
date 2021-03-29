from django.urls import path, include
from . import views

urlpatterns = (
    # urls for Notice
    path('notice/list/', views.NoticeListView.as_view(), name='noticeboard_notice_list'),
    path('notice/create/', views.NoticeCreateView, name='noticeboard_notice_create'),
    path('notice/detail/<slug:slug>/', views.NoticeDetailView.as_view(), name='noticeboard_notice_detail'),
    path('notice/update/<slug:slug>/', views.NoticeUpdateView.as_view(), name='noticeboard_notice_update'),
    path('notice/delete/<slug:slug>/', views.NoticeDeleteView.as_view(), name='noticeboard_notice_delete'),
    path('success', views.success, name = 'success'),
)