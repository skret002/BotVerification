from .models import VerificationCode
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from .serializers import RigOptionSerializer,RigForUserSerializer
from license.views import LicenseAll
from BotVerification.services.services import  get_user_profile,apply_new_option,get_realtime_option,get_full_data
import logging
logger = logging.getLogger('django')

class SendMail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        r_data=request.query_params
        user_data=get_user_profile(r_data)
        if user_data is not False:
            user_name,user_id,time_offset=user_data
        else:
            logger.info("Попытка добавления не существующего аккаунта")
            return Response({'status':'False','user_name':user_name,'user_id':user_id})
        try:
            email=VerificationCode.objects.get(email=request.query_params['email']).email
        except ObjectDoesNotExist:
            VerificationCode.objects.create(email=request.query_params['email'],
                                            send_hash = request.query_params['hash']
                                            )
            email=request.query_params['email']
        message = f"Your authorization code {request.query_params['hash']} for SmartBox bot"
        send_mail(u'SmartBoxBot sent you the code ',message, settings.EMAIL_HOST_USER, [email])
        logger.info(f"Регистрация юзера {user_name} c id {user_id} прошла успешно")
        return Response({'status':'Done','user_name':user_name,'user_id':user_id,'time_offset':time_offset})

class GetRigForUser(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        queryset = get_full_data(request.query_params["email"])
        serializer_class = RigForUserSerializer(queryset, many=True)
        return Response(serializer_class.data)

#@clear_rig_massage
class NewOptionFromBot(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        if apply_new_option(request.query_params) is True:
            return Response('Done')
        logger.error("An error was detected in the rig data ")
        return Response('An error was detected in the rig data')

class GetOptionSinglRig(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        q_set=get_realtime_option(request.query_params)
        if q_set is not False:
            return Response(RigOptionSerializer(q_set).data)
        return Response('No data')
class LicenseAllBot(LicenseAll):
 ...

