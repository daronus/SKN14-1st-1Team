import streamlit as st

pages = {
    "Comp CarDiB": [
        st.Page("app.py", title="🚗 자동차 스펙 비교하기"),
        st.Page("graph_page.py", title="📊 자세하게 비교하기"),
    ]
}

pg = st.navigation(pages)
pg.run()

st.markdown(
    """
        <style>
            [data-testid="stSidebar"] {
                background-image: url(https://cdn.discordapp.com/attachments/1349656172692766722/1366641943035252817/logo.png?ex=6811affe&is=68105e7e&hm=3ea461a0899ee462e47db5140a88eb66902576f6bc40b4609df33e8ffae69b64&);
                background-repeat: no-repeat;
                padding-top: 80px;
                background-size: 335px;
            }
        </style>
        """,
    unsafe_allow_html=True,
)