from django.db import models


class FamilyChoice(models.TextChoices):
    unmarried = '1', 'Неодружений'
    married = '2', 'Одружений'
    divorced = '3', 'Розлучений'


class SubdivisionChoice(models.TextChoices):
    UGSO = '1', "Управління поліції охорони"
    Kramatorsk = '2', "Краматорське районне відділення"
    Slovyansk = '3', "Слов'янське міське відділення"
    Bahmut = '4', "Бахмутське міжрайонне відділення"


class RankChoice(models.TextChoices):
    soldier = '0', 'рядовий поліції'
    corporal = '1', 'капрал поліції'
    sergeant = '2', 'сержант поліції'
    staff_sergeant = '3', 'старший сержант поліції'
    junior_lieutenant = '4', 'молодший лейтенант поліції'
    lieutenant = '5', 'лейтенант поліції'
    senior_lieutenant = '6', 'старший лейтенант поліції'
    captain = '7', 'капітан поліції'
    major = '8', 'майор поліції'
    lieutenant_colonel = '9', 'підполковник поліції'
    colonel = '10', 'полковник поліції'
    general_3rd_rank = '11', 'генерал поліції 3 рангу'


class Family (models.Model):
    mother = models.CharField(max_length=100, blank=True)
    father = models.CharField(max_length=100, blank=True)
    wife = models.CharField(max_length=100, blank=True)
    son = models.CharField(max_length=100, blank=True)
    daughter = models.CharField(max_length=100,blank=True)
    date_of_birth_mother = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    date_of_birth_father = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    date_of_birth_wife = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    date_of_birth_son = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    date_of_birth_daughter = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    place_of_birth_mother = models.CharField(max_length=150, blank=True)
    place_of_birth_father = models.CharField(max_length=150, blank=True)
    place_of_birth_wife = models.CharField(max_length=150, blank=True)
    place_of_birth_son = models.CharField(max_length=150, blank=True)
    place_of_birth_daughter = models.CharField(max_length=150, blank=True)
    position_mother = models.CharField(max_length=50, blank=True)
    position_father = models.CharField(max_length=50, blank=True)
    position_wife = models.CharField(max_length=50, blank=True)
    position_son = models.CharField(max_length=50, blank=True)
    position_daughter = models.CharField(max_length=50, blank=True)
    job_mother = models.CharField(max_length=50, blank=True)
    job_father = models.CharField(max_length=50, blank=True)
    job_wife = models.CharField(max_length=50, blank=True)
    job_son = models.CharField(max_length=50, blank=True)
    job_daughter = models.CharField(max_length=50, blank=True)
    place_of_registration_mother = models.CharField(max_length=150, blank=True)
    place_of_registration_father = models.CharField(max_length=150, blank=True)
    place_of_registration_wife = models.CharField(max_length=150, blank=True)
    place_of_registration_son = models.CharField(max_length=150, blank=True)
    place_of_registration_daughter = models.CharField(max_length=150, blank=True)
    place_of_actual_residence_mother = models.CharField(max_length=150, blank=True)
    place_of_actual_residence_father = models.CharField(max_length=150, blank=True)
    place_of_actual_residence_wife = models.CharField(max_length=150, blank=True)
    place_of_actual_residence_son = models.CharField(max_length=150, blank=True)
    place_of_actual_residence_daughter = models.CharField(max_length=150, blank=True)


class Education(models.Model):
    educational_institution = models.CharField()


class FramesPolice (models.Model):
    number_private_business = models.IntegerField(max_length=6)
    subdivision = models.CharField(choices=SubdivisionChoice.choices, default=SubdivisionChoice.UGSO,)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    Surname = models.CharField(max_length=20)
    First_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=20)
    special_number = models.IntegerField(max_length=9, unique=True, blank=False)
    rank = models.CharField(choices=RankChoice.choices, default=RankChoice.soldier,)
    sex = models.CharField(max_length=9)
    date_of_recruitment = models.DateField(auto_now=False, auto_now_add=False)
    date_of_call_of_the_service = models.DateField(auto_now=False, auto_now_add=False)
    nationality = models.CharField(max_length=20)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    city_of_people = models.CharField(max_length=30)
    family_camp = models.CharField(choices=FamilyChoice.choices, default=FamilyChoice.unmarried,)
    Archive = models.FileField(upload_to='archive/%Y/%m/%d/', blank=True)


