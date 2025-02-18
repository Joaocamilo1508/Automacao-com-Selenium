# 📈 Automação de Cotação de Ações com Selenium
Este script utiliza a biblioteca **Selenium** para automatizar a busca de cotações de ações na página de **cotações da UOL**. Ele pesquisa os valores das ações de algumas empresas específicas, coleta as informações e as salva em um arquivo **Excel** para análise posterior.

## 🛠️ Tecnologias Utilizadas
- **Python** 🐍
- **Selenium** (para automação de navegação na web)
- **Pandas** (para manipulação e exportação dos dados)
- **WebDriver Manager** (para gerenciamento automático do driver do Chrome)

## 🔍 Funcionamento do Código
1. O script abre o site de cotações da **UOL** no navegador.
2. Para cada empresa listada, ele preenche a barra de pesquisa e busca o valor da ação.
3. Os valores encontrados são armazenados junto com a data e hora da consulta.
4. Os dados são organizados em um **DataFrame do Pandas** e exportados para um arquivo **Excel** (`empresas.xlsx`).

## ⚠️ Requisitos
- Ter o **Google Chrome** instalado.
- Instalar as dependências com:
  ```bash
  pip install selenium pandas openpyxl webdriver-manager
