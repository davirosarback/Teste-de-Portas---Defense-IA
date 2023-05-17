# SCRIPT DEFENSE
# IP Defense: 168.195.215.69

import socket


VERMELHO = "color 4"
VERDE = "color 2"
RESET = "color f"

ip = input('Digite o endereço de IP: ')
portas = [443, 80, 9000, 8005, 9005, 61616, 9200, 9100, 9320, 9090, 9500, 9550, 5060, 9600,
          30001, 9400, 5080, 554, 9900, 9901, 9115, 8081, 40000, 49999, 8080, 3306, 12366, 6379]

aberta = 0
fechada = 0


for porta in portas:
    # AF_INET (representa o tipo de endereço), SOCK_STREAM (indica que socket é do tipo TCP)
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(1)  # limite de tempo suportado
    conexao = cliente.connect_ex((ip, porta))

# condição (se conexão for igual a 0 porta aberta se não porta fechada)
# with open("teste.txt", 'a') as f:  # inserir caminho onde será salvo o arquivo
    # open("C:\\teste.txt", 'a') as f: # Windows
    if conexao == 0:
        print(str(porta) + " >> porta aberta")
        aberta = int(aberta) + 1
    else:
        print(str(porta) + " >> porta fechada")
        fechada = int(fechada) + 1

print('Para o IP: ' + ip)
print('Portas abertas: ' + str(aberta))
print('Portas fechadas: ' + str(fechada))

input('Pressione Enter para fechar')
input('Pressione Enter para fechar')
