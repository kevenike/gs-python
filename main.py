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