import requests
from datetime import datetime

maquina_ip = "192.168.15.155" # IP estatico definido anteriormente
# colocar de acordo com o IP do seu servidor
ultima_linha = ""
with open("/var/log/monitoramento.log", 'r') as log:
        for linha in log:
                ultima_linha = linha

try:
        requests.get(f"http://{maquina_ip}/")
        if "ONLINE" not in ultima_linha:
                with open("/var/log/monitoramento.log", "a+") as log:
                        log.write(f"Servidor status: ONLINE - {datetime.now()}\n")
except:
        if "OFFLINE" not in ultima_linha:
                requests.get("https://api.telegram.org/bot[SEU TOKEN DE ACESSO DO BOT AQUI]/sendMessage?chat_id=[SEU ID DO CHAT DO TELEGRAM]&text=Seu servidor web NGINX saiu do ar!!!")
                with open("/var/log/monitoramento.log", "a+") as log:
                        log.write(f"Servidor status: OFFLINE - {datetime.now()}\n")
