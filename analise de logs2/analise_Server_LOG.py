from collections import Counter

#Abrir e ler o arquivo
arquivo = 'D:/Python/Exercicios/LOG/analise de logs2/server.LOG.txt'

abrir_arquivo = open(arquivo)
status_alvo = '404'
leitura_linha_a_linha = abrir_arquivo.readlines()
abrir_arquivo.close()

#Contadores
contador_status_404 = 0
contador_IP = Counter()
contador_User_agent_404 = Counter()

#Análise de fato
for linha in leitura_linha_a_linha:
    try:
        partes = linha.split('"')
        info_inicial = partes[0].split()
        ip = info_inicial[0]

        requisicao = partes[1].split()
        status = partes[2].strip().split()[0]  # código de status
        user_agent = partes[5] if len(partes) >= 6 else 'Desconhecido'

        if status == status_alvo:
            contador_IP[ip] += 1
            contador_status_404 += 1
            contador_User_agent_404[user_agent] += 1

    except Exception as e:
        print(f' Erro ao processar linha: {linha.strip()}')


print(f'O total de erros foram:{contador_status_404}')
print(f'Os IPs que geraram erros:{contador_IP} ')
print(f'o User Agent mais comuns foram: {contador_User_agent_404}')
print(f'O ip que mais causou erro com a requisição 404 foi: {contador_IP.most_common(1)[0]}')

                    





 