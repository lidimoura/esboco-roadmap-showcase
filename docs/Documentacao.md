# PowerPolis - Análise e Otimização de Consumo Energético

## 👩‍💻 Sobre a Equipe / About the Team

**G9-BR-TEAM-12** | Hackathon No-Country - EnergiAI

| Membro | Papel | LinkedIn | GitHub |
| --- | --- | --- | --- |
| Lídi Moura | Data Analyst / Líder | [LinkedIn](https://www.linkedin.com/in/lidimoura/) | [GitHub](https://github.com/lidimoura) |
| Pedro Henrique Rodrigues da Costa Tireli | Data Scientist | [LinkedIn](https://www.linkedin.com/in/phtirelli/) | [GitHub](https://github.com/phtirelli) |
| Samanta Sá | Backend Developer / Scrum Master | [LinkedIn](https://www.linkedin.com/in/engsamantasa/) | [GitHub](https://github.com/engsamantasa) |
| Kauã da Silva Barros | Backend Developer | - | [GitHub](https://github.com/kaua3-c) |
| Alan Anderson | Backend Developer | [LinkedIn](https://www.linkedin.com/in/alan-anderson-dev/) | [GitHub](https://github.com/alanandersondev) |
| Mayara Medeiros Giangiacomo | Backend Developer | - | - |
| Alex Furukawa | Full Stack Developer | [LinkedIn](https://www.linkedin.com/in/lexkawa/) | [GitHub](https://github.com/dev-corvus/) |
| Antônio Carlos Martins Teixeira | Frontend Developer | [LinkedIn](https://www.linkedin.com/in/antonio-carlos-martins-teixeira) | [GitHub](https://github.com/digichargeac) |
| Dryelli Vitoria Martins de Freitas | Architect (Software / Solution Architect) | - | - |

---

## 📂 Entregas do Projeto / Project Deliverables

Para garantir a transparência técnica e a facilidade na tomada de decisão, este projeto foi estruturado em três frentes de entrega:

- 📊 [**Dashboard Interativo (Streamlit)**](https://github.com/No-Country-simulation/G9-BR-TEAM-12/tree/main/frontend/streamlit_app): Desenvolvido para stakeholders, diretores e usuários finais[...]
- 🛠️ [**Documentação Técnica e Notebooks (GitHub)**](https://github.com/No-Country-simulation/G9-BR-TEAM-12): Recomendado para Tech Leads, recrutadores e a própria equipe de desenvolvimen[...]
- 🌐 [**Site de Apresentação (EnergiAI Showcase)**](https://manus-webdev-energiai-showcase.manus.computer/): Uma landing page trilíngue que conta a história do projeto, apresenta a equipe e [...]

---

## [PT-BR] Visão geral do projeto

O **PowerPolis** é uma solução inovadora desenvolvida no Hackathon EnergiAI da No-Country, com o objetivo de transformar dados de consumo energético em inteligência acionável. Nossa platafor[...]

## [EN] Project Overview

**PowerPolis** is an innovative solution developed during the No-Country EnergiAI Hackathon, aiming to transform energy consumption data into actionable intelligence. Our platform...

---

## Stack Tecnológica

- **Python & Pandas**: Limpeza de dados, manipulação de DataFrames e cálculo de KPIs.
- **Scikit-Learn**: Implementação e comparação de modelos preditivos (Regressão Linear, Árvore de Decisão, Random Forest).
- **Streamlit**: Desenvolvimento de dashboards interativos e visualização dinâmica.
- **Google Colab / Kaggle Notebooks**: Ambiente de prototipagem, EDA e documentação técnica.
- **Java/Spring Boot**: Backend para a API de análise energética.
- **OCI Object Storage**: Armazenamento de modelos e dados.
- **Git & GitHub**: Controle de versão e colaboração da equipe.
- **Discord**: Comunicação e alinhamento da equipe.

## Critérios de Negócio e Classificação

Para a classificação de eficiência (Eficiente, Moderado, Ineficiente), utilizamos uma lógica baseada em quantis e regras de negócio que consideram as seguintes variáveis:

- `consumo_kwh`: Consumo total de energia elétrica em kWh por mês.
- `quantidade_equipamentos`: Número total de equipamentos elétricos no imóvel.
- `horas_alto_consumo`: Média de horas diárias com equipamentos de alto consumo ligados.
- `tipo_imovel`: Categoria do imóvel (Casa, Apartamento, Comercial, Indústria).
- `uso_horario_pico`: Indicação de consumo significativo durante o horário de pico (18h-21h).
- `possui_energia_solar`: (A ser integrada) Indica se o imóvel possui sistema de energia solar.

Os critérios exatos e a metodologia de rotulagem estão detalhados em `docs/criterios-classificacao.md` e `docs/METODOLOGIA.md` (a ser criado).

## Contrato entre Dados e API

O modelo preditivo será serializado (e.g., `.pkl` ou `.joblib`) e carregado pelo Backend em Java/Spring Boot. A integração se dará através de um endpoint `POST /analise-energetica` que recebe[...]

**Exemplo de JSON de Entrada:**
```json
{
  "consumo_kwh": 450.5,
  "quantidade_equipamentos": 12,
  "horas_alto_consumo": 6,
  "tipo_imovel": "Casa",
  "uso_horario_pico": true
}
```

**Exemplo de JSON de Saída:**
```json
{
  "categoria": "Moderado",
  "probabilidade": 0.78,
  "recomendacoes": [
    "Considere otimizar o uso de ar condicionado em horários de pico.",
    "Verifique a eficiência de equipamentos antigos."
  ],
  "custo_estimado_mensal": 337.88
}
```

## Integração OCI

1. **Treinamento do Modelo**: O notebook de Data Science treina o modelo e o serializa para um arquivo (e.g., `modelo_powerpolis.pkl`).
2. **Upload para OCI**: O arquivo do modelo é enviado para um bucket no OCI Object Storage.
3. **Download pelo Backend**: O serviço Spring Boot, ao iniciar, baixa o modelo do OCI Object Storage para carregá-lo em memória e realizar as predições.

---

**Transparência e Vibe Coding:** A análise de dados, lógica de programação e tomada de decisão estratégica apresentadas neste repositório são de autoria da equipe G9-BR-TEAM-12.
