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
    soldier = '0', "рядовий поліції"
    corporal = '1', "капрал поліції"
    sergeant = '2', "сержант поліції"
    staff_sergeant = '3', "старший сержант поліції"
    junior_lieutenant = '4', "молодший лейтенант поліції"
    lieutenant = '5', "лейтенант поліції"
    senior_lieutenant = '6', "старший лейтенант поліції"
    captain = '7', "капітан поліції"
    major = '8', "майор поліції"
    lieutenant_colonel = '9', "підполковник поліції"
    colonel = '10', "полковник поліції"
    general_3rd_rank = '11', "генерал поліції 3 рангу"


class IssuerChoice(models.TextChoices):
    NPD = '0', 'НПУ'
    DPS = '1', 'ДПО'
    UPO = '2', 'УПО'


class EncouragementChoice(models.TextChoices):
    completion_of_the_disciplinary_contract = '0', "Дострокове зняття дисциплінарного стягнення"
    listed_on_the_board = '1', "Занесення на дошку пошани"
    reword_money = '2', "Заохочення грошовою винагородою"
    reword_gift = '3', "Заохочення цінним подарунком"
    vacation = '4', "Надання додаткової плачуваної відпустки тривалістю до п\'яти діб"
    departmental_awards_of_the_National_Police_of_Ukraine = '5', "Заохочення відомчими заохочувальними відзнаками Національної поліції України"
    departmental_awards_of_the_Ministry_of_Internal_Affairs_of_Ukraine = '6', "Заохочення відомчими заохочувальними відзнаками Міністерства внутрішніх справ України"
    early_assignment_of_rank = '7', "Дострокове присвоєння чергового спеціального звання"
    assignment_of_the_title_higher_by_one_degree = '8', "Присвоєння спеціального звання, вищого на одну ступінь від звання, передбаченого займаною штатною посадою"
    firearm = '9', "Заохочення відомчою заохочувальною відзнакою Міністерства внутрішніх справа України \'Вогнепальна зброя'"
    cold_weapon = '10', "Заохочення відомчою заохочувальною відзнакою Міністерства внутрішніх справа України \'Холодна зброя'"


class Encouragement(models.Model):
    completion_of_the_disciplinary_contract = "Дострокове зняття дисциплінарного стягнення"
    listed_on_the_board = "Занесення на дошку пошани"
    reword_money = "Заохочення грошовою винагородою"
    reword_gift = "Заохочення цінним подарунком"
    vacation = "Надання додаткової плачуваної відпустки тривалістю до п\'яти діб"
    departmental_awards_of_the_National_Police_of_Ukraine = "Заохочення відомчими заохочувальними відзнаками Національної поліції України"
    departmental_awards_of_the_Ministry_of_Internal_Affairs_of_Ukraine = "Заохочення відомчими заохочувальними відзнаками Міністерства внутрішніх справ України"
    early_assignment_of_rank = "Дострокове присвоєння чергового спеціального звання"
    assignment_of_the_title_higher_by_one_degree = "Присвоєння спеціального звання, вищого на одну ступінь від звання, передбаченого займаною штатною посадою"
    firearm = "Заохочення відомчою заохочувальною відзнакою Міністерства внутрішніх справа України \'Вогнепальна зброя'"
    cold_weapon = "Заохочення відомчою заохочувальною відзнакою Міністерства внутрішніх справа України \'Холодна зброя'"
    EncouragementChoice = [
        (completion_of_the_disciplinary_contract, "Дострокове зняття дисциплінарного стягнення"),
        (listed_on_the_board, "Занесення на дошку пошани"),
        (reword_money, "Заохочення грошовою винагородою"),
        (reword_gift, "Заохочення цінним подарунком"),
        (vacation, "Надання додаткової плачуваної відпустки тривалістю до п\'яти діб"),
        (departmental_awards_of_the_National_Police_of_Ukraine,
         "Заохочення відомчими заохочувальними відзнаками Національної поліції України"),
        (departmental_awards_of_the_Ministry_of_Internal_Affairs_of_Ukraine,
         "Заохочення відомчими заохочувальними відзнаками Міністерства внутрішніх справ України"),
        (early_assignment_of_rank, "Дострокове присвоєння чергового спеціального звання"),
        (assignment_of_the_title_higher_by_one_degree,
         "Присвоєння спеціального звання, вищого на одну ступінь від звання, передбаченого займаною штатною посадою"),
        (firearm,
         "Заохочення відомчою заохочувальною відзнакою Міністерства внутрішніх справа України \'Вогнепальна зброя'"),
        (cold_weapon,
         "Заохочення відомчою заохочувальною відзнакою Міністерства внутрішніх справа України \'Холодна зброя'"),
    ]
    kind_of_encouragement = models.CharField(choices=EncouragementChoice, blank=True, max_length=110)
    order = models.CharField(max_length=100, blank=True)
    date_of_the_order = models.DateField(auto_now=False, auto_now_add=False)
    NPD = 'НПУ'
    DPS = 'ДПО'
    UPO = 'УПО'
    IssuerChoice = [
        (NPD, 'НПУ'),
        (DPS, 'ДПО'),
        (UPO, 'УПО]'),
        ]
    Issuer_of_the_order = models.CharField(choices=IssuerChoice, blank=True, max_length=3)


