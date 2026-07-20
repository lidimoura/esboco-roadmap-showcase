## PowerPolis - Dashboard Streamlit

Este é o dashboard interativo do projeto PowerPolis, desenvolvido em Streamlit. Ele serve como um MVP funcional para a análise energética, um roadmap visual da evolução do projeto e uma apresentação da equipe.

### Funcionalidades:
- **Home:** Visão geral do projeto, missão e status atual.
- **Análise Energética:** Formulário para entrada de dados de consumo e classificação de eficiência, com recomendações personalizadas.
- **Roadmap do Projeto:** Acompanhamento visual do cronograma de desenvolvimento do hackathon.
- **Nossa Equipe:** Apresentação dos membros da equipe com seus papéis e links para perfis.
- **Documentação:** Links essenciais para o repositório GitHub, contrato da API, critérios de classificação e outros documentos.
- **Internacionalização (i18n):** Suporte trilíngue (Português, Inglês, Espanhol) com seleção de idioma.

### Como Rodar Localmente:

1.  **Navegue até o diretório:**
    ```bash
    cd /home/ubuntu/powerpolis-repo/frontend/streamlit_app
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o aplicativo Streamlit:**
    ```bash
    streamlit run app.py
    ```

    O aplicativo será aberto no seu navegador padrão (geralmente `http://localhost:8501`).

### Como Fazer Deploy no Streamlit Cloud:

1.  **Certifique-se de que seu código está no GitHub:**
    Este diretório (`frontend/streamlit_app`) deve ser a raiz do seu aplicativo Streamlit no repositório GitHub do PowerPolis.

2.  **Vá para o Streamlit Cloud:**
    Acesse [share.streamlit.io](https://share.streamlit.io/) e faça login.

3.  **Conecte seu repositório:**
    Clique em "New app" e selecione o repositório `No-Country-simulation/G9-BR-TEAM-12`.

4.  **Configure o caminho do arquivo principal:**
    - **Main file path:** `frontend/streamlit_app/app.py`
    - **Python version:** Selecione a versão do Python que você usou (ex: 3.9, 3.10)

5.  **Deploy:**
    Clique em "Deploy!" e aguarde o Streamlit Cloud construir e implantar seu aplicativo.

### Estrutura de Arquivos:

```
frontend/streamlit_app/
├── .streamlit/
│   └── config.toml
├── app.py
├── pages/
│   ├── 1_Análise.py
│   ├── 2_Roadmap.py
│   ├── 3_Equipe.py
│   └── 4_Documentação.py
├── utils/
│   └── i18n.py
├── assets/
│   └── logo.png
└── requirements.txt
```

Este dashboard é um showcase do nosso trabalho e será continuamente atualizado com as evoluções do projeto PowerPolis. Contribuições são bem-vindas!
