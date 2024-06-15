# Descrição: Programa para gerenciar reservas de um restaurante

# classe definida para representar uma reserva com os atributos nome, data e hora, e lista para armazenar as reservas.

class reserva:
    def __init__(self, nome, data, hora,):
        self.nome = nome
        self.data = data
        self.hora = hora

    def __str__(self):
        return f"Reserva para {self.nome} no dia {self.data} às {self.hora} horas."
    
reservas = []

# Funções para adicionar os dados necessários.

def adicionar_reserva():
    nome = input("Digite o nome completo do cliente: ").upper() # converter as letras para maiúsculas para facilitar a busca.
    data = input("Digite a data da reserva (dd/mm/aaaa): ")
    hora = input("Digite a hora da reserva (HH:MM): ")
    reserva_nova = reserva(nome, data, hora)  # instância da classe reserva.
    reservas.append(reserva_nova)  # instância adicionada à lista de reservas.
    print("Reserva realizada com sucesso!")

# Função para listar as reservas realizadas.

def listar_reservas():
    if reservas:
        print("Reservas realizadas:")
        for reserva in reservas:
            print(reserva)
    else:
        print("Não há reservas realizadas.")

# função para cancelar uma reserva.

def cancelar_reserva():
    nome = input("Digite o nome completo do cliente: ").upper() # converter as letras para maiúsculas para facilitar a busca.
    for reserva in reservas:
        if reserva.nome == nome:
            reservas.remove(reserva)
            print("Reserva cancelada com sucesso!")
            break
    else:
        print("Reserva não encontrada.")

# menu de opções para o usuário.

while True:
    print("=================Opções=================:")
    print("1 - Adicionar reserva")
    print("2 - Listar reservas")
    print("3 - Cancelar reserva")
    print("4 - Sair")
    print("==========================================")
    opcao = input("Digite a opção desejada: ")
    
# chamada das funções de acordo com a opção escolhida pelo usuário.

    if opcao == "1":
        adicionar_reserva()
    elif opcao == "2":
        listar_reservas()
    elif opcao == "3":
        cancelar_reserva()
    elif opcao == "4":
        break
    else:
        print("Opção inválida!")


    