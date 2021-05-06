
from django.urls import path
from stockManagement import views
urlpatterns = [
    path('',views.index,name="home"),
    path('all_category/', views.category,name='category-list'),
    path('add_category/',views.addCategory,name='add-category'),
    path('edit_category/<str:pk>/',views.updateCategory,name='update-category'),
    path('del_category/<str:pk>/',views.deleteCategory,name='delete-category'),


    path('all_vendor/', views.vendor,name='vendor-list'),
    path('add_vendor/',views.addVendor,name='add-vendor'),
    path('edit_vendor/<str:pk>/',views.updateVendor,name='update-vendor'),
    path('del_vendor/<str:pk>/',views.deleteVendor,name='delete-vendor'),


    path('items/',views.itemList,name='item-list'),
    path('add_item/',views.addItem,name='add-item'),
    path('edit_item/<str:pk>/',views.updateItem,name='update-item'),
    path('del_item/<str:pk>/',views.deleteItem,name='delete-item'),



    path('issue_item/<str:pk>/', views.issueItem,name="issue-item"),
    path('receive_item/<str:pk>/', views.receiveItem,name="receive-item"),

]