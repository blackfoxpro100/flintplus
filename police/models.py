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
    soldier = '0', 'рядовий'
    corporal = '1', 'капрал'
    sergeant = '2', 'сержант'



class Police (models.Model):
    number_private_business = models.IntegerField(max_length=6)
    subdivision = models.CharField(choices=SubdivisionChoice.choices, default=SubdivisionChoice.UGSO,)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    Surname = models.CharField(max_length=20)
    First_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=20)
    special_number = models.IntegerField(max_length=9, unique=True, blank=False)
    # rank
    sex = models.CharField(max_length=9)
    date_of_recruitment = models.DateField(auto_now=False, auto_now_add=False)
    date_of_call_of_the_service = models.DateField(auto_now=False, auto_now_add=False)
    nationality = models.CharField(max_length=20)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    city_of_people = models.CharField(max_length=30)
    family_camp = models.CharField(choices=FamilyChoice.choices, default=FamilyChoice.unmarried,)



