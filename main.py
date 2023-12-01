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