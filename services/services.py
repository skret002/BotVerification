from FanData.models import Profile as ProfileCustom
from FanData.views import set_new_status_option
from FanData.models import RigName,SetModeFan,SetMode0,SetMode2,KeyMaster
def get_user_profile(r_data: dict) -> tuple:
    try:
        user_obj=ProfileCustom.objects.get(user__email = r_data['email'])
        user_name=user_obj.user.username
        user_id=user_obj.user.pk
        time_offset=user_obj.time_offset
        return(user_name,user_id,time_offset)
    except ProfileCustom.DoesNotExist:
        return False

def apply_new_option(r: object) -> bool:
    rig=KeyMaster.objects.select_related('key_for_rig').get(key = r['key_license']).key_for_rig
    rig.mod_option_hive =0
    rig.save()
    modFan = SetModeFan.objects.filter(pk = rig.SetModeFan_id)
    modOption = SetMode0.objects.filter(pk = rig.SetMode0_id)
    modOption.update(terget_temp_min = r["terget_temp_min"],
                        terget_temp_max = r["terget_temp_max"],
                        min_fan_rpm = r["min_fan_rpm"],
                        critical_temp=r["critical_temp"],
                        target_mem = r["target_mem"],
                        boost=r["boost"]
                        )
    modOption2 = SetMode2.objects.filter(pk = rig.SetMode2_id)
    modOption2.update(SetRpm = r["SetRpm"])
    modFan.update( selected_mod= r["selected_mod"])
    set_new_status_option(rig.id)
    return True

def get_realtime_option(r: object) -> object:
    try:
        return RigName.objects.get(pk = KeyMaster.objects.select_related('key_for_rig').get(key = r['key']).key_for_rig.id)
    except AttributeError:
        return False
def get_full_data(email: str) ->object:
    return RigName.objects.filter(user__user__email=email)