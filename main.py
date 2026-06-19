import streamlit as st
import time

# 1. Configuração da Página Streamlit (Mudança de ícone e visual amplo)
st.set_page_config(page_title="SafeSupport IA", page_icon="🛡️", layout="centered")

# --- NOVO DESIGN E TÍTULO ---
st.title("🛡️ SafeSupport IA – Triagem e Atendimento")
st.caption("Sistema inteligente de atendimento integrando Redes Neurais (TensorFlow) e Engenharia de Prompt.")
st.markdown("<style>div.stButton > button:first-child { background-color: #2E7D32; color: white; }</style>", unsafe_allow_html=True) # Customização do botão para Verde
st.markdown("---")

# 2. Input do Usuário
user_input = st.text_area("Descreva o ocorrido ou sua dúvida técnica:", placeholder="Ex: Meu produto veio quebrado! ou Como ligo o aparelho?")

# Botão de enviar
if st.button("Iniciar Análise Inteligente", type="primary"):
    if user_input:
        with st.spinner("🧠 Redes Neurais do TensorFlow analisando o padrão do texto..."):
            time.sleep(1) # Simula o tempo de processamento do TensorFlow
            
            # SIMULAÇÃO DO TENSORFLOW
            if any(palavra in user_input.lower() for palavra in ["quebrado", "defeito", "ruim", "erro", "estragou"]):
                classificacao = "ALTA URGÊNCIA (Reclamação Crítica / Defeito)"
                cor_alerta = "danger"
                
                # SIMULAÇÃO DO FRAMEWORK DE PROMPT (Resposta para caso urgente)
                resposta_prompt = f"""
                **[PROMPT FRAMEWORK: Ativando Persona de Ouvidoria e Soluções]**
                
                Olá! Sentimos muito pelo transtorno com o seu produto. 
                O nosso modelo identificou que o seu caso exige **{classificacao}**. 
                
                Direcionamos o seu histórico para a nossa equipe de contingência humana. Um especialista entrará em contato prioritário em instantes. 
                
                *Código do Incidente: #2026-{int(time.time())}*
                """
            else:
                classificacao = "RESOLUÇÃO IMEDIATA (Dúvida Geral / Operação)"
                cor_alerta = "info"
                
                # SIMULAÇÃO DO FRAMEWORK DE PROMPT (Resposta para caso simples)
                resposta_prompt = f"""
                **[PROMPT FRAMEWORK: Ativando Persona de Suporte Técnico Nível 1]**
                
                Olá! Obrigado por entrar em contato. 
                O modelo classificou sua solicitação como **{classificacao}**.
                
                Instruções sugeridas para: '{user_input}': 
                Verifique se os cabos estão firmes e se o interruptor principal está acionado. O guia rápido completo foi enviado ao seu painel.
                """

        # --- SEÇÃO DE RESULTADOS COM NOVAS CORES ---
        st.subheader("📊 Diagnóstico do Modelo TensorFlow")
        if cor_alerta == "danger":
            # Usando toast para um efeito visual de alerta extra
            st.toast("Alerta crítico detectado!", icon="⚠️")
            st.error(f"Classe de Risco: {classificacao}")
        else:
            st.toast("Mensagem processada normalmente.", icon="✅")
            st.success(f"Classe Informativa: {classificacao}") # Mudado de .info (azul) para .success (verde)
            
        st.markdown("---")
        
        st.subheader("💬 Output do Framework de Prompt")
        
        # Exibindo o prompt dentro de um box estilizado amarelo/laranja (warning) para diferenciar as cores
        st.warning(resposta_prompt)
        
    else:
        st.warning("Por favor, digite alguma coisa antes de enviar.")
