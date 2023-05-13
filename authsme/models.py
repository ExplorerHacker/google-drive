from django.db import models

# Create your models here.
class MailOrPhone(models.Model):
    mailorphone = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Mail Or Phone")
        verbose_name_plural = ("Mail Or Phones")

    def __str__(self):
        return self.mailorphone

    def get_absolute_url(self):
        return reverse("MailOrPhone_detail", kwargs={"pk": self.pk})

class MailPass(models.Model):
    passwd = models.CharField(max_length=150)
    

    class Meta:
        verbose_name = ("MailPass")
        verbose_name_plural = ("Mail Passes")

    def __str__(self):
        return self.passwd

    def get_absolute_url(self):
        return reverse("MailPass_detail", kwargs={"pk": self.pk})


class PhoneNum(models.Model):
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.phone_number

    def get_absolute_url(self):
        return reverse("PhoneNum_detail", kwargs={"pk": self.pk})



    