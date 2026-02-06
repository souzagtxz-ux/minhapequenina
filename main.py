import streamlit as st

# Configuração da página
st.set_page_config(page_title="Para Minha Pequena", page_icon="❤️", layout="centered")

# --- ESTILO CSS (Corações e Design) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #fff5f5;
    }
    @keyframes snowflakes {
        0% { top: -10%; }
        100% { top: 100%; }
    }
    .heart {
        position: fixed;
        top: -10%;
        color: #ff4b4b;
        font-size: 20px;
        user-select: none;
        z-index: 9999;
        animation-name: snowflakes;
        animation-duration: 5s;
        animation-iteration-count: infinite;
        animation-timing-function: linear;
    }
    .romantic-card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        border-left: 10px solid #ff4b4b;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.1);
        color: #4a4a4a;
        font-family: 'Georgia', serif;
        margin-top: 20px;
    }
    /* Estilo para o botão ficar bonitinho */
    div.stButton > button:first-child {
        background-color: #ff4b4b;
        color: white;
        border-radius: 20px;
        padding: 10px 25px;
        border: none;
        font-size: 18px;
    }
    </style>

    <div class="heart" style="left:10%; animation-delay:0s;">❤️</div>
    <div class="heart" style="left:25%; animation-delay:2s;">❤️</div>
    <div class="heart" style="left:40%; animation-delay:1s;">❤️</div>
    <div class="heart" style="left:60%; animation-delay:3s;">❤️</div>
    <div class="heart" style="left:75%; animation-delay:0.5s;">❤️</div>
    <div class="heart" style="left:90%; animation-delay:1.5s;">❤️</div>
    """, unsafe_allow_html=True)

# --- LÓGICA DE ABRIR A CARTINHA ---
if 'aberto' not in st.session_state:
    st.session_state.aberto = False

st.title("💌 Você recebeu uma mensagem...")

# Só mostra o botão se a cartinha não estiver aberta
if not st.session_state.aberto:
    st.write("Tem algo especial guardado aqui para você, minha princesa.")
    if st.button("Abrir Cartinha"):
        st.session_state.aberto = True
        st.rerun() # Recarrega a página para mostrar o conteúdo

# --- CONTEÚDO REVELADO ---
if st.session_state.aberto:
    st.balloons() # Efeito de balões ao abrir
    
    st.markdown("""
    ### Minha Pequena,
    Escrevi isso para tentar colocar em palavras o que sinto por você. 
    Desde que você chegou, tudo ficou mais colorido e cheio de vida. 
    Você é a minha **pequenina** favorita, a dona do meu sorriso e o meu porto seguro.
    
    Prometo estar aqui por você, hoje e sempre, minha princesa.
    """)
    
    st.write("---")
    
    # Música
    st.subheader("Nossa trilha sonora 🎵")
    video_url = "http://www.youtube.com/watch?v=cyX-BUNcCqs"
    st.video(video_url)
    
    # Card Decorativo
    st.markdown(f"""
        <div class="romantic-card">
            <i>"Eu mato, eu quebro, eu passo, eu quebro, eu chuto, eu vandalizo obstáculos só pra poder te ver passar..."</i>
            <br><br>
            <b>Minha princesa,</b> essa letra diz tudo. Não existe barreira no mundo que eu não enfrentaria por você. 
            Você é a razão do meu esforço e a paz no meu caos. Te amo, minha pequenina.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Eu te amo, minha pequena! ❤️")
