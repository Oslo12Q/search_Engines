# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Areazone(models.Model):
    city_id = models.IntegerField()
    city_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'areazone'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class MedicalTestDisease(models.Model):
    id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=255, blank=True, null=True)
    child_name = models.CharField(max_length=255, blank=True, null=True)
    disease_name = models.CharField(max_length=255, blank=True, null=True)
    disease_alias_name = models.CharField(max_length=255, blank=True, null=True)
    disease_summary = models.TextField(blank=True, null=True)
    department_name = models.CharField(max_length=255, blank=True, null=True)
    symptom_name = models.CharField(max_length=255, blank=True, null=True)
    susceptible_population = models.CharField(max_length=255, blank=True, null=True)
    mode_of_infection = models.CharField(max_length=255, blank=True, null=True)
    therapy_name = models.CharField(max_length=255, blank=True, null=True)
    drug_name = models.CharField(max_length=255, blank=True, null=True)
    about_disease_name = models.CharField(max_length=255, blank=True, null=True)
    inspect_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medical__test_disease'


class MedicalDisease(models.Model):
    disease_id = models.IntegerField(primary_key=True)
    disease_icd = models.CharField(max_length=255, blank=True, null=True)
    disease_icd_cn = models.CharField(max_length=255, blank=True, null=True)
    disease_icd_en = models.CharField(max_length=255, blank=True, null=True)
    disease_icd_cn_shorthand = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medical_disease'


class MedicalHospital(models.Model):
    hospital_id = models.AutoField(primary_key=True)
    hospital_city = models.CharField(max_length=255, blank=True, null=True)
    hospital_name = models.CharField(max_length=255, blank=True, null=True)
    hospital_address = models.CharField(max_length=255, blank=True, null=True)
    hospital_grade = models.CharField(max_length=255, blank=True, null=True)
    hospital_features = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medical_hospital'


class MedicalTestCatagoryDict(models.Model):
    seqid = models.BigIntegerField(primary_key=True)
    test_cata_id = models.BigIntegerField(blank=True, null=True)
    test_cata_name = models.CharField(max_length=255, blank=True, null=True)
    test_cat1_id = models.BigIntegerField(blank=True, null=True)
    test_cat1_name = models.CharField(max_length=255, blank=True, null=True)
    test_cat2_id = models.BigIntegerField(blank=True, null=True)
    test_cat2_name = models.CharField(max_length=255, blank=True, null=True)
    test_cat3_id = models.BigIntegerField(blank=True, null=True)
    test_cat3_name = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medical_test_catagory_dict'


class MedicalTestHospital(models.Model):
    hospital_id = models.BigIntegerField(primary_key=True)
    hospital_idx_id = models.BigIntegerField(blank=True, null=True)
    hospital_province = models.CharField(max_length=255, blank=True, null=True)
    hospital_city = models.CharField(max_length=255, blank=True, null=True)
    hospital_name = models.CharField(max_length=255, blank=True, null=True)
    hospital_address = models.CharField(max_length=255, blank=True, null=True)
    hospital_level = models.CharField(max_length=255, blank=True, null=True)
    hospital_phone = models.CharField(max_length=255, blank=True, null=True)
    hospital_special = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medical_test_hospital'


class MedicalTestHospitalAlias(models.Model):
    hospital_alias_id = models.BigIntegerField(primary_key=True)
    test_hospital_alias_idx_id = models.BigIntegerField(blank=True, null=True)
    hospital_idx_id = models.BigIntegerField(blank=True, null=True)
    test_hospital_name = models.CharField(max_length=255, blank=True, null=True)
    test_hospital_alias_name = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medical_test_hospital_alias'


class MedicalTestIndexAliasDict(models.Model):
    seqid = models.BigIntegerField(primary_key=True)
    test_idx_id = models.BigIntegerField(blank=True, null=True)
    test_idx_name = models.CharField(max_length=500, blank=True, null=True)
    test_idx_alias = models.CharField(max_length=500, blank=True, null=True)
    test_cata_id = models.BigIntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medical_test_index_alias_dict'