class TypeOfRecovery(models.Model):
    remark = 'Зауваження'
    reprimand = 'Догана'
    severe_reprimand = "Сувора догана"
    warning = "Попередження про неповну посадову відповідність"
    demotion = "Пониження у спеціальному званні на одну ступінь"
    dismissal_from_office = "Звільнення з посада"
    dismissal_from_the_police = "Звільнення зі служби в поліції"
    TypeOfRecoveryChoice = [
        (remark, 'Зауваження'),
        (reprimand, 'Догана'),
        (severe_reprimand, "Сувора догана"),
        (warning, "Попередження про неповну посадову відповідність"),
        (demotion, "Пониження у спеціальному званні на одну ступінь"),
        (dismissal_from_office, "Звільнення з посада"),
        (dismissal_from_the_police, "Звільнення зі служби в поліції"),
    ]
    type_of_recovery = models.CharField(choices=TypeOfRecoveryChoice, blank=True, max_length=50)
    order = models.CharField(max_length=100, blank=True)
    date_of_the_order = models.DateField(auto_now=False, auto_now_add=False)
    NPD = 'НПУ'
    DPS = 'ДПО'
    UPO = 'УПО'
    IssuerChoice = [
        (NPD, 'НПУ'),
        (DPS, 'ДПО'),
        (UPO, 'УПО]'),
        ]
    Issuer_of_the_order = models.CharField(choices=IssuerChoice, blank=True, max_length=3)


class Vocation(models.Model):
    order = models.CharField(max_length=10, blank=True)
    date_of_the_order = models.DateField(auto_now=False, auto_now_add=False)
    number_of_days = models.IntegerField(blank=True)
    vacation_start_date = models.DateField(auto_now=False, auto_now_add=False)
    vacation_end_date = models.DateField(auto_now=False, auto_now_add=False)


