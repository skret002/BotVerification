from django.db import models
class VerificationCode(models.Model):
    send_hash = models.CharField(max_length=150, blank=True, null=False, verbose_name="Отправленый код проверки")
    email = models.CharField(max_length=100,blank=True,null=False,verbose_name='Email')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    def __str__(self):
        return f"Email - {self.email} Отправленный код - {self.send_hash} Создано - {self.created_at} Обновлено - {self.updated_at}"

    class Meta:
        verbose_name = 'Отправленный код для верификации'
        verbose_name_plural = 'Отправленные коды для верификации'

