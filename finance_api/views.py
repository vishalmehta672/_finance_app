from django.shortcuts import render
from rest_framework.decorators import api_view
import requests
from django.http import JsonResponse
from rest_framework import status

@api_view(['POST'])
def create_inventory_specific_contact(request):
    
    data = request.data
    cf_occupation = data.get('occupation')
    email = data.get('email')
    lifecycle_stage_id=113000001358
    contact_status_id=112000000355
    
    
    json_data = {
        "name": data.get('first_name', '') + ' ' + data.get('last_name', ''),
        "first_name": data.get('first_name'),
        "last_name": data.get('last_name'),
        "date_of_birth":data.get("date_of_birth"),
        "address": data.get('address'),
        "city": data.get('city'),
        "state": data.get('province'),
        "country": data.get('country'),
        "zipcode": data.get('postal_code'),
        "phone": data.get('telephone'),
        "mobile_number": data.get('telephone'),
        "emails":email,
        "lifecycle_stage_id":lifecycle_stage_id ,
        "contact_status_id": contact_status_id,
        # "owner_id":112000000083,
        "is_active": True,
        "custom_field": {

            "cf_finance_that_portal_application_status":"Conditionally approved",
            "cf_signed_up_with_finance_that": "Yes",
            "cf_dealer_id": data.get('user_id'),
            "cf_date_of_birth": data.get('date_of_birth'),
            "cf_employment_status": data.get("cf_employment_status"),
            "cf_employer_name":data.get("cf_employer_name"),
            "cf_occupation": cf_occupation,
            "cf_monthly_gross_income":data.get("cf_monthly_gross_income"),
            "cf_asset_type":data.get("cf_asset_type"),
            "cf_contact_type": "Applicant / Buyer - Public"
        },
    }
    
    headers = {
    'Authorization': 'Token token=oJjfiyJt_N1x4_baiv9MMQ',
    }

    owner_data = requests.post('https://crm.financethat.ca/crm/sales/api/contacts', headers=headers, json=json_data)
    owner_data =owner_data.json()
    return JsonResponse(owner_data,status=status.HTTP_200_OK)

@api_view(['POST'])
def create_inventory_specific_deal(request):
    """Create deal"""
    data = request.data
    contacts_added_list = data.get("contacts_added_list")
    cf_finance_that_stock_id = data.get("cf_finance_that_stock_id")
    cf_credit_rating = data.get("cf_credit_rating")
    cf_asset_type_migrated = data.get("cf_asset_type_migrated")
    cf_asset_subtype = data.get("cf_asset_subtype")
    cf_odometers_reading =data.get("cf_odometers_reading")
    cf_vehicle_purchase_price_ = data.get("cf_vehicle_purchase_price_")
    cf_vehicle_vin_ = data.get("cf_vehicle_vin_")
    cf_vehicle_model = data.get("cf_vehicle_model")
    cf_vehicle_make =data.get("cf_vehicle_make")
    cf_vehicle_year = data.get("cf_vehicle_year")
    cf_finance_that_stock_number = data.get("cf_finance_that_stock_number")
    sales_account_id = data.get("sales_account_id")
    
    headers = {
    'Authorization': 'Token token=oJjfiyJt_N1x4_baiv9MMQ',
    }
    owner_data = requests.get(f'https://crm.financethat.ca/crm/sales/api/contacts/{contacts_added_list}', headers=headers)
    owner_data = owner_data.json()
    json_data = {
        'deal': {      
            "display_name": owner_data["contact"].get("first_name") +' '+ owner_data["contact"].get("last_name"),
            "name":owner_data["contact"].get("first_name") +' '+ owner_data["contact"].get("last_name"),
            "amount":data.get("amount"),
            "contacts_added_list":contacts_added_list,
            "cf_asset_type_migrated":cf_asset_type_migrated,
            "sales_account_id":sales_account_id,
            
             "custom_field": {
                "cf_finance_that_stock_id": cf_finance_that_stock_id,
                "cf_vehicle_year": cf_vehicle_year,
                "cf_vehicle_make": cf_vehicle_make,
                "cf_vehicle_model": cf_vehicle_model,
                "cf_vehicle_vin_": cf_vehicle_vin_,
                "cf_vehicle_purchase_price_": cf_vehicle_purchase_price_,
                "cf_odometers_reading":cf_odometers_reading,
                "cf_asset_type_migrated":cf_asset_type_migrated,
                "cf_asset_subtype":cf_asset_subtype,
                "cf_credit_rating":cf_credit_rating,
                "cf_finance_that_stock_number": cf_finance_that_stock_number,
        }
            },
        }

    response = requests.post('https://crm.financethat.ca/crm/sales/api/deals', headers=headers, json=json_data)
    deal_data =response.json()
    return JsonResponse(deal_data,status=status.HTTP_200_OK)


