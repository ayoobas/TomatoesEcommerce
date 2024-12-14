from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm, MyPasswordResetForm, MyPasswordChangeForm

urlpatterns = [
    path('', views.home, name = "home"),
    path('home/', views.home, name = "home"),
    path('about/', views.about, name = "about"),
    path('contact/', views.contact, name= "contact"),
    path("category/<slug:val>", views.CategoryView.as_view(), name = "category"), #.asview() was used because a class was used in view to define category  also their are several cateogries so the categories are passed in as parameters 
    path("product-detail/<int:pk>", views.ProductDetail.as_view(), name = "product-detail"),
    path("category-title/<val>", views.CategoryTitle.as_view(), name = "category-title"),
    path('profile/', views.ProfileView.as_view(), name = 'profile'), 
    path('address/', views.address, name = 'address'), 
    path('updateAddress/<int:pk>', views.updateAddress.as_view(), name = 'updateAddress'), 

    #Users registration 
    path("registration/", views.CustomerRegistrationView.as_view(), name = "customerregistration"),
    
    #Login authentication
    #path("accounts/login/", auth_view.LoginView.as_view(template_name = "app/login.html",
    #authentication_form = LoginForm), name = 'login'),
    path('login/', views.login_user, name = 'login'),

    #for add to cart
    path('add-to-cart/', views.add_to_cart, name = 'add-to-cart'),
    
    path('cart/', views.show_cart, name = 'showcart'), 
    path('wishlist/', views.show_wish, name = 'wishlist'), 
    path('checkout/', views.checkout.as_view(), name = 'checkout'),
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),
    path('pluswishlist/', views.plus_wishlist),
    path('minuswishlist/', views.minus_wishlist),
    path("comments/", views.Comment.as_view(), name = "comments"),


    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name = 'app/changepassword.html',
    form_class = MyPasswordChangeForm, success_url ='/passwordchangedone'), name = 'passwordchange'),
    path('passwordchangedone/', auth_view.PasswordChangeView.as_view(template_name = 'app/passwordchangedone.html'),
    name = 'passwordchangedone'),
 
    path('logout/', views.logout_user, name = 'logout'),

    
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name = 'app/password_reset.html',
    form_class = MyPasswordResetForm), name = 'password_reset'),

    #path('password-reset/done/', auth_view.Password),


    
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

