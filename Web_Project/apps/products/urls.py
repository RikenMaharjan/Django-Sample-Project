from django.urls import path

from apps.products.views import *

urlpatterns = [
    path('create/',create_product),
    path('create-cbv/',CreateProduct.as_view()),
    path('create-cbv/<int:pk>/',CreateProduct.as_view()),
    path('update-cbv/<int:pk>/',UpdateProduct.as_view()),
    path('detail-cbv/<int:pk>/',DetailProduct.as_view()),
    path('my_view/',my_view),
    path('my_view_cb/',MorningGreeting.as_view()),
    path('my_view_ev/',EveningGreeting.as_view()),

    # View ---> setup() --> dispatch --> Determine the type of request [get, put, post, etc]

]
