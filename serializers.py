from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from FanData.models import RigName
class RigSerializerData(serializers.ModelSerializer):
    class Meta:
        depth = 9
        model = RigName
        fields = ['rigId','rigName','mod_option_hive','rig_online_status','hotGPU','hotMem','softVersion',
                  'AlertFan','SystemMessages','SetModeFan','AlertFan','historyBoardFan']
class RigForUserSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 9
        model = RigName
        fields = ['rigId','rigName']        
class RigOptionSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 9
        model = RigName
        fields = ['rigId','rigName','mod_option_hive','device_name','AlertFan','SetModeFan','SetMode0',
                  'SetMode2','softVersion','hotGPU','hotMem','historyBoardFan','rig_online_status']