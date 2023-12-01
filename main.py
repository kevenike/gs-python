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