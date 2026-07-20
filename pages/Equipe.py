import streamlit as st
from utils.i18n import t

def app():
    st.title(t("team_title"))
    st.markdown(t("team_intro"))

    team_members = [
        {
            "name": "Lídi Moura",
            "role": t("role_lidi"),
            "specialty": t("specialty_lidi"),
            "linkedin": "https://www.linkedin.com/in/lidimoura/",
            "github": "https://github.com/lidimoura",
            "avatar": "https://avatars.githubusercontent.com/u/195331493?v=4"
        },
        {
            "name": "Pedro Henrique Rodrigues da Costa Tireli",
            "role": t("role_pedro"),
            "specialty": t("specialty_pedro"),
            "linkedin": "https://www.linkedin.com/in/phtirelli/",
            "github": "https://github.com/phtirelli",
            "avatar": "https://avatars.githubusercontent.com/u/100102157?v=4"
        },
        {
            "name": "Samanta Sá",
            "role": t("role_samanta"),
            "specialty": t("specialty_samanta"),
            "linkedin": "https://www.linkedin.com/in/engsamantasa/",
            "github": "https://github.com/engsamantasa",
            "avatar": "https://avatars.githubusercontent.com/u/227623247?v=4"
        },
        {
            "name": "Kauã da Silva Barros",
            "role": t("role_kaua"),
            "specialty": t("specialty_kaua"),
            "linkedin": None,
            "github": "https://github.com/kaua3-c",
            "avatar": "https://avatars.githubusercontent.com/u/68451290?v=4"
        },
        {
            "name": "Alan Anderson",
            "role": t("role_alan"),
            "specialty": t("specialty_alan"),
            "linkedin": "https://www.linkedin.com/in/alan-anderson-dev/",
            "github": "https://github.com/alanandersondev",
            "avatar": "https://avatars.githubusercontent.com/u/298712983?v=4"
        },
        {
            "name": "Mayara Medeiros Giangiacomo",
            "role": t("role_mayara"),
            "specialty": t("specialty_mayara"),
            "linkedin": None,
            "github": None,
            "avatar": 
        },
        {
            "name": "Alex Furukawa",
            "role": t("role_alex"),
            "specialty": t("specialty_alex"),
            "linkedin": "https://www.linkedin.com/in/lexkawa/",
            "github": "https://github.com/dev-corvus/",
            "avatar": "https://avatars.githubusercontent.com/u/98266359?v=4"
        },
        {
            "name": "Antônio Carlos Martins Teixeira",
            "role": t("role_antonio"),
            "specialty": t("specialty_antonio"),
            "linkedin": "www.linkedin.com/in/antonio-carlos-martins-teixeira",
            "github": "https://github.com/digichargeac",
            "avatar": "https://avatars.githubusercontent.com/u/217652752?v=4"
        },
        {
            "name": "Dryelli Vitoria Martins de Freitas",
            "role": t("role_dryelli"),
            "specialty": t("specialty_dryelli"),
            "linkedin": None,
            "github": None,
            "avatar": 
        },
    ]

    # Organizar por área para exibição
    st.markdown(f"## {t("ds_analytics_title")}")
    ds_members = [m for m in team_members if "Data Analyst" in m["role"] or "Data Scientist" in m["role"]]
    cols = st.columns(len(ds_members))
    for i, member in enumerate(ds_members):
        with cols[i]:
            st.image(member["avatar"], width=100)
            st.subheader(member["name"].split("|")[0].strip())
            st.write(f"**{member["role"]}**")
            st.caption(member["specialty"])
            if member["linkedin"]:
                st.markdown(f"[LinkedIn]({member["linkedin"]})")
            if member["github"]:
                st.markdown(f"[GitHub]({member["github"]})")

    st.markdown(f"## {t("backend_dev_title")}")
    be_members = [m for m in team_members if "Backend Developer" in m["role"]]
    cols = st.columns(len(be_members))
    for i, member in enumerate(be_members):
        with cols[i]:
            st.image(member["avatar"], width=100)
            st.subheader(member["name"].split("|")[0].strip())
            st.write(f"**{member["role"]}**")
            st.caption(member["specialty"])
            if member["linkedin"]:
                st.markdown(f"[LinkedIn]({member["linkedin"]})")
            if member["github"]:
                st.markdown(f"[GitHub]({member["github"]})")

    st.markdown(f"## {t("fs_frontend_dev_title")}")
    fe_members = [m for m in team_members if "Full Stack" in m["role"] or "Frontend" in m["role"]]
    cols = st.columns(len(fe_members))
    for i, member in enumerate(fe_members):
        with cols[i]:
            st.image(member["avatar"], width=100)
            st.subheader(member["name"].split("|")[0].strip())
            st.write(f"**{member["role"]}**")
            st.caption(member["specialty"])
            if member["linkedin"]:
                st.markdown(f"[LinkedIn]({member["linkedin"]})")
            if member["github"]:
                st.markdown(f"[GitHub]({member["github"]})")

    st.markdown(f"## {t("architecture_title")}")
    arch_members = [m for m in team_members if "Architect" in m["role"]]
    cols = st.columns(len(arch_members))
    for i, member in enumerate(arch_members):
        with cols[i]:
            st.image(member["avatar"], width=100)
            st.subheader(member["name"].split("|")[0].strip())
            st.write(f"**{member["role"]}**")
            st.caption(member["specialty"])
            if member["linkedin"]:
                st.markdown(f"[LinkedIn]({member["linkedin"]})")
            if member["github"]:
                st.markdown(f"[GitHub]({member["github"]})")

    st.markdown(f"""
    --- 
    
    ### {t("collaboration_title")}
    {t("collaboration_text")}
    """)

if __name__ == "__main__":
    app()
