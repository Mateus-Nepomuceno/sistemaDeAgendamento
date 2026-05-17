# 📅 Sistema de Agendamento

Aplicação web desenvolvida para o **Núcleo de Apoio à Gestão de Pessoas do IFBaiano**, com o objetivo de gerenciar o quadro de funcionários (Docentes e Técnicos Administrativos), acompanhar estágios probatórios, contratos e fornecer um sistema de notificações inteligentes sobre prazos e progressões.

## Prévia

![Prévia do Sistema de Agendamento](docs/previa.png)

## Tecnologias Utilizadas

* **Framework:** Django 6.0+
* **Linguagem:** Python 3.12+
* **Banco de Dados:** SQLite / PostgreSQL
* **Segurança:** Django Authentication System
* **Frontend:** Bootstrap 5 & JavaScript

## Funcionalidades

O sistema exige autenticação e oferece os seguintes módulos:

#### Dashboard Central (`/`)
* **Visão Unificada:** Exibição consolidada de todas as demandas (progressões, probatórios, contratos e anotações) com vencimento próximo.
* **Calendário Inteligente:** Calendário interativo que destaca os dias com prazos críticos no mês vigente.

#### Gestão de Servidores (`/cadastros/`)
* **Técnicos e Docentes:** Cadastro completo com controle de matrícula, cargo, nível e processo.
* **Progressão Automática:** O sistema calcula automaticamente a data da próxima progressão com base no último ano avaliado.
* **Importação CSV:** Possibilidade de importar servidores em lote via arquivos CSV.

#### Gestão de Prazos (`/prazos/`)
* **Estágio Probatório:** Acompanhamento detalhado das 3 avaliações obrigatórias.
* **Contratos Temporários:** Gestão de Professores Substitutos e Estágios com controle de vigência.
* **Cálculo de Encerramento:** Definição automática de datas de término baseadas na data de início.
* **Importação CSV:** Suporte para carga inicial de probatórios e contratos.

#### Bloco de Anotações (`/anotacoes/`)
* **Notas Privadas:** Sistema de anotações exclusivas por usuário.
* **Prazos em Notas:** Possibilidade de definir alertas para tarefas específicas.

####  Sistema de Notificações
* **Alertas Inteligentes:** Notificações automáticas para prazos que vencem em 30, 15, 7 ou 0 dias.
* **Status Dinâmico:** Atualização automática do status para "Pendente" caso o prazo expire.
* **Central de Notificações:** Acesso rápido a todos os alertas pendentes no sistema.

## Automação e Comandos

Para manter o sistema atualizado, existe um comando personalizado para verificar prazos e gerar notificações:

```bash
python manage.py verificar_prazos
```