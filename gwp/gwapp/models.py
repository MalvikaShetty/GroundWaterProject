from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager
# Create your models here.


class UserBasic(models.Model):
    userID = models.CharField(max_length=50, null=False,
                              unique=True, primary_key=True)
    userFirstName = models.CharField(max_length=100)
    userLastName = models.CharField(max_length=100)
    userAddress = models.CharField(max_length=200)
    userVillage = models.CharField(max_length=200)
    userTaluka = models.CharField(max_length=200)
    userDistrict = models.CharField(max_length=200)
    userContact = models.IntegerField(null=False, unique=True)
    userEmail = models.EmailField(max_length=200, unique=True, null=False)
    userPassword = models.CharField(max_length=200, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.userFirstName

    class Meta:
        verbose_name_plural = "User"


class UserOtherInfo(models.Model):
    userID = models.ForeignKey(UserBasic, on_delete=models.CASCADE)
    userTotalFamilyMembers = models.IntegerField(null=True)
    userAdultFamMembers = models.IntegerField(null=True)
    userChildrenFamMembers = models.IntegerField(null=True)
    userAreaOfLandOwned = models.DecimalField(max_digits=20, decimal_places=3, null=True)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Other User Info"


class UserWellRegistration(models.Model):
    userID = models.ForeignKey(UserBasic, on_delete=models.CASCADE)
    userWellID = models.CharField(max_length=200, null=True)
    userWellType = models.CharField(max_length=50)  # Private or public
    # userBorewellID = models.CharField(max_length=200, null=True)
    # userBorewellType = models.CharField(max_length=50)

    objects = models.Manager()


class UserWaterUsage(models.Model):
    userID = models.ForeignKey(UserBasic, on_delete=models.CASCADE)
    userWellID = models.ForeignKey(UserWellRegistration, on_delete=models.CASCADE)
    # userWaterUsageDomestic =
