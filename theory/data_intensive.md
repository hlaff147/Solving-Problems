# Designing Data-Intensive Applications - Anotações de Estudo

<!--toc:start-->
- [Designing Data-Intensive Applications - Anotações de Estudo](#designing-data-intensive-applications---anotações-de-estudo)
  - [1. Armazenamento e Processamento Analítico](#1-armazenamento-e-processamento-analítico)
    - [OLTP vs. OLAP](#oltp-vs-olap)
    - [Data Warehouse](#data-warehouse)
    - [Data Lake vs. Data Warehouse (Esclarecimento de Dúvida)](#data-lake-vs-data-warehouse-esclarecimento-de-dúvida)
    - [HTAP (Hybrid Transactional/Analytical Processing)](#htap-hybrid-transactionalanalytical-processing)
  - [2. Fluxo e Integração de Dados](#2-fluxo-e-integração-de-dados)
    - [Sistemas de Registro (System of Record)](#sistemas-de-registro-system-of-record)
    - [Sistemas de Dados Derivados (Derived Data Systems)](#sistemas-de-dados-derivados-derived-data-systems)
    - [Diferença na Prática](#diferença-na-prática)
<!--toc:end-->

## 1. Armazenamento e Processamento Analítico

### OLTP vs. OLAP

* **Sistemas Transacionais (OLTP - Online Transaction Processing):** Sistemas operacionais que acessam e alteram o banco de dados para realizar suas transações de dados de forma rápida.
  * *Exemplo:* Ao montar um carrinho na Amazon, o usuário utiliza o sistema, ativa gatilhos e, com isso, aquela operação é inserida no banco de dados.
  * *Padrão de acesso:* Consultas fixas e predefinidas através de programas/softwares (invisíveis para o usuário final).
* **Sistemas Analíticos (OLAP - Online Analytical Processing):** Sistemas que têm o intuito de analisar grandes volumes de dados históricos para gerar valor empresarial (seja criando um dashboard ou um modelo de recomendação de produtos corretos para cada pessoa). 
  * *Padrão de acesso:* Consultas flexíveis, ad-hoc, visíveis para analistas e usuários que precisam gerar relatórios de negócios.
  * **Regra geral:** Este fluxo OLAP deve ficar apartado do fluxo OLTP explicado anteriormente para evitar gargalos de performance.

---

### Data Warehouse

Um banco de dados exclusivo para OLAP. Como os sistemas OLAP realizam consultas flexíveis e, muitas vezes, extremamente pesadas para gerar insights, separar o local onde são executadas evita prejudicar a operação dos clientes. Essa solução ficou muito popular a partir de 1980 e hoje é considerada essencial.

O processo de extrair dados de bancos OLTP, transformá-los e carregá-los no Data Warehouse (o famoso processo de **ETL - Extract, Transform, Load**) é feito utilizando ferramentas e frameworks especializados em conectores de dados e pipelines. 

> **[Adicionado pela IA]**
> **Exemplos de frameworks populares de ETL/Orquestração:**
> * **Apache Airflow:** O orquestrador mais utilizado para gerenciar e agendar pipelines de ETL complexos definidos como código (Python).
> * **Apache Spark:** Framework de processamento distribuído ideal para grandes volumes de dados (Batch e Streaming).
> * **dbt (data build tool):** Focado na etapa de *transformação* dentro do Data Warehouse usando SQL.
> * **Apache NiFi:** Excelente para ingestão e conectividade visual de dados em tempo real.
> * **AWS Glue / Google Cloud Dataflow:** Soluções gerenciadas (serverless) nas respectivas nuvens públicas para ETL.

---

### Data Lake vs. Data Warehouse (Esclarecimento de Dúvida)

> **[Esclarecimento de Dúvida / Expandido pela IA]**
> **Qual é mais refinado?**
> * O **Data Warehouse** é o repositório **mais refinado**. Nele, os dados já passaram por limpeza, filtragem, modelagem e normalização (esquema na escrita ou *schema-on-write*), prontos para analistas e relatórios corporativos.
> * O **Data Lake** armazena **dados brutos** (raw). Ele funciona como um repositório central mais econômico (geralmente usando Object Storages como AWS S3 ou Azure Blob Storage), onde os dados são despejados no seu formato original sem estrutura rígida predefinida (esquema na leitura ou *schema-on-read*).
> 
> **Resumo do Fluxo:**
> Os cientistas de dados preferem o **Data Lake** justamente por ele conter os dados brutos e não refinados, evitando que informações valiosas sejam descartadas no processo de limpeza. O Data Lake serve como um estágio intermediário entre os sistemas de produção (OLTP) e a estruturação final no Data Warehouse (OLAP).

---

### HTAP (Hybrid Transactional/Analytical Processing)

Alguns sistemas de banco de dados oferecem um modelo híbrido capaz de servir tanto a cargas OLTP quanto OLAP, conhecidos como **HTAP**. 

* **Nos sistemas OLTP:** É correto e recomendado que cada microsserviço possua seu banco de dados segregado para evitar acoplamento.
* **No cenário OLAP:** É muito melhor consolidar tudo em um único Data Warehouse para cruzar informações de múltiplos bancos OLTP com maior facilidade e performance.

---

## 2. Fluxo e Integração de Dados

### Sistemas de Registro (System of Record)

> **[Expandido pela IA]**
> Também conhecido como **Fonte da Verdade (Source of Truth)**. Este sistema guarda a versão primária e autoritativa do dado. 
> * Quando novas informações são criadas (por exemplo, um novo usuário se cadastra), elas são gravadas diretamente no Sistema de Registro primeiro.
> * Cada dado relevante possui apenas uma origem oficial neste sistema. Se houver qualquer divergência entre ele e outros sistemas, o valor presente no Sistema de Registro é o correto.

### Sistemas de Dados Derivados (Derived Data Systems)

> **[Expandido pela IA]**
> Sistemas que não são a fonte original da informação, mas sim o resultado de processar, transformar ou indexar dados existentes vindos de outro sistema de registro.
> * *Exemplos práticos:* Índices de busca (como o Elasticsearch), caches (como o Redis) e views materializadas.
> * Se um sistema de dados derivados for perdido ou corrompido, ele pode ser totalmente reconstruído a partir da fonte da verdade (o Sistema de Registro).

### Diferença na Prática

> **[Expandido pela IA]**
> A diferença entre um sistema de registro e um sistema de dados derivados **não depende da ferramenta ou do banco de dados escolhido**, mas sim de **como você projeta o fluxo de dados na sua arquitetura**.
> * *Por exemplo:* Você pode usar o PostgreSQL como Sistema de Registro (onde os novos pedidos de uma loja são persistidos) e, simultaneamente, usar outra instância de PostgreSQL (ou o mesmo banco, através de réplicas de leitura e views materializadas) para atuar como um sistema de dados derivados para relatórios.
