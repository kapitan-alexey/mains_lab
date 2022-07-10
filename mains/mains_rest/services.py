import pandas as pd


def import_xls_clients(xls_file):
    table_xls = pd.ExcelFile(xls_file)
    sheet1 = pd.read_excel(table_xls, 'client')
    sheet2 = pd.read_excel(table_xls, 'organization')

    clients_list = [client[0] for client in sheet1.values]
    organizations_list = [org for org in sheet2.values]
    return clients_list, organizations_list
