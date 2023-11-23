from django.urls import path
from rest_framework import routers
from .views import GetRigForUser, SendMail,NewOptionFromBot,LicenseAllBot,GetOptionSinglRig
#
router = routers.DefaultRouter()
##router.register(r'type_lcd', TypeLcdViewSet)
#
# URLs настраиваются автоматически роутером
##urlpatterns = router.urls
#

urlpatterns = [
    path(r'mail_for_bot/', SendMail.as_view()),
    path(r'get_all_rig_name/', GetRigForUser.as_view()),
    path(r'set_option_rig_from_bot/', NewOptionFromBot.as_view()),
    path(r'license_all_bot/', LicenseAllBot.as_view()),
    path(r'get_opt_rig_for_bot/', GetOptionSinglRig.as_view()),
]+router.urls