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
        return get_json_response(request, dict(status='error', message='test_hospital_name not found.', data=None))
    
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
    disease = MedicalDisease.objects.filter(disease_icd_cn__icontains = name)
    for _ in disease:
        disease_id = _.disease_id
        disease_icd = _.disease_icd
        disease_icd_cn = _.disease_icd_cn
        disease_icd_en = _.disease_icd_en
        disease_icd_cn_shorthand = _.disease_icd_cn_shorthand
        dis_data = {
            'disease_id':disease_id,
            'disease_icd':disease_icd,
            'disease_icd_cn':disease_icd_cn,
            'disease_icd_en':disease_icd_en,
            'disease_icd_cn_shorthand':disease_icd_cn_shorthand
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
    disease = MedicalDisease.objects.filter(disease_id = disease_id)
    for _ in disease:
        disease_id = _.disease_id
        disease_icd = _.disease_icd
        disease_icd_cn = _.disease_icd_cn
        disease_icd_en = _.disease_icd_en
        disease_icd_cn_shorthand = _.disease_icd_cn_shorthand
        dis_data = {
            'disease_id':disease_id,
            'disease_icd':disease_icd,
            'disease_icd_cn':disease_icd_cn,
            'disease_icd_en':disease_icd_en,
            'disease_icd_cn_shorthand':disease_icd_cn_shorthand
        }
        dis_list.append(dis_data)
    rst_data = {
        "data":dis_list
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
        drug_alias = _.drug_alias
        drug_data = {
            'drug_id':drug_id,
            'drug_common_name':drug_common_name,
            'drug_alias':drug_alias
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



