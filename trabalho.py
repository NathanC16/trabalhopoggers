import tkinter as tk
import re

# Criando a janela principal
janela = tk.Tk()
janela.title("Cartão de Vacina Virtual")

# Variáveis para armazenar os dados
dados_pacientes = {}
dados_vacinas = {}

# Funções para gerenciar os dados

def adicionar_paciente():
    """Adiciona um novo paciente ao sistema com validação de dados aprimorada."""
    # Coletar dados do paciente
    while True:
        nome = input("Nome completo: ")
        if not re.match(r"^[a-zA-ZáàâÃãóòôõÓÒÔÕêéêÊÉÈíìíÌÌÍúùúÚÙÙçÇñÑ\s]+$", nome):
            print("Nome inválido! Insira apenas letras e caracteres especiais.")
            continue
        break

    while True:
        data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
        try:
            dia, mes, ano = map(int, data_nascimento.split("/"))
            if 1 <= dia <= 31 and 1 <= mes <= 12 and ano >= 1900:
                break  # Data válida
            else:
                print("Data de nascimento inválida. Siga o formato DD/MM/AAAA.")
        except ValueError:
            print("Data de nascimento inválida. Use apenas números.")
            continue

    while True:
        cpf = input("CPF: ")
        if not re.match(r"^\d{11}$", cpf):
            print("CPF inválido! Insira apenas 11 números.")
            continue
        break

    while True:
        sexo = input("Sexo (M/F/Outro): ").upper()
        if sexo not in ("M", "F", "O"):
            print("Sexo inválido! Insira 'M' para masculino ou 'F' para feminino, ou 'O' para outro.")
            continue
        break

    endereco = input("Endereço: ")

    # Validar dados e salvar no dicionário
    dados_pacientes[cpf] = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "sexo": sexo,
        "endereco": endereco,
        "vacinas": {}  # Dicionário para armazenar as vacinas do paciente
    }

    print("Paciente adicionado com sucesso!")

def adicionar_vacina():
    """Adiciona uma nova vacina para um paciente."""
    # Selecionar paciente
    cpf = input("CPF do paciente: ")
    if cpf not in dados_pacientes:
        print("Erro: Paciente não encontrado!")
        return

    # Coletar dados da vacina
    nome_vacina = input("Nome da vacina: ")
    while True:
        data_aplicacao = input("Data de aplicação (DD/MM/AAAA): ")
        try:
            dia, mes, ano = map(int, data_aplicacao.split("/"))
            if 1 <= dia <= 31 and 1 <= mes <= 12 and ano >= 1900:
                break  # Data válida
            else:
                print("Data de aplicação inválida. Siga o formato DD/MM/AAAA.")
        except ValueError:
            print("Data de aplicação inválida. Use apenas números.")
            continue
        dose = None

    while True:
        try:
            dose = int(input("Dose (1, 2, etc.): "))
            break  # Sai do loop se a conversão for bem sucedida
        except ValueError:
            print("Erro: Digite um número inteiro.")
            continue
        
    while True:
        data_proxima_dose = input("Data da próxima dose (DD/MM/AAAA): ")
        try:
            dia, mes, ano = map(int, data_proxima_dose.split("/"))
            if 1 <= dia <= 31 and 1 <= mes <= 12 and ano >= 1900:
                break  # Data válida
            else:
                print("Data da próxima dose inválida. Siga o formato DD/MM/AAAA.")
        except ValueError:
            print("Data da próxima dose inválida. Use apenas números.")
            continue
        
    observacao = input("Observações (opcional): ")

    # Validar dados e salvar no dicionário
    if not all([nome_vacina, data_aplicacao, dose]):
        print("Erro: Preencha os campos obrigatórios!")
        return

    dados_pacientes[cpf]["vacinas"][nome_vacina] = {
        "data_aplicacao": data_aplicacao,
        "dose": dose,
        "data_proxima_dose": data_proxima_dose or "",
        "observacao": observacao or ""
    }

    print("Vacina adicionada com sucesso!")

def consultar_historico():
    """Consulta o histórico vacinal de um paciente."""
    cpf = input("CPF do paciente: ")
    if cpf not in dados_pacientes:
        print("Erro: Paciente não encontrado!")
        return

    paciente = dados_pacientes[cpf]
    if not paciente["vacinas"]:
        print("Este paciente não possui vacinas cadastradas.")
        return

    print(f"\nHistórico vacinal de {paciente['nome']}:")
    for nome_vacina, dados_vacina in paciente["vacinas"].items():
        print(f"\n- {nome_vacina}:")
        print(f"  Data de aplicação: {dados_vacina['data_aplicacao']}")
        print(f"  Dose: {dados_vacina['dose']}")
        if dados_vacina["data_proxima_dose"]:
            print(f"  Data da próxima dose: {dados_vacina['data_proxima_dose']}")
        if dados_vacina["observacao"]:
            print(f"  Observações: {dados_vacina['observacao']}")

