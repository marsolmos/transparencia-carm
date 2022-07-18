import pandas as pd
import requests
import datetime

def get_contracts():
    '''
    Get all contracts avalialble up to now from CARM Official source

    :return: Saved data into folder as .csv file
    :rtype: .csv file saved in data folder
    '''
    # API Endpoint
    URL = "https://transparencia.carm.es/rest-services/services/restAPI/Contratos"
    
    # Sending get request and saving the response as response object
    r = requests.get(url=URL)

    # Extracting data in json format
    data = r.json()

    # Convert API answer into pandas DataFrame
    df = pd.DataFrame(data, columns=[
        "CODIGO INSCRIPCION",
        "TIPO DE CONTRATO",
        "PROCEDIMIENTO",
        "OBJETO",
        "IMPORTE LICITACION (IVA INCLUIDO)",
        "IMPORTE ADJUDICACION (IVA INCLUIDO)",
        "ADJUDICATARIO DESCRIPCION",
        "ADJUDICATARIO CODIGO",
        "FECHA FORMALIZACION",
        "DURACION",
        "ORGANO DE CONTRATACION",
        "COD-ORGANO-CONTRATACION",
        "CPV DESCRIPCION",
        "CPV CODIGO",
        "NUM_MODIFICACIONES",
        "UNKNOWN"
        ])
    df.drop("UNKNOWN", axis=1, inplace=True)

    # Save DataFrame into .csv with today's date
    today = datetime.datetime.now().strftime("%Y%m%d")
    file_path = f"../../data/raw_{today}.csv"
    df.to_csv(file_path, index=False, sep=";")
    print(f"File with all available contract saved in local path: {file_path}")

    return