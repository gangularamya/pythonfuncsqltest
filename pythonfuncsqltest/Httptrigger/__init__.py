import logging

import azure.functions as func
import pyodbc

server = 'tcp:pythonfuncsqltestdb.database.windows.net'
database = 'xxxxxx'
username = 'xxxxxx'
password = 'xxxxx'


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        driver = sorted(pyodbc.drivers()).pop()
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        return func.HttpResponse(f"Hello {name},  {driver}, {cnxn} ")
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )
