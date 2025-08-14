# 🚀 Gerenciador de Arquivos via Terminal

> Um script Python simples para criar, ler, atualizar e deletar arquivos de texto diretamente da linha de comando.

![Status do Projeto](https://img.shields.io/badge/status-concluído-green)

## 📄 Sobre o Projeto

Este projeto foi desenvolvido como um exercício prático para aprofundar os conhecimentos em Python, com foco especial na manipulação de arquivos e na interação com o sistema operacional através do terminal. O objetivo era criar uma ferramenta de linha de comando (CLI) intuitiva para gerenciar notas e pequenos arquivos de texto sem a necessidade de uma interface gráfica.

Todos os arquivos criados e gerenciados por este script são armazenados de forma organizada em um diretório chamado `files/`, que é criado automaticamente na primeira execução.

---

## ✨ Funcionalidades

* **Escrever em Arquivos:** Crie um novo arquivo ou sobrescreva um existente com um novo conteúdo.
* **Leitura Interativa:** Liste todos os arquivos `.txt` disponíveis e escolha qual deles deseja ler.
* **Adicionar Conteúdo (Append):** Adicione novas informações ao final de um arquivo existente sem apagar o conteúdo anterior.
* **Deletar Arquivos:** Remova permanentemente um arquivo do sistema.
* **Limpar Conteúdo de Arquivos:** Apague todo o conteúdo de um arquivo, mas mantenha o arquivo vazio.
* **Interface Simples:** Um menu numerado guia o usuário através de todas as opções disponíveis.

---

## 🛠️ Tecnologias Utilizadas

* **[Python 3](https://www.python.org/)**
* Módulos Nativos do Python:
    * `os` - Para interações com o sistema operacional, como criar diretórios e listar arquivos.
    * `sys` - Para funcionalidades do sistema, como sair do programa.

Não há necessidade de instalar bibliotecas externas!

---

## ⚙️ Como Usar

Para executar este projeto localmente, siga os passos abaixo.

**Pré-requisitos:**
* Você precisa ter o [Python 3](https://www.python.org/downloads/) instalado.
* Você precisa ter o [Git](https://git-scm.com/downloads) instalado (opcional, para clonar).

**Passos:**

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/Mikaelnotfound/file-management-py.git
    ```

2.  **Navegue até o diretório do projeto:**
    ```bash
    cd file-management-py/
    ```

3.  **Execute o script:**
    ```bash
    python main.py 
    ```

4.  **Interaja com o menu:**
    O programa irá apresentar um menu no terminal. Basta digitar o número da opção desejada e pressionar Enter.
    ```
    --- Sistema de Gerenciamento de Arquivos ---
    1. Escrever em um arquivo (cria/sobrescreve)
    2. Ler o conteúdo de um arquivo
    3. Adicionar conteúdo a um arquivo
    4. Deletar um arquivo
    5. Apagar o conteúdo de um arquivo
    6. Sair
    Por favor, entre com sua escolha (1-6):
    ```

---

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

Desenvolvido por **Mikael Carlos** 👋

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Mikaelnotfound)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mikael-carlos-0950612bb/)