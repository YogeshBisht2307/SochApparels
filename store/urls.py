from django.urls import path, include
from django.contrib import admin
from store.views import IndexView,BuyView, StoreView,AboutView, LoginView , RegistrationView, LogoutView, ContactView, CartView , AddCartView, RemoveCartView , ProductDetailView,CheckoutView, validate_payment, CancelOrderView,OrderView, CommentView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

admin.site.site_title = "Welcome to SochApparels Admin DashBoard"
admin.site.index_title = "Welcome to SochApparels Portal"

urlpatterns = [
    path("", IndexView.as_view() , name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("store/", StoreView.as_view(), name = "store"),
    path("login/", LoginView.as_view(), name="login"),
    path("registration/", RegistrationView.as_view(), name="Registration"),
    path("logout/", LogoutView.as_view(), name="Logout"),
    path("contact/", ContactView.as_view(), name= "Contact"),
    path("cart/",CartView.as_view(), name="Cart"),
    path("addtocart/<str:cloth_slug>/<str:size>", AddCartView.as_view(), name = "AddtoCart"),
    path("removecart/<str:cloth_slug>/<str:size>", RemoveCartView.as_view(), name="RemoveCart"),
    path("product_detail/<str:cloth_slug>", ProductDetailView.as_view(), name="Product_detail"),
    path("checkout/", login_required(CheckoutView.as_view(), login_url="/login/"), name="Checkout"),
    path("validate_payment/", validate_payment, name="validate_payment"),
    path('orders/',OrderView.as_view(), name="Orders"),
    path('cancel_order/', CancelOrderView.as_view(), name="cancelOrder"),
    path('comments/',login_required(CommentView.as_view(), login_url="/login/"), name="Comment"),
    path('buy/', BuyView.as_view(),name="Buy"),
    #password reset
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name = "store/registration/password_reset_form.html"),
    name="reset_password"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = "store/registration/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = "store/registration/password_reset_confirm.html"),name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name = "store/registration/password_reset_complete.html"), name='password_reset_complete')
]