class Position(models.Model):
    police_response_platoon = "поліцейський взводу реагування"
    a_police_officer_of_the_guard_platoon = "поліцейський взводу ОО та ПБ"
    police_driver = "поліцейський - водій ВР"
    junior_inspector_of_the_security_platoon = "молодший інспектор взводу ОО та ПБ"
    response_platoon_junior_inspector = "молодший інспектор ВР"
    security_platoon_inspector = "інспектор взводу ОО та ПБ"
    deputy_platoon_commander = "заступник командира взводу"
    platoon_leader = "командир взводу"
    company_commander = "командир роти"
    deputy_company_commander = "заступник командира роти"
    battalion_commander = "командир батальйону"
    deputy_battalion_commander = "заступник командира батальйону"
    PositionCategory = [
        (police_response_platoon, "поліцейський взводу реагування"),
        (a_police_officer_of_the_guard_platoon, "поліцейський взводу ОО та ПБ"),
        (police_driver, "поліцейський - водій ВР"),
        (junior_inspector_of_the_security_platoon, "молодший інспектор взводу ОО та ПБ"),
        (response_platoon_junior_inspector, "молодший інспектор ВР"),
        (security_platoon_inspector, "інспектор взводу ОО та ПБ"),
        (deputy_platoon_commander, "заступник командира взводу"),
        (platoon_leader, "командир взводу"),
        (company_commander, "командир роти"),
        (deputy_company_commander, "заступник командира роти"),
        (battalion_commander, "командир батальйону"),
        (deputy_battalion_commander, "заступник командира батальйону"),
    ]
    available_position = models.CharField(choices=PositionCategory, default=a_police_officer_of_the_guard_platoon, max_length=40)
    junior_senior_staff = "МНС"
    senior_staff = "НС"
    PersonnelCategory = [
        (junior_senior_staff, "МНС"),
        (senior_staff, "НС"),
    ]
    position_category = models.CharField(choices=PersonnelCategory, default=junior_senior_staff,
                                         max_length=20)
    appointment_date = models.DateField(auto_now=False, auto_now_add=False)
    appointment_order = models.CharField(max_length=10, blank=True)
    NPD = 'НПУ'
    DPS = 'ДПО'
    UPO = 'УПО'
    IssuerChoice = [
        (NPD, 'НПУ'),
        (DPS, 'ДПО'),
        (UPO, 'УПО]'),
    ]
    Issuer_of_the_order = models.CharField(choices=IssuerChoice, max_length=3)


class Rank(models.Model):
    rank = models.CharField(choices=RankChoice.choices, default=RankChoice.soldier, max_length=27)
    date_of_the_order = models.DateField(auto_now=False, auto_now_add=False)
    order = models.CharField(max_length=100, blank=True)
    Issuer_of_the_order = models.CharField(choices=IssuerChoice.choices, default=IssuerChoice.UPO, max_length=5)


class Family(models.Model):
    mother = models.CharField(max_length=100, blank=True)
    father = models.CharField(max_length=100, blank=True)
    wife = models.CharField(max_length=100, blank=True)
    son = models.CharField(max_length=100, blank=True)
    daughter = models.CharField(max_length=100, blank=True)
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
    family_camp = models.CharField(choices=FamilyChoice.choices, default=FamilyChoice.unmarried, max_length=15)


class Education(models.Model):
    educational_institution = models.CharField(max_length=100, blank=True)
    date_of_entry = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    date_of_graduation_from_the_educational_institution = models.DateField(auto_now=False, auto_now_add=False,
                                                                           blank=True)
    document_about_education = models.CharField(max_length=100)
    specialty = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    form_of_education = models.CharField(max_length=20)


class EducationPolice(models.Model):
    educational_institution = models.CharField(max_length=100, blank=True)
    date_of_entry = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    date_of_graduation_from_the_educational_institution = models.DateField(auto_now=False, auto_now_add=False,
                                                                           blank=True)
    retraining_educational_institution = models.CharField(max_length=100, blank=True)
    retraining_specialty = models.CharField(max_length=100, blank=True)
    date_of_entry_retraining = models.DateField(auto_now=False, auto_now_add=False)
    date_of_graduation_from_the_retraining = models.DateField(auto_now=False, auto_now_add=False)


class FramesPolice(models.Model):
    number_private_business = models.IntegerField(blank=True)
    subdivision = models.CharField(choices=SubdivisionChoice.choices, default=SubdivisionChoice.UGSO, max_length=5)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    Surname = models.CharField(max_length=20)
    First_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=20)
    special_number = models.IntegerField(unique=True, blank=True)
    sex = models.CharField(max_length=9)
    date_of_recruitment = models.DateField(auto_now=False, auto_now_add=False)
    date_of_call_of_the_service = models.DateField(auto_now=False, auto_now_add=False)
    nationality = models.CharField(max_length=20)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    city_of_people = models.CharField(max_length=30)
    Archive = models.FileField(upload_to='archive/%Y/%m/%d/', blank=True)
