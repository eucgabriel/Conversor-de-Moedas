import requests
import pandas as pd
from datetime import datetime
import time


def price_do():
    while True:
        requisition = requests.get(
            "https://economia.awesomeapi.com.br/last/USD-BRL")
        requisition_dic = requisition.json()
        price_dolar = requisition_dic["USDBRL"]["bid"]

        tabela = pd.read_excel("Cotações.xlsx")
        tabela.loc[0, "Cotação"] = float(price_dolar)

        tabela.loc[0, "Data da Última Atualização"] = datetime.now()

        tabela.to_excel("Cotações.xlsx", index=False)
        print(f"Cotação Atualizada. {datetime.now()}")

        time.sleep(60)
