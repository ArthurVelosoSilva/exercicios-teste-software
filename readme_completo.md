# Exercícios de Testes Web e REST - Solução Completa

## 📋 Índice
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação](#instalação)
- [Execução dos Testes](#execução-dos-testes)
- [Descrição dos Exercícios](#descrição-dos-exercícios)
- [Relatórios](#relatórios)

## 🗂️ Estrutura do Projeto

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

## 📝 Descrição dos Exercícios

### Exercício 1: Teste de Login (Web)
**Arquivo:** `exercicio01/tests/test_login.py`

Testes automatizados do formulário de login usando Selenium WebDriver.

**Cenários cobertos:**
- ✅ Login com credenciais válidas
- ✅ Login com username inválido
- ✅ Login com senha incorreta
- ✅ Tentativa de login sem preencher campos
- ✅ Login com username vazio
- ✅ Verificação de mensagens de erro

**Como executar:**
```bash
pytest exercicio01/ -v
```

---

### Exercício 2: API de Produtos (REST)
**Arquivo:** `exercicio02/tests/test_products_api.py`

Testes da API FakeStore utilizando requests.

**Cenários cobertos:**
- ✅ Listar todos os produtos
- ✅ Buscar produto por ID
- ✅ Filtrar produtos por categoria
- ✅ Validar schema da resposta
- ✅ Testar limite de produtos retornados
- ✅ Testar ordenação
- ✅ Listar categorias disponíveis

**Como executar:**
```bash
pytest exercicio02/ -v
```

---

### Exercício 3: Teste CRUD Completo (REST)
**Arquivo:** `exercicio03/tests/test_todos_crud.py`

Implementação completa de testes CRUD usando JSONPlaceholder.

**Operações testadas:**
- ✅ CREATE - Criar novo todo
- ✅ READ - Buscar todo específico
- ✅ READ - Listar todos os todos
- ✅ READ - Filtrar por usuário
- ✅ UPDATE - Atualização completa (PUT)
- ✅ UPDATE - Atualização parcial (PATCH)
- ✅ DELETE - Deletar todo
- ✅ Fluxo CRUD completo
- ✅ Validação de schema

**Como executar:**
```bash
pytest exercicio03/ -v
```

---

### Exercício 4: Page Object Model (Web)
**Arquivos:** 
- `exercicio04/pages/base_page.py`
- `exercicio04/pages/login_page.py`
- `exercicio04/pages/dashboard_page.py`
- `exercicio04/tests/test_login_pom.py`

Refatoração dos testes do Exercício 1 usando o padrão Page Object Model.

**Estrutura POM:**
- **BasePage**: Métodos comuns (clicar, digitar, encontrar elementos)
- **LoginPage**: Page Object da página de login
- **DashboardPage**: Page Object da página pós-login

**Vantagens:**
- ✅ Código mais organizado e reutilizável
- ✅ Manutenção facilitada
- ✅ Separação clara entre testes e páginas
- ✅ Testes parametrizados com POM

**Como executar:**
```bash
pytest exercicio04/ -v
```

---

### Exercício 5: Testes Parametrizados
**Arquivos:**
- `exercicio05/tests/test_validacoes_parametrizadas.py`
- `exercicio05/tests/test_busca_parametrizada.py`

Testes parametrizados para validar múltiplos cenários.

**Parte A - Validação de Email (REST):**
- 10 cenários de emails inválidos
- Teste de registro com email válido

**Parte B - Validação de Senhas (REST):**
- 7 cenários de senhas inválidas
- Validação de formato e requisitos

**Parte C - Busca Parametrizada (Web):**
- Busca no Google com múltiplos termos
- Múltiplos cenários de login
- Testes de responsividade
- Validação de cores

**Como executar:**
```bash
pytest exercicio05/ -v
```

## 📊 Relatórios

### Gerar relatório HTML completo
```bash
pytest --html=report.html --self-contained-html
```

O relatório incluirá:
- ✅ Total de testes executados
- ✅ Testes aprovados/reprovados
- ✅ Tempo de execução
- ✅ Detalhes de cada teste
- ✅ Logs e stack traces de erros

### Visualizar relatório em tempo real
```bash
pytest -v --tb=short
```

### Gerar relatório JUnit XML
```bash
pytest --junitxml=report.xml
```

## 🔧 Configurações

### pytest.ini
Configurações globais do pytest:
- Diretórios de testes
- Padrões de nomenclatura
- Opções padrão
- Marcadores personalizados

### conftest.py
Fixtures compartilhadas:
- `chrome_driver`: WebDriver do Chrome configurado

## 🐛 Troubleshooting

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

## 📚 Recursos Utilizados

- **Selenium WebDriver**: Automação de navegadores
- **Pytest**: Framework de testes
- **Requests**: Cliente HTTP para testes de API
- **WebDriver Manager**: Gerenciamento automático do ChromeDriver
- **Pytest-HTML**: Geração de relatórios HTML

## ✅ Checklist de Entrega

- [x] Código de todos os 5 exercícios
- [x] Estrutura de pastas organizada
- [x] README com instruções
- [x] requirements.txt
- [x] pytest.ini configurado
- [x] Fixtures globais (conftest.py)
- [x] Testes passando com sucesso
- [x] Page Object Model implementado
- [x] Testes parametrizados
- [x] Comentários e docstrings

## 👨‍💻 Autor

Projeto desenvolvido para a disciplina de Teste de Software

## 📄 Licença

Este projeto é para fins educacionais.
