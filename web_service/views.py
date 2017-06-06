#!/usr/bin/env Python
# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json
from .models import *
from django.db.models import Q

def index(request):
    
    return render(request,'search_online.html')

def get_json_response(request, json_rsp):
    return HttpResponse(json.dumps(json_rsp), content_type='application/json')

## 医院别名查询
def search_hospital(request):
    
    if request.method != 'POST':
            return get_json_response(request, dict(status='error', message='only POST method supported.', data=None))
    search_hospital_name = request.POST.get('name',None)
    
    if not search_hospital_name:
        return get_json_response(request, dict(status='error', message='search_hospital_name not found.', data=None))
    
    his_list =[]
    hospital = MedicalTestHospitalAlias.objects.filter(test_hospital_alias_name__icontains = search_hospital_name)
    for _ in hospital:
        hospital_idx_id = _.hospital_idx_id
        test_hospital_name = _.test_hospital_name
        his_data = {
            'hospital_idx_id':hospital_idx_id,
            'test_hospital_name':test_hospital_name
        }
        his_list.append(his_data)
    rst_data = {
        "data":his_list
    }
    return get_json_response(request, dict(status='1', message='ok', data=rst_data))

##医院详细信息查询
def search_hospital_dict(request):
    
    if request.method != 'POST':
            return get_json_response(request, dict(status='error', message='only POST method supported.', data=None))
    hospital_idx_id = request.POST.get('hospital_idx_id',None)
    if not hospital_idx_id:
        return get_json_response(request, dict(status='error', message='hospital_idx_id not found.', data=None))
    
    his_list =[]
    hospital_dict = MedicalTestHospital.objects.filter(hospital_idx_id = hospital_idx_id)
    for _ in hospital_dict:
        hospital_id = _.hospital_id
        hospital_idx_id = _.hospital_idx_id
        hospital_name = _.hospital_name
        hospital_address = _.hospital_address
        hospital_level = _.hospital_level
        hospital_phone = _.hospital_phone
        hospital_special = _.hospital_special
        his_data =  {
            'hospital_id':hospital_id,
            'hospital_idx_id':hospital_idx_id,
            'hospital_name':hospital_name,
            'hospital_address':hospital_address,
            'hospital_level':hospital_level,
            'hospital_phone':hospital_phone,
            'hospital_special':hospital_special
        }
        his_list.append(his_data)
    rst_data = {
        "data":his_list
    }
    return get_json_response(request, dict(status='1', message='ok', data=rst_data))

## 疾病
def search_disease(request):
    
    if request.method != 'POST':
            return get_json_response(request, dict(status='error', message='only POST method supported.', data=None))
    name = request.POST.get('name',None)
    if not name:
        return get_json_response(request, dict(status='error', message='name not found.', data=None))

    dis_list = []
    disease = MedicalTestDisease.objects.filter(disease_name__icontains = name)
    for _ in disease:
        disease_id = _.id
        disease_name = _.disease_name
        dis_data = {
            'disease_id':disease_id,
            'disease_name':disease_name
        }
        dis_list.append(dis_data)
    rst_data = {
        "data":dis_list
    }
    return get_json_response(request, dict(status='1', message='ok', data=rst_data))

## 疾病详情
def search_disease_dict(request):
    
    if request.method != 'POST':
            return get_json_response(request, dict(status='error', message='only POST method supported.', data=None))
    disease_id = request.POST.get('disease_id',None)
    if not disease_id:
        return get_json_response(request, dict(status='error', message='disease_id not found.', data=None))

    dis_list = []
    disease = MedicalTestDisease.objects.filter(id = disease_id)
    for _ in disease:
        disease_id = _.id
        category_name = _.category_name
        child_name = _.child_name
        disease_name = _.disease_name
        disease_alias_name = _.disease_alias_name
        disease_summary = _.disease_summary
        department_name = _.department_name
        symptom_name = _.symptom_name
        susceptible_population = _.susceptible_population
        mode_of_infection = _.mode_of_infection
        therapy_name = _.therapy_name
        drug_name = _.drug_name
        about_disease_name = _.about_disease_name
        inspect_name = _.inspect_name

        dis_data = {
            'disease_id':disease_id,
            'category_name':category_name,
            'child_name':child_name,
            'disease_name':disease_name,
            'disease_alias_name':disease_alias_name,
            'disease_summary':disease_summary,
            'department_name':department_name,
            'symptom_name':symptom_name,
            'susceptible_population':susceptible_population,
            'mode_of_infection':mode_of_infection,
            'therapy_name':therapy_name,
            'drug_name':drug_name,
            'about_disease_name':about_disease_name,
            'inspect_name':inspect_name
        }
        dis_list.append(dis_data)
    rst_data = {
        "data":dis_list
    }
    return get_json_response(request, dict(status='1', message='ok', data=rst_data))


##疾病药物详情

