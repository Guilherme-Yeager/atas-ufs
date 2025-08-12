# Organização do projeto

```shell
  Codigo/
  .
  ├── models/ # Modelos de dados (ORM)
  ├── routes/ # Definição das rotas da aplicação
  ├── services/ # Lógica de negócio e serviços
  ├── static/ # Arquivos estáticos (CSS, JS, imagens...)
      ├── css/
      ├── js/
  ├── app.py # Aplicação Flask
  ├── .gitignore # Arquivos e pastas ignorados pelo Git
  ├── README.md # Documentação do projeto
  └── requirements.txt # Dependências Python do projeto
```


# Executar a aplicação

### Pré-requisitos

- Python 3.8+


### 1. Clonar o Repositório

```powershell
git clone https://seu-repositorio.git
cd nome-da-pasta-do-projeto
```

### 2. Criar o Ambiente Virtual

Windows:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Linux / macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar as Dependências

```
pip install -r requirements.txt
```

### 4. Executar

```
python app.py
```