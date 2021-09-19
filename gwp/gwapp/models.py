from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager
# Create your models here.


#### FOR DEMO ######

class BorewellsYedshi(models.Model):
    name = models.CharField(max_length=500)
    location_lat = models.DecimalField(max_digits=20, decimal_places=5)
    location_long = models.DecimalField(max_digits=20, decimal_places=5)
    location_altitude = models.DecimalField(max_digits=20, decimal_places=5)
    location_precision = models.DecimalField(max_digits=20, decimal_places=5)
    address = models.CharField(max_length=500)
    type = models.CharField(max_length=100)
    useTime = models.IntegerField()   #in mins
    borewellFoot = models.IntegerField()

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Borewells Yedshi"

class District(models.Model):
    districtName = models.CharField(max_length=500)
    # cultivatedland etc
    # population
    def __str__(self):
        return self.districtName


class Taluka(models.Model):
    districtName = models.ForeignKey(District, on_delete=models.CASCADE)
    talukaName = models.CharField(max_length=500)

    def __str__(self):
        return self.talukaName


class Village(models.Model):
    districtName = models.ForeignKey(District, on_delete=models.CASCADE)
    talukaName = models.ForeignKey(Taluka, on_delete=models.CASCADE)
    villageName = models.CharField(max_length=500)

    def __str__(self):
        return self.villageName


##### User Data #####


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
    wellOwner = models.CharField(max_length=200)
    userdateOfWellRegistration = models.DateField()
    userWellType = models.CharField(max_length=50)  # Private or public
    userWellActiveOrInact = models.CharField(max_length=50)
    userWellDugDate = models.DateField()
    # userWelllocation = models.PointField(srid=4326)
    # usage
    # inactive
    objects = GeoManager()

class UserBorewellRegistration(models.Model):
    userID = models.ForeignKey(UserBasic, on_delete=models.CASCADE)
    userBorewellID = models.CharField(max_length=200, null=True)
    userBorewellType = models.CharField(max_length=50)



###### Village/Taluka Data ######


class Rainfall(models.Model):
    yearOfInput = models.IntegerField()
    dateOfInput = models.DateField()
    villageName = models.ForeignKey(Village, on_delete=models.CASCADE)
    averageRainfall = models.DecimalField(max_digits=20, decimal_places=3)


class GroundWaterLevelPreMonsoon(models.Model):
    yearOfInput = models.IntegerField()
    dateOfInput = models.DateField()
    villageName = models.ForeignKey(Village, on_delete=models.CASCADE)
    noOfObservationWells = models.IntegerField()
    preMonsoonLevel = models.DecimalField(max_digits=20, decimal_places=3)      #in mbgl
    totalWaterRechargedFromRainfall = models.DecimalField(max_digits=20, decimal_places=3)
    totalWaterRechargedFromSurfaceWater = models.DecimalField(max_digits=20, decimal_places=3)
    # averageFluctuation =


class GroundWaterLevelPostMonsoon(models.Model):
    yearOfInput = models.IntegerField()
    dateOfInput = models.DateField()
    villageName = models.ForeignKey(Village, on_delete=models.CASCADE)
    noOfObservationWells = models.IntegerField()
    postMonsoonLevel = models.DecimalField(max_digits=20, decimal_places=3)      #in mbgl
    totalWaterRechargedFromRainfall = models.DecimalField(max_digits=20, decimal_places=3)
    totalWaterRechargedFromSurfaceWater = models.DecimalField(max_digits=20, decimal_places=3)
    # averageFluctuation =


class Population(models.Model):
    villageName = models.ForeignKey(Village, on_delete=models.CASCADE)
    adults = models.IntegerField()
    under18 = models.IntegerField()
    seniorCitizen = models.IntegerField()
    female = models.IntegerField()
    male = models.IntegerField()
    other = models.IntegerField()


class Landuse(models.Model):
    villageName = models.ForeignKey(Village, on_delete=models.CASCADE)
    year = models.IntegerField()
    cultivatedLandArea = models.DecimalField(max_digits=20, decimal_places=3)
    uncultivatedLandArea = models.DecimalField(max_digits=20, decimal_places=3)  # which can be cultivated
    noncultivableLandArea = models.DecimalField(max_digits=20, decimal_places=3)  # which can't be cultivated
    forestArea = models.DecimalField(max_digits=20, decimal_places=3)
    otherLandUseArea = models.DecimalField(max_digits=20, decimal_places=3)


class RechargeStructures(models.Model):
    rechargeStructID = models.CharField(max_length=50, null=False, unique=True)
    villageName = models.ForeignKey(Village, on_delete=models.CASCADE)
    rechargeStructBuiltDate = models.DateField()
    rechargeStructOwnership = models.CharField(max_length=50)  # Private or public
    rechargeStructVolumePotential = models.DecimalField(max_digits=20, decimal_places=3)
    rechargeStructVolumeRecharged = models.DecimalField(max_digits=20, decimal_places=3)


class RechargeStructuresPrediction(models.Model):
    rechargeStructID = models.ForeignKey(RechargeStructures, on_delete=models.CASCADE)
    villageName = models.ForeignKey(Village, on_delete=models.CASCADE)
    rechargeStructDateOfInput = models.DateField()              #feed data quaterly or every 15 days?
    rechargeStructVolumeRecharged = models.DecimalField(max_digits=20, decimal_places=3)



# class IndustryUsage
#crops
#GWavailability
#Aquifers