from django.db import models

class ActiveUserDetail(models.Model):
    ip = models.GenericIPAddressField(verbose_name="IP Address")
    is_user = models.BooleanField(verbose_name="User ?", default=False)
    visited_time = models.DateTimeField(verbose_name="Visited Time")

    class Meta:
        db_table = "ActiveUserDetail"
        verbose_name_plural = "Active_Users_Detail"