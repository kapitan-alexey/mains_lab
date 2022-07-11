import pandas as pd

from random import random, choice


def process_client_org_xlsx(xls_file):
    table_xls = pd.ExcelFile(xls_file)
    sheet1 = pd.read_excel(table_xls, 'client')
    sheet2 = pd.read_excel(table_xls, 'organization')

    clients_list = [client[0] for client in sheet1.values]
    organizations_list = [org for org in sheet2.values]

    return clients_list, organizations_list


def process_bills_xlsx(xls_file):
    table_xls = pd.ExcelFile(xls_file)
    sheet1 = pd.read_excel(table_xls)

    return sheet1.values.tolist()


def fraud_detector(service: str) -> float:
    return random()


def service_classification(service: str) -> dict:
    service_dict = {1: 'консультация', 2: 'лечение', 3: 'стационар', 4: 'диагностика', 5: 'лаборатория'}
    result = choice(list(service_dict.items()))
    return {'service_class': result[0], 'service_name': result[1]}


def address_correction(address: str) -> str:
    address_forbidden = {'-'}
    address_prefix = 'Адрес: '
    result_address = address if address.isspace() or address in address_forbidden else address_prefix + address
    return result_address
