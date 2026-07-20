import streamlit as st
import requests
from utils.i18n import t

def app():
    st.title(t("analysis_title"))
    st.markdown(t("analysis_intro"))

    # Formulário de Input
    with st.form("analise_form"):
        col1, col2 = st.columns(2)
        with col1:
            consumo_kwh = st.slider(t("consumo_kwh_label"), 0, 5000, 420, help=t("consumo_kwh_help"))
            quantidade_equipamentos = st.slider(t("quantidade_equipamentos_label"), 1, 50, 10, help=t("quantidade_equipamentos_help"))
            tipo_imovel = st.selectbox(t("tipo_imovel_label"), ["Casa", "Apartamento", "Comercial", "Indústria"], help=t("tipo_imovel_help"))
        
        with col2:
            uso_horario_pico = st.checkbox(t("uso_horario_pico_label"), value=True, help=t("uso_horario_pico_help"))
            horas_alto_consumo = st.slider(t("horas_alto_consumo_label"), 0, 24, 8, help=t("horas_alto_consumo_help"))
            # Placeholder para possui_energia_solar - será adicionado após enriquecimento da base
            # possui_energia_solar = st.checkbox(t("possui_energia_solar_label"), value=False)

        submitted = st.form_submit_button(t("analyze_button"))

    if submitted:
        # Preparar payload para a API (URL do Backend será configurada)
        payload = {
            "consumo_kwh": consumo_kwh,
            "uso_horario_pico": uso_horario_pico,
            "quantidade_equipamentos": quantidade_equipamentos,
            "tipo_imovel": tipo_imovel,
            "horas_alto_consumo": horas_alto_consumo
            # "possui_energia_solar": possui_energia_solar # Adicionar quando a API suportar
        }

        st.markdown(t("analysis_result_title"))
        
        # Simulação de chamada à API (substituir pela URL real do Backend)
        try:
            # response = requests.post("http://localhost:8080/analise-energetica", json=payload)
            # data = response.json()
            
            # Dados mock para demonstração
            data = {
                "categoria": "Moderado",
                "probabilidade": 0.75,
                "recomendacoes": [
                    "Considere otimizar o uso de ar condicionado em horários de pico.",
                    "Verifique a eficiência de equipamentos antigos.",
                    "Aproveite a luz natural e desligue as luzes durante o dia."
                ],
                "custo_estimado_mensal": consumo_kwh * 0.75 # Tarifa de referência
            }

            categoria = data.get("categoria", "N/A")
            probabilidade = data.get("probabilidade", 0.0)
            recomendacoes = data.get("recomendacoes", [])
            custo_estimado = data.get("custo_estimado_mensal", 0.0)

            if categoria == "Eficiente":
                st.success(t("classification_efficient", categoria=categoria, probabilidade=probabilidade))
            elif categoria == "Moderado":
                st.warning(t("classification_moderate", categoria=categoria, probabilidade=probabilidade))
            else:
                st.error(t("classification_inefficient", categoria=categoria, probabilidade=probabilidade))
            
            st.info(t("estimated_cost", custo_estimado=custo_estimado))

            st.markdown(t("recommendations_title"))
            for rec in recomendacoes:
                st.write(f"- {rec}")

        except requests.exceptions.ConnectionError:
            st.error(t("error_api_connection"))
        except Exception as e:
            st.error(t("error_analysis", e=e))
