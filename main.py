from colorama import init, Fore, Style

# Inicializar o colorama
init(autoreset=True)

# Função para exibir o menu principal
def exibir_menu_principal():
    print(Fore.BLUE + Style.BRIGHT + "Sistema Hospitalar - Menu Principal:")
    print("1. Cadastrar Paciente")
    print("2. Agendar Consulta")
    print("3. Visualizar Lista de Pacientes")
    print("4. Sair" + Style.RESET_ALL)

# Função para cadastrar um paciente
def cadastrar_paciente():
    print("\nCadastro de Paciente:")
    nome = input("Digite o nome do paciente: ")
    idade = validar_numero("Digite a idade do paciente: ")
    documento = validar_documento("Digite o número do documento do paciente: ")
    paciente = {"Nome": nome, "Idade": idade, "Documento": documento}
    lista_pacientes.append(paciente)
    print("Paciente cadastrado com sucesso!")

# Função para agendar uma consulta
def agendar_consulta():
    print("\nAgendamento de Consulta:")
    nome_paciente = input("Digite o nome do paciente: ")

    # Verificar se o paciente está na lista
    paciente_encontrado = False
    for paciente in lista_pacientes:
        if paciente['Nome'] == nome_paciente:
            paciente_encontrado = True
            break

    if paciente_encontrado:
        data_consulta = input("Digite a data da consulta (formato DD/MM/YYYY): ")
        horario_consulta = input("Digite o horário da consulta (formato HH:MM): ")
        consulta = {"Nome Paciente": nome_paciente, "Data Consulta": data_consulta,
                    "Horario Consulta": horario_consulta}
        lista_consultas.append(consulta)
        print("Consulta agendada com sucesso!")
    else:
        print("Paciente não encontrado. Por favor, verifique o nome.")

# Função para visualizar a lista de pacientes com a data e o horário da consulta
def visualizar_lista_pacientes():
    print("\nLista de Pacientes:\n")
    for paciente in lista_pacientes:
        print(f"Nome: {paciente['Nome']}, Idade: {paciente['Idade']}, Documento: {paciente['Documento']}")

        # Verificar se o paciente tem consultas agendadas
        consultas_paciente = [f"{consulta['Data Consulta']} às {consulta['Horario Consulta']}\n" for consulta in
                              lista_consultas if consulta['Nome Paciente'] == paciente['Nome']]
        if consultas_paciente:
            print(f" Consultas Agendadas: {', '.join(consultas_paciente)}")
        else:
            print("  Nenhuma consulta agendada.")

    print()       

# Função para validar entrada numérica
def validar_numero(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError:
            print("Por favor, digite um número válido.")

# Função para validar o número do documento
def validar_documento(mensagem):
    while True:
        documento = input(mensagem)
        if documento.isdigit() and len(
                documento) == 11:  # Validar se é composto apenas por dígitos e possui o tamanho esperado
            return documento
        else:
            print("Por favor, digite um número de documento válido com 11 dígitos.")

# Lista para armazenar pacientes e consultas
lista_pacientes = []
lista_consultas = []

# Loop principal do programa
while True:
    exibir_menu_principal()

    escolha = validar_numero(Fore.GREEN + "Digite a opção desejada: " + Style.RESET_ALL)

    if escolha == 1:
        cadastrar_paciente()
    elif escolha == 2:
        agendar_consulta()
    elif escolha == 3:
        visualizar_lista_pacientes()
    elif escolha == 4:
        print(Fore.RED + "Saindo do sistema. Até logo!" + Style.RESET_ALL)
        break
    else:
        print(Fore.YELLOW + "Opção inválida. Por favor, escolha uma opção válida." + Style.RESET_ALL)