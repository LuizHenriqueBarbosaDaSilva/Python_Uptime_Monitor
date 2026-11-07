import requests
import datetime

# Uma lista que ira conter os sites que queremos monitorar
sites = [
    "https://google.com", 
    "https://github.com",
    "https://linkedin.com"
]

# Faz a verificação de cada site da lista
for site in sites:
    try:
        # Tenta entrar em contato com o site, com um timeout de 5 segundos
        resposta = requests.get(site, timeout=5)
        
        # Se o código da resposta for 200, significa que está tudo OK
        if resposta.status_code == 200:
            status = "ONLINE"
        else:
            status = f"ERRO (Código {resposta.status_code})"
            
    except requests.exceptions.RequestException:
        # Se a internet cair ou o site não existir passa por aqui
        status = "OFFLINE"

    # Pega a data e hora atual para registrar no log
    agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    #   Cria uma string com o resultado do monitoramento
    resultado = f"[{agora}] O site {site} está {status}\n"
    
    with open("log_monitoramento.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(resultado)
        
    print(resultado.strip()) # Mostra também no terminal