@api_view(['POST'])
def create_general_application_contact(request):
    data = request.data
    email = data.get('emails')
    lifecycle_stage_id=113000001358
    contact_status_id="112000000297"
    json_data = {
        "first_name": data.get('first_name'),
        "last_name": data.get('last_name'),
        "address": data.get('address'),
        "city": data.get("city"),
        "country":data.get("country","Canada"),
        "state": data.get('province'),
        "zipcode": data.get('postal_code'),
       "mobile_number": data.get('mobile_number'),
        "emails":email,
        "lifecycle_stage_id":lifecycle_stage_id ,
        "contact_status_id": contact_status_id,
        "is_active": True,
        "custom_field": {
            # "cf_signed_up_with_finance_that": "Yes",
            "cf_occupation": data.get('cf_occupation'),
            "cf_date_of_birth": data.get('cf_date_of_birth'),
            "cf_employment_status": data.get('cf_employment_status'),
            "cf_employer_name" : data.get('cf_employer_name'),
            "cf_monthly_gross_income":data.get("cf_monthly_gross_income"),
            "cf_contact_type": "Applicant / Buyer - Public",
            "cf_credit_rating": data.get('cf_credit_rating'),
        },
    }
    headers = {
    'Authorization': 'Token token=oJjfiyJt_N1x4_baiv9MMQ',
    }

    owner_data = requests.post('https://crm.financethat.ca/crm/sales/api/contacts', headers=headers, json=json_data)
    owner_data =owner_data.json()
    return JsonResponse({"owner_data": owner_data,"status_code":status.HTTP_200_OK})

@api_view(['POST'])
def  create_general_application_deals(request):
    data = request.data
    contacts_added_list = data.get("contacts_added_list")
    cf_asset_type_migrated = data.get("cf_asset_type_migrated")
    cf_asset_subtype = data.get("cf_asset_subtype")
    cf_credit_rating = data.get("cf_credit_rating")
    headers = {
    'Authorization': 'Token token=oJjfiyJt_N1x4_baiv9MMQ',
    }
    owner_data = requests.get(f'https://crm.financethat.ca/crm/sales/api/contacts/{contacts_added_list}', headers=headers)
    owner_data = owner_data.json()
    
    
    json_data = {
        'deal': {      
            "display_name": owner_data["contact"].get("first_name") +' '+ owner_data["contact"].get("last_name"),
            "name":owner_data["contact"].get("first_name") +' '+ owner_data["contact"].get("last_name"),
            "amount":data.get("monthly_budget"),
            "contacts_added_list":contacts_added_list,
            "cf_asset_type_migrated":cf_asset_type_migrated,
             "custom_field": {
                "cf_asset_type_migrated":cf_asset_type_migrated,
                "cf_asset_subtype":cf_asset_subtype,
                "cf_credit_rating":cf_credit_rating,
                 'cf_monthly_budget':data.get("monthly_budget")
        }
            },
        }
    response = requests.post('https://crm.financethat.ca/crm/sales/api/deals', headers=headers, json=json_data)
    deal_data =response.json()
    return JsonResponse(deal_data,status=status.HTTP_200_OK)


@api_view(['POST'])
def create_manual_application_contact(request):
    data = request.data
    email = data.get('emails')
    lifecycle_stage_id=113000001358
    contact_status_id="112000000356"
    json_data = {
        "first_name": data.get('first_name'),
        "last_name": data.get('last_name'),
        "address": data.get('address'),
        "city": data.get("city"),
        "country":data.get("country","Canada"),
        "state": data.get('province'),
        "zipcode": data.get('postal_code'),
       "mobile_number": data.get('mobile_number'),
        "emails":email,
        "lifecycle_stage_id":lifecycle_stage_id ,
        "contact_status_id": contact_status_id,
        "is_active": True,
        "custom_field": {
            # "cf_signed_up_with_finance_that": "Yes",
            "cf_occupation": data.get('cf_occupation'),
            "cf_date_of_birth": data.get('cf_date_of_birth'),
            "cf_employment_status": data.get('cf_employment_status'),
            "cf_employer_name" : data.get('cf_employer_name'),
            "cf_monthly_gross_income":data.get("cf_monthly_gross_income"),
            "cf_contact_type": "Dealer Applicant", 
            "cf_credit_rating": data.get('cf_credit_rating'),
        },
    }
    headers = {
    'Authorization': 'Token token=oJjfiyJt_N1x4_baiv9MMQ',
    }

    owner_data = requests.post('https://crm.financethat.ca/crm/sales/api/contacts', headers=headers, json=json_data)
    owner_data =owner_data.json()
    return JsonResponse({"owner_data": owner_data,"status_code":status.HTTP_200_OK})


@api_view(['POST'])
def  create_manual_application_deals(request):
    data = request.data
    contacts_added_list = data.get("contacts_added_list")
    cf_asset_type_migrated = data.get("cf_asset_type_migrated")
    cf_asset_subtype = data.get("cf_asset_subtype")
    cf_credit_rating = data.get("cf_credit_rating")
    headers = {
    'Authorization': 'Token token=oJjfiyJt_N1x4_baiv9MMQ',
    }
    owner_data = requests.get(f'https://crm.financethat.ca/crm/sales/api/contacts/{contacts_added_list}', headers=headers)
    owner_data = owner_data.json()
    
    
    json_data = {
        'deal': {      
            "display_name": owner_data["contact"].get("first_name") +' '+ owner_data["contact"].get("last_name"),
            "name":owner_data["contact"].get("first_name") +' '+ owner_data["contact"].get("last_name"),
            "amount":data.get("monthly_budget"),
            "contacts_added_list":contacts_added_list,
            "cf_asset_type_migrated":cf_asset_type_migrated,
             "custom_field": {
                "cf_asset_type_migrated":cf_asset_type_migrated,
                "cf_asset_subtype":cf_asset_subtype,
                "cf_credit_rating":cf_credit_rating,
                 'cf_monthly_budget':data.get("monthly_budget")
        }
            },
        }
    response = requests.post('https://crm.financethat.ca/crm/sales/api/deals', headers=headers, json=json_data)
    deal_data =response.json()
    return JsonResponse(deal_data,status=status.HTTP_200_OK)