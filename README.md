# 🛒 Análise de E-commerce Brasileiro (Olist) — Pipeline ETL com Python + Power BI

Projeto de Engenharia de Dados Jr para portfólio, utilizando um pipeline de dados completo (ETL) com Python e visualização no Power BI. O conjunto de dados é baseado em transações reais de um marketplace brasileiro (Olist).

---

## 🔄 Pipeline ETL

### 🔍 Extração
Leitura dos arquivos CSV originais disponibilizados pelo Olist.

### 🧪 Transformação
- Remoção de registros inconsistentes
- Cálculo de tempo de entrega
- Normalização de categorias
- Agregações por data, estado, categoria e cliente

### 📦 Carga
Exportação dos dados tratados para `.csv` e conexão com o Power BI.

---

## 📜 Regras de Negócio

- Considerar apenas pedidos entregues (`order_status = 'delivered'`)
- Excluir registros com dados essenciais ausentes
- Calcular tempo de entrega real por pedido
- Calcular ticket médio por cliente e por pedido
- Agrupar dados por estado, categoria e mês para visualização

---

## ✅ Critérios de Aceite

- [x] Dados extraídos com sucesso do Kaggle
- [x] Transformações aplicadas conforme regras de negócio
- [ ] Dados limpos salvos em `/data/processed/`
- [ ] Dashboards criados no Power BI com:
  - Faturamento mensal
  - Tempo médio de entrega por estado
  - Vendas por categoria de produto
  - Ticket médio por cliente
  - Top 10 produtos mais vendidos
- [ ] Repositório versionado com Git
- [ ] Documentação clara (este README)

---

## 📊 Insights Gerados (Exemplos)

- Estados do Sudeste concentram a maior parte do faturamento
- Produtos da categoria **"cama_mesa_banho"** têm maior tempo médio de entrega
- Cartão de crédito é a forma de pagamento mais comum
- Ticket médio aumenta no final do ano (sazonalidade)

---

## 📦 Fonte dos Dados

Dataset Olist (via Kaggle):  
🔗 [https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

---

## 👤 Autor

**Miguel Luis Resende**  
📧 miguelresende.emprego@gmail.com  
🔗 [linkedin.com/in/miguel-luis-resende](https://www.linkedin.com/in/miguel-luis-resende/)

---

## 📌 Licença

Este projeto é apenas para fins educacionais e de portfólio.  
Os dados são públicos, conforme termos do Kaggle/Olist.