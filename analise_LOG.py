from collections import Counter
 
#Arquivo
arquivo_log = "D:/Python/Exercicios/LOG/analiseLogs/access.log.txt" # Coloque o caminho do arquivo de texto Apache aqui
abrir_arquivo = open(arquivo_log)
ip_alvo = "192.168.4.25"
 
contador_acesso_200 = 0
contador_de_acesso = 0
contador_de_url = Counter() #conta com que frenquencia essa URL aparece, função de biblioteca
 
#abrir o arquivo e ler linha por linha
abrir_arquivo = open(arquivo_log)
linhas = abrir_arquivo.readlines()
abrir_arquivo.close()
 
#analisar linha por linha
for linha in linhas:
    try:
        partes = linha.split()
        ip = partes[0]
        metodo = partes[5].strip('"')
        url = partes[6]
        status = partes[8]
       
        if len(partes) < 9:
            continue
       
        if ip.replace('"', '') == ip_alvo and status == "200":
            contador_acesso_200 += 1
 
        contador_de_url[url] += 1
    except IndexError:
        continue
 
#Resultados
 
print(f"O ip {ip_alvo} acessou com status 200: {contador_acesso_200} vezes")
print(f"O ip {ip_alvo} teve como caminho mais acessado o: {contador_de_url.most_common(1)[0]}")
 