def editar_dados():
    """Edita os dados de um paciente."""
    cpf = input("CPF do paciente: ")
    if cpf not in dados_pacientes:
        print("Erro: Paciente não encontrado!")
        return

    paciente = dados_pacientes[cpf]

    # Permitir a edição de nome, data de nascimento, sexo e endereço
    novo_nome = input(f"Novo nome ({paciente['nome']}): ") or paciente["nome"]
    nova_data_nascimento = input(f"Nova data de nascimento ({paciente['data_nascimento']}): ") or paciente["data_nascimento"]
    novo_sexo = input(f"Novo sexo ({paciente['sexo']}): ").upper() or paciente["sexo"]
    novo_endereco = input(f"Novo endereço ({paciente['endereco']}): ") or paciente["endereco"]

    # Atualizar os dados do paciente
    paciente["nome"] = novo_nome
    paciente["data_nascimento"] = nova_data_nascimento
    paciente["sexo"] = novo_sexo
    paciente["endereco"] = novo_endereco

    print("Dados do paciente atualizados com sucesso!")

def remover_dados():
    """Remove um paciente do sistema."""
    cpf = input("CPF do paciente: ")
    if cpf not in dados_pacientes:
        print("Erro: Paciente não encontrado!")
        return

    confirmacao = input("Tem certeza que deseja remover o paciente (S/N)? ").upper()
    if confirmacao != "S":
        print("Remoção cancelada.")
        return

    del dados_pacientes[cpf]
    print("Paciente removido com sucesso!")

def sair():
    """Sai do programa."""
    print("Saindo do programa...")
    janela.quit()  # Encerrar a janela gráfica (caso esteja implementada)

# Criar a janela principal
janela = tk.Tk()
janela.title("Sistema de Vacinação")
janela.geometry("800x600")

# Definir as cores de fundo e do texto
cor_fundo = "white"
cor_texto = "black"

# Criar a área principal da interface
area_principal = tk.Frame(janela, bg=cor_fundo)
area_principal.pack(expand=True, fill="both")

# Funções para chamar as funções existentes
def chamar_adicionar_paciente():
    adicionar_paciente()  # Chamar a função existente

def chamar_adicionar_vacina():
    adicionar_vacina()  # Chamar a função existente

def chamar_consultar_historico():
    consultar_historico()  # Chamar a função existente

def chamar_editar_dados():
    editar_dados()  # Chamar a função existente

def chamar_remover_dados():
    remover_dados()  # Chamar a função existente

def chamar_sair():
    sair()  # Chamar a função existente
    

# Criar botões para cada função
botao_adicionar_paciente = tk.Button(area_principal, text="Adicionar Paciente", command=chamar_adicionar_paciente, bg=cor_texto, fg=cor_fundo, cursor="hand2")
botao_adicionar_paciente.pack(pady=10, padx=20)

botao_adicionar_vacina = tk.Button(area_principal, text="Adicionar Vacina", command=chamar_adicionar_vacina, bg=cor_texto, fg=cor_fundo, cursor="hand2")
botao_adicionar_vacina.pack(pady=10, padx=20)

botao_adicionar_paciente = tk.Button(area_principal, text="Consultar histórico", command=chamar_consultar_historico, bg=cor_texto, fg=cor_fundo, cursor="hand2")
botao_adicionar_paciente.pack(pady=10, padx=20)

botao_adicionar_vacina = tk.Button(area_principal, text="Editar Dados", command=chamar_editar_dados, bg=cor_texto, fg=cor_fundo, cursor="hand2")
botao_adicionar_vacina.pack(pady=10, padx=20)

botao_adicionar_vacina = tk.Button(area_principal, text="Remover Dados", command=chamar_remover_dados, bg=cor_texto, fg=cor_fundo, cursor="hand2")
botao_adicionar_vacina.pack(pady=10, padx=20)

# Botão Sair
botao_sair = tk.Button(area_principal, text="Sair", command=janela.destroy, bg=cor_texto, fg=cor_fundo, cursor="hand2")
botao_sair.pack(pady=10, padx=20)

# Executar o programa
janela.mainloop()
