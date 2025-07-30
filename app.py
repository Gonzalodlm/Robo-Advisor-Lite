import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from scoring import score_user, bucket_to_label
from portfolios import MODEL_PORTFOLIOS

st.set_page_config(page_title="Robo-Advisor Lite", page_icon="💸")

# ---------- UI ----------
st.title("💸 Robo-Advisor Lite")
st.subheader("Completa el cuestionario y obtén un portafolio acorde a tu perfil de riesgo.")

with st.form("questionnaire"):
    st.write("### 10 preguntas sobre tu situación y tolerancia al riesgo")

    # 1
    age = st.slider("1️⃣  ¿Cuál es tu edad?", 18, 75, 30)

    # 2
    horizon = st.selectbox(
        "2️⃣  ¿Cuánto tiempo planificas mantener la inversión?",
        ("< 3 años", "3-5 años", "5-10 años", "> 10 años"),
    )

    # 3
    income = st.selectbox(
        "3️⃣  Proporción de tus ingresos que puedes invertir regularmente",
        ("< 5 %", "5-10 %", "10-20 %", "> 20 %"),
    )

    # 4
    knowledge = st.selectbox(
        "4️⃣  ¿Qué tan familiarizado estás con los mercados financieros?",
        ("Principiante", "Intermedio", "Avanzado"),
    )

    # 5
    max_drop = st.selectbox(
        "5️⃣  ¿Qué caída máxima (en %) tolerarías sin vender?",
        ("5 %", "10 %", "20 %", "30 %", "> 30 %"),
    )

    # 6
    reaction = st.selectbox(
        "6️⃣  Si tu portafolio cae 15 % en un mes, ¿qué harías?",
        ("Vendo todo", "Vendo una parte", "No hago nada", "Compro más"),
    )

    # 7
    liquidity = st.selectbox(
        "7️⃣  Necesidad de rescatar dinero rápidamente",
        ("Alta", "Media", "Baja"),
    )

    # 8
    goal = st.selectbox(
        "8️⃣  Principal objetivo de inversión",
        ("Proteger capital", "Ingresos regulares", "Crecimiento balanceado", "Máximo crecimiento"),
    )

    # 9
    inflation = st.selectbox(
        "9️⃣  ¿Qué opinas del riesgo de inflación sobre tus ahorros?",
        ("No me preocupa", "Me preocupa moderadamente", "Me preocupa mucho"),
    )

    #10
    digital = st.selectbox(
        "🔟  Grado de confianza en plataformas digitales para invertir",
        ("Baja", "Media", "Alta"),
    )

    submitted = st.form_submit_button("Calcular perfil 🔎")

if submitted:
    answers = dict(
        age=age,
        horizon=horizon,
        income=income,
        knowledge=knowledge,
        max_drop=max_drop,
        reaction=reaction,
        liquidity=liquidity,
        goal=goal,
        inflation=inflation,
        digital=digital,
    )

    bucket, total_score = score_user(answers)
    label = bucket_to_label[bucket]

    st.success(f"### Tu perfil: **{label}** (puntaje {total_score})")

    # Traer portafolio modelo
    pf = MODEL_PORTFOLIOS[bucket].copy()
    pf_df = pd.DataFrame(
        {"Ticker": pf.keys(), "Peso %": [v * 100 for v in pf.values()]}
    )

    # Gráfico
    fig, ax = plt.subplots()
    ax.pie(pf.values(), labels=pf.keys(), autopct="%1.0f%%", startangle=90)
    ax.axis("equal")
    st.pyplot(fig)

    st.write("#### Detalle de la cartera")
    st.table(pf_df)

    # Descargar CSV
    csv = pf_df.to_csv(index=False).encode()
    st.download_button(
        "📥 Descargar en CSV", csv, f"portfolio_{label}.csv", "text/csv"
    )

    st.info(
        """
        **Disclaimer**  
        Esta herramienta tiene fines **educativos** y no constituye recomendación personalizada
        según la normativa vigente. El usuario es responsable de sus decisiones de inversión.
        """
    )