def search_Drugs_dict_test(request):
    if request.method != 'POST':
            return get_json_response(request, dict(status='error', message='only POST method supported.', data=None))
    name = request.POST.get('name',None)
    if not name:
        return get_json_response(request, dict(status='error', message='name not found.', data=None))

    drugs_list = []
    drugs = RefDrugDict.objects.filter(Q(cnname__contains = name)|Q(commonname__contains = name))
    for _ in drugs:
        id = _.id
        cnname = _.cnname
        commonname = _.commonname
        engname = _.engname
        showname = _.showname
        component = _.component
        indication = _.indication
        dosage = _.dosage
        contraindications = _.contraindications
        precautions = _.precautions
        adverseReactions = _.adversereactions
        drugInteractions = _.druginteractions
        drugs_data = {
            'id':id,
            'cnname':cnname,
            'commonname':commonname,
            'engname':engname,
            'showname':showname,
            'component':component,
            'indication':indication,
            'dosage':dosage,
            'contraindications':contraindications,
            'precautions':precautions,
            'adverseReactions':adverseReactions,
            'drugInteractions':drugInteractions
        }
        drugs_list.append(drugs_data)
    rst_data = {
        "data":drugs_list
    }
    return get_json_response(request, dict(status='1', message='ok', data=rst_data)) 

## 药品别名表查询
def search_Drugs_alias(request):
    
    if request.method != 'POST':
            return get_json_response(request, dict(status='error', message='only POST method supported.', data=None))
    Drugs_name = request.POST.get('name',None)
    if not Drugs_name:
        return get_json_response(request, dict(status='error', message='Drugs_name not found.', data=None))
    
    drugs_list = []
    drugs = RefDrugAliasDict.objects.filter(drug_alias__icontains = Drugs_name)
    for _ in drugs:
        drug_id = _.drug_id
        drug_common_name = _.drug_common_name
        drug_data = {
            'drug_id':drug_id,
            'drug_common_name':drug_common_name
        }
        drugs_list.append(drug_data)
    rst_data = {
        "data":drugs_list
    }
    return get_json_response(request, dict(status='1', message='ok', data=rst_data))

##药品详细信息查询
def search_Drugs_dict(request):
    
    if request.method != 'POST':
            return get_json_response(request, dict(status='error', message='only POST method supported.', data=None))
    id = request.POST.get('drug_id',None)
    if not id:
        return get_json_response(request, dict(status='error', message='id not found.', data=None))

    drugs_list = []
    drugs = RefDrugDict.objects.filter(id = id)
    for _ in drugs:
        id = _.id
        cnname = _.cnname
        commonname = _.commonname
        engname = _.engname
        showname = _.showname
        component = _.component
        indication = _.indication
        dosage = _.dosage
        contraindications = _.contraindications
        precautions = _.precautions
        adverseReactions = _.adversereactions
        drugInteractions = _.druginteractions
        drugs_data = {
            'id':id,
            'cnname':cnname,
            'commonname':commonname,
            'engname':engname,
            'showname':showname,
            'component':component,
            'indication':indication,
            'dosage':dosage,
            'contraindications':contraindications,
            'precautions':precautions,
            'adverseReactions':adverseReactions,
            'drugInteractions':drugInteractions
        }
        drugs_list.append(drugs_data)
    rst_data = {
        "data":drugs_list
    }
    return get_json_response(request, dict(status='1', message='ok', data=rst_data))   


##指标别名检索

def medical_test_index_alias_dict(request):
    
    if request.method != 'POST':
        return get_json_response(request, dict(status='error', message='only POST method supported.', data=None))
    test_idx_alias = request.POST.get('name',None)
    if not test_idx_alias:
        return get_json_response(request, dict(status='error', message='test_idx_name is None.', data=None))

    medical_list = []
    medical_dict = MedicalTestIndexAliasDict.objects.filter(test_idx_alias__icontains = test_idx_alias)
    for _ in medical_dict:
        test_idx_id = _.test_idx_id
        test_idx_name = _.test_idx_name
        test_idx_alias = _.test_idx_alias
        medical_data = {
            'test_idx_id':test_idx_id,
            'test_idx_name':test_idx_name,
            'test_idx_alias':test_idx_alias
        }
        medical_list.append(medical_data)
    rst_data = {
        "data":medical_list
    }
    return get_json_response(request, dict(status='1', message='ok', data=rst_data)) 

##根据别名检测主表信息

def medical_test_index_dict(request):

    if request.method != 'POST':
        return get_json_response(request, dict(status='error', message='only POST method supported.', data=None))

    test_idx_id = request.POST.get('id',None)
    if not test_idx_id:
        return get_json_response(request, dict(status='error', message='id is None.', data = None))
    medical_list = []
    medical_dict = MedicalTestIndexDict.objects.filter(test_idx_id = test_idx_id)
    for _ in medical_dict:
        test_idx_id = _.test_idx_id
        test_idx_name = _.test_idx_name
        testprinciple = _.testprinciple
        normalvaluedescription = _.normalvaluedescription
        diseaserelated = _.diseaserelated
        summary = _.summary
        testdescription = _.testdescription
        medical_data = {
            'test_idx_id':test_idx_id,
            'test_idx_name':test_idx_name,
            'testprinciple':testprinciple,
            'normalvaluedescription':normalvaluedescription,
            'diseaserelated':diseaserelated,
            'summary':summary,
            'testdescription':testdescription
        }
    medical_list.append(medical_data)
    rst_data = {
        "data":medical_list
    }
    return get_json_response(request, dict(status='1', message='ok', data=rst_data)) 