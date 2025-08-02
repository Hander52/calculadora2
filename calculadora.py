import streamlit as st

st.title("Calculadora de Distribuição de Salário 💰")

# Entrada do salário
salario = st.number_input("Digite seu salário (R$):", min_value=0.0, format="%.2f")

if salario > 0:
    st.subheader("Sugestão de divisão (50/30/20):")
    st.write(f"🏠 50% para Despesas de casa: R$ {salario * 0.5:.2f}")
    st.write(f"🧍 30% para Gastos pessoais: R$ {salario * 0.3:.2f}")
    st.write(f"📈 20% para Investimentos: R$ {salario * 0.2:.2f}")

    st.markdown("---")

    st.subheader("Personalize os percentuais (tem que somar 100%)")

    despesas = st.slider("🏠 Despesas de casa (%)", 0, 100, 50)
    pessoais = st.slider("🧍 Gastos pessoais (%)", 0, 100, 30)
    investimentos = st.slider("📈 Investimentos (%)", 0, 100, 20)

    total_percentual = despesas + pessoais + investimentos

    # Barra de progresso visual
    st.write(f"🔢 Soma atual dos percentuais: {total_percentual}%")
    st.progress(min(int(total_percentual), 100))

    if total_percentual != 100:
        st.error("⚠️ A soma dos percentuais deve ser exatamente 100% para continuar.")
    else:
        if st.button("Calcular distribuição"):
            valor_despesas = salario * despesas / 100
            valor_pessoais = salario * pessoais / 100
            valor_investimentos = salario * investimentos / 100

            st.success("✅ Percentuais válidos! Veja como ficou a divisão:")

            st.write(f"🏠 Despesas de casa: R$ {valor_despesas:.2f}")
            st.write(f"🧍 Gastos pessoais: R$ {valor_pessoais:.2f}")
            st.write(f"📈 Investimentos: R$ {valor_investimentos:.2f}")