# Exercícios de Testes Web e REST - Solução Completa

## Índice
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação](#instalação)
- [Execução dos Testes](#execução-dos-testes)
- [Descrição dos Exercícios](#descrição-dos-exercícios)
- [Relatórios](#relatórios)

## Estrutura do Projeto

```
exercicios-teste-software/
├── README.md
├── requirements.txt
├── pytest.ini
├── conftest.py                    # Fixtures globais
├── exercicio01/
│   └── tests/
│       └── test_login.py          # Testes de login web
├── exercicio02/
│   └── tests/
│       └── test_products_api.py   # Testes API de produtos
├── exercicio03/
│   └── tests/
│       └── test_todos_crud.py     # Testes CRUD completo
├── exercicio04/
│   ├── pages/
│   │   ├── __init__.py
│   │   ├── base_page.py           # Classe base POM
│   │   ├── login_page.py          # Page Object Login
│   │   └── dashboard_page.py      # Page Object Dashboard
│   └── tests/
│       └── test_login_pom.py      # Testes com POM
└── exercicio05/
    └── tests/
        ├── test_validacoes_parametrizadas.py  # Testes REST parametrizados
        └── test_busca_parametrizada.py        # Testes Web parametrizados
```

## 🚀 Instalação

### 1. Clone o repositório
```bash
git clone <url-do-repositorio>
cd exercicios-teste-software
```

### 2. Crie um ambiente virtual (recomendado)
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Verifique a instalação do ChromeDriver
O webdriver-manager instalará automaticamente o ChromeDriver necessário na primeira execução.

## ▶️ Execução dos Testes

### Executar todos os testes
```bash
pytest
```

### Executar testes de um exercício específico
```bash
pytest exercicio01/
pytest exercicio02/
pytest exercicio03/
pytest exercicio04/
pytest exercicio05/
```

### Executar testes por marcador
```bash
# Apenas testes web
pytest -m web

# Apenas testes de API
pytest -m api

# Testes de smoke
pytest -m smoke
```

### Executar teste específico
```bash
pytest exercicio01/tests/test_login.py::test_login_sucesso
```

### Executar com verbose e mostrar print
```bash
pytest -v -s
```

### Gerar relatório HTML
```bash
pytest --html=report.html --self-contained-html
```

### Visualizar relatório em tempo real
```bash
pytest -v --tb=short
```

### Gerar relatório JUnit XML
```bash
pytest --junitxml=report.xml
```

## Configurações

### pytest.ini
Configurações globais do pytest:
- Diretórios de testes
- Padrões de nomenclatura
- Opções padrão
- Marcadores personalizados

### conftest.py
Fixtures compartilhadas:
- `chrome_driver`: WebDriver do Chrome configurado

## Troubleshooting

### ChromeDriver não encontrado
```bash
pip install --upgrade webdriver-manager
```

### Timeout em testes web
Aumente o tempo de espera implícita no `conftest.py`:
```python
driver.implicitly_wait(20)  # Aumentar de 10 para 20 segundos
```

### Erro de conexão com API
Verifique sua conexão com a internet e se as APIs estão acessíveis:
- https://fakestoreapi.com/
- https://jsonplaceholder.typicode.com/
- https://reqres.in/

## Recursos Utilizados

- **Selenium WebDriver**: Automação de navegadores
- **Pytest**: Framework de testes
- **Requests**: Cliente HTTP para testes de API
- **WebDriver Manager**: Gerenciamento automático do ChromeDriver
- **Pytest-HTML**: Geração de relatórios HTML
