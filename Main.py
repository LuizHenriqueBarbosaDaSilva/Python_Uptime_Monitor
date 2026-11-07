import requests
import datetime

# 1. A lista de sistemas que queremos monitorar
sites = [
    "https://google.com", 
    "https://github.com",
    "https://linkedin.com"
]

# 2. Vamos verificar cada site da lista
for site in sites:
    try:
        # Tenta aceder ao site (espera no máximo 5 segundos)
        resposta = requests.get(site, timeout=5)
        
        # Se o código da resposta for 200, significa que está tudo OK
        if resposta.status_code == 200:
            status = "ONLINE"
        else:
            status = f"ERRO (Código {resposta.status_code})"
            
    except requests.exceptions.RequestException:
        # Se a internet cair ou o site não existir, cai aqui
        status = "OFFLINE"

    # 3. Pega a data e hora exata de agora
    agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 4. Monta a frase final e guarda num ficheiro de texto
    resultado = f"[{agora}] O site {site} está {status}\n"
    
    with open("log_monitoramento.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(resultado)
        
    print(resultado.strip()) # Mostra também no terminal