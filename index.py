import os
import sys

DATA_DIR = "files"

def setup_directory():
    if not os.path.exists(DATA_DIR):
        os.mkdir(DATA_DIR)
        print(f"Diretório '{DATA_DIR}' criado.")

def get_full_path(filename):
    if not filename.endswith('.txt'):
        filename += '.txt'
    return os.path.join(DATA_DIR, filename)

def write_to_file(filename, content):
    full_path = get_full_path(filename)
    with open(full_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Conteúdo escrito em '{full_path}'")

def read_content_from_file():
    files = [f for f in os.listdir(DATA_DIR) if f.endswith('.txt')]
    
    if not files:
        print(f"Nenhum arquivo encontrado no diretório '{DATA_DIR}'.")
        return

    print("\nArquivos disponíveis para leitura:")
    for i, filename in enumerate(files):
        print(f"  {i + 1}. {filename}")

    try:
        choice = int(input(f"Por favor, escolha o número do arquivo (1-{len(files)}): "))
        if 1 <= choice <= len(files):
            selected_file = files[choice - 1]
            full_path = get_full_path(selected_file)
            
            with open(full_path, 'r', encoding='utf-8') as file:
                content = file.read()
                print(f"\n--- Conteúdo de '{selected_file}' ---")
                print(content)
                print("-------------------------------------\n")
        else:
            print("Escolha inválida. Por favor, tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

def append_to_file(filename, content):
    full_path = get_full_path(filename)
    if not os.path.exists(full_path):
        print(f"Erro: O arquivo '{filename}' não existe. Crie-o primeiro usando a opção 1.")
        return
        
    with open(full_path, 'a', encoding='utf-8') as file:
        file.write(content)
    print(f"Conteúdo adicionado a '{full_path}'")

def delete_file(filename):
    full_path = get_full_path(filename)
    if os.path.exists(full_path):
        os.remove(full_path)
        print(f"Arquivo '{full_path}' deletado com sucesso.")
    else:
        print(f"Erro: O arquivo '{full_path}' não existe.")

def delete_file_content(filename):
    full_path = get_full_path(filename)
    if not os.path.exists(full_path):
        print(f"Erro: O arquivo '{filename}' não existe.")
        return
    with open(full_path, 'w') as file:
        pass 
    print(f"Conteúdo do arquivo '{full_path}' foi apagado.")

setup_directory()

while True:
    print("\n--- Sistema de Gerenciamento de Arquivos ---")
    print("1. Escrever em um arquivo (cria/sobrescreve)")
    print("2. Ler o conteúdo de um arquivo")
    print("3. Adicionar conteúdo a um arquivo")
    print("4. Deletar um arquivo")
    print("5. Apagar o conteúdo de um arquivo")
    print("6. Sair")
    
    try:
        choice = int(input("Por favor, entre com sua escolha (1-6): "))
    except ValueError:
        print("Escolha inválida. Por favor, digite um número.")
        continue

    if choice == 1:
        filename = input("Digite o nome do arquivo: ")
        content = input("Digite o conteúdo a ser escrito:\n")
        write_to_file(filename, content)
    elif choice == 2:
        read_content_from_file()
    elif choice == 3:
        filename = input("Digite o nome do arquivo para adicionar conteúdo: ")
        content = input("Digite o conteúdo a ser adicionado:\n")
        append_to_file(filename, content)
    elif choice == 4:
        filename = input("Digite o nome do arquivo a ser deletado: ")
        delete_file(filename)
    elif choice == 5:
        filename = input("Digite o nome do arquivo para apagar o conteúdo: ")
        delete_file_content(filename)
    elif choice == 6:
        print("Saindo do sistema. Adeus!")
        sys.exit()
    else:
        print("Escolha inválida. Por favor, tente novamente.")