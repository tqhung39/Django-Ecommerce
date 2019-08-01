from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth.models import User

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    path('', include('core.urls', namespace='core')),
    path('api/item/', include(('core.api.item.urls',
                               'core-api-item'), namespace='core-api-item')),
    path('api/order/', include(('core.api.order.urls',
                                'core-api-order'), namespace='core-api-order')),
    path('api/coupon/', include(('core.api.coupon.urls',
                                 'core-api-coupon'), namespace='core-api-coupon')),
    path('api/orderitem/', include(('core.api.orderitem.urls',
                                    'core-api-orderitem'), namespace='core-api-orderitem')),
    path('api/user/', include(('core.api.account.urls',
                               'core-api-account'), namespace='core-api-account')),
    path('api/cart/', include(('core.api.cart.urls',
                               'core-api-cart'), namespace='core-api-cart')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
