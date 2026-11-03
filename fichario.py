# Atividade de Recuperação: Monitor de Nível de Água
# Aluno: Guilherme Aparecido Samperi Rodrigues

# Definição dos códigos de cores ANSI
COR_RESET = "\033[0m"
COR_VERMELHO = "\033[31m"
COR_LARANJA = "\033[33m"  # O amarelo/laranja padrão ANSI
COR_AMARELO = "\033[93m"  # Amarelo brilhante
COR_AZUL = "\033[34m"
COR_VERDE = "\033[32m"

def monitorar_reservatorio(nivel):
    """
    Função que recebe o nível do reservatório e exibe 
    a situação correspondente com a cor configurada.
    """
    if nivel == 1:
        print(f"{COR_VERMELHO}Situação: Muito baixo (crítico){COR_RESET}")
    elif nivel == 2:
        print(f"{COR_LARANJA}Situação: Baixo{COR_RESET}")
    elif nivel == 3:
        print(f"{COR_AMARELO}Situação: Médio{COR_RESET}")
    elif nivel == 4:
        print(f"{COR_AZUL}Situação: Alto{COR_RESET}")
    elif nivel == 5:
        print(f"{COR_VERDE}Situação: Muito alto (cheio){COR_RESET}")
    else:
        print("Nível inválido! Digite um valor entre 1 e 5.")

# --- Programa Principal ---
if __name__ == "__main__":
    print("--- MONITOR DE RESERVATÓRIO ---")
    try:
        # Lê o nível digitado pelo usuário
        nivel_usuario = int(input("Digite o nível do reservatório (1 a 5): "))
        
        # Chama a função passando o parâmetro
        monitorar_reservatorio(nivel_usuario)
    except ValueError:
        print("Por favor, digite apenas números inteiros de 1 a 5.")