class MedicalTestIndexDict(models.Model):
    seqid = models.BigIntegerField(primary_key=True)
    test_idx_id = models.BigIntegerField(blank=True, null=True)
    test_idx_name = models.CharField(max_length=500, blank=True, null=True)
    test_idx_name_en = models.CharField(max_length=500, blank=True, null=True)
    test_cata_id = models.BigIntegerField(blank=True, null=True)
    relation_test = models.TextField(db_column='Relation_Test', blank=True, null=True)  # Field name made lowercase.
    relation_question = models.TextField(db_column='Relation_Question', blank=True, null=True)  # Field name made lowercase.
    testwhys = models.TextField(db_column='TestWhys', blank=True, null=True)  # Field name made lowercase.
    testwhen = models.TextField(db_column='TestWhen', blank=True, null=True)  # Field name made lowercase.
    suffererprepare = models.TextField(db_column='SuffererPrepare', blank=True, null=True)  # Field name made lowercase.
    swatchgather = models.TextField(db_column='SwatchGather', blank=True, null=True)  # Field name made lowercase.
    testprinciple = models.TextField(db_column='TestPrinciple', blank=True, null=True)  # Field name made lowercase.
    normalvaluedescription = models.TextField(db_column='NormalValueDescription', blank=True, null=True)  # Field name made lowercase.
    diseaserelated = models.TextField(db_column='DiseaseRelated', blank=True, null=True)  # Field name made lowercase.
    summary = models.TextField(db_column='Summary', blank=True, null=True)  # Field name made lowercase.
    testdescription = models.TextField(db_column='TestDescription', blank=True, null=True)  # Field name made lowercase.
    resulteffectreason = models.TextField(db_column='ResultEffectReason', blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medical_test_index_dict'


class RefDrugAliasDict(models.Model):
    seqid = models.BigIntegerField(primary_key=True)
    drug_id = models.BigIntegerField(blank=True, null=True)
    drug_common_name = models.CharField(max_length=500, blank=True, null=True)
    drug_alias = models.CharField(max_length=500, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ref_drug_alias_dict'


class RefDrugDict(models.Model):
    id = models.BigIntegerField(primary_key=True)
    cnname = models.CharField(db_column='cnName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commonname = models.CharField(db_column='commonName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    engname = models.CharField(db_column='engName', max_length=140, blank=True, null=True)  # Field name made lowercase.
    vsname = models.CharField(db_column='vsName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    showname = models.CharField(db_column='showName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    othername = models.TextField(db_column='otherName', blank=True, null=True)  # Field name made lowercase.
    companyid = models.IntegerField(db_column='companyId', blank=True, null=True)  # Field name made lowercase.
    fda = models.CharField(db_column='FDA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    component = models.TextField(blank=True, null=True)
    indication = models.TextField(blank=True, null=True)
    dosage = models.TextField(blank=True, null=True)
    contraindications = models.TextField(blank=True, null=True)
    precautions = models.TextField(blank=True, null=True)
    adversereactions = models.TextField(db_column='adverseReactions', blank=True, null=True)  # Field name made lowercase.
    druginteractions = models.TextField(db_column='drugInteractions', blank=True, null=True)  # Field name made lowercase.
    forensicclassification = models.TextField(db_column='forensicClassification', blank=True, null=True)  # Field name made lowercase.
    type = models.TextField(blank=True, null=True)
    pack = models.TextField(blank=True, null=True)
    otc = models.IntegerField(db_column='OTC', blank=True, null=True)  # Field name made lowercase.
    drugtype = models.IntegerField(db_column='drugType', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='createDate', blank=True, null=True)  # Field name made lowercase.
    modifydate = models.DateTimeField(db_column='modifyDate', blank=True, null=True)  # Field name made lowercase.
    grade = models.FloatField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    picpath = models.CharField(db_column='picPath', max_length=130, blank=True, null=True)  # Field name made lowercase.
    cateid1 = models.IntegerField(db_column='cateId1', blank=True, null=True)  # Field name made lowercase.
    cateid2 = models.IntegerField(db_column='cateId2', blank=True, null=True)  # Field name made lowercase.
    cateid3 = models.IntegerField(db_column='cateId3', blank=True, null=True)  # Field name made lowercase.
    shortname1 = models.CharField(db_column='shortName1', max_length=15, blank=True, null=True)  # Field name made lowercase.
    shortname2 = models.CharField(db_column='shortName2', max_length=15, blank=True, null=True)  # Field name made lowercase.
    shortname3 = models.CharField(db_column='shortName3', max_length=15, blank=True, null=True)  # Field name made lowercase.
    fullcnname = models.CharField(db_column='fullCnName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    guidemessage = models.CharField(db_column='guideMessage', max_length=100, blank=True, null=True)  # Field name made lowercase.
    position = models.IntegerField(blank=True, null=True)
    votecount = models.IntegerField(db_column='voteCount', blank=True, null=True)  # Field name made lowercase.
    priceid = models.IntegerField(db_column='priceId', blank=True, null=True)  # Field name made lowercase.
    warning = models.TextField(blank=True, null=True)
    warninginfoid = models.CharField(db_column='warningInfoId', max_length=200, blank=True, null=True)  # Field name made lowercase.
    routeid = models.CharField(db_column='routeId', max_length=30, blank=True, null=True)  # Field name made lowercase.
    inncomponentid = models.CharField(db_column='innComponentId', max_length=30, blank=True, null=True)  # Field name made lowercase.
    drugcatetype = models.IntegerField(db_column='drugCateType', blank=True, null=True)  # Field name made lowercase.
    inncomponentname = models.CharField(db_column='innComponentName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    innfda = models.CharField(db_column='innFDA', max_length=200, blank=True, null=True)  # Field name made lowercase.
    innlrc = models.CharField(db_column='innLRC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ref_drug_dict'
