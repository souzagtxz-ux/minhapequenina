import streamlit as st

# Configuração da página
st.set_page_config(page_title="Para Minha Pequena", page_icon="❤️", layout="centered")

# --- ESTILO CSS (Corações, Design e Efeito Glow) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #fff5f5;
    }
    
    /* Efeito de Glow/Sombra no texto para destacar do fundo */
    .glow-text {
        color: white;
        text-shadow: 0px 0px 8px rgba(0, 0, 0, 0.8), 0px 0px 2px rgba(0, 0, 0, 1);
        font-size: 1.2rem;
        line-height: 1.6;
    }
    
    h1, h2, h3 {
        color: #ff4b4b !important;
        text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.2);
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

    div.stButton > button:first-child {
        background-color: #ff4b4b;
        color: white;
        border-radius: 20px;
        padding: 10px 25px;
        border: none;
        font-size: 18px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
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

if not st.session_state.aberto:
    st.write("Tem algo especial guardado aqui para você, minha princesa.")
    if st.button("Abrir Cartinha"):
        st.session_state.aberto = True
        st.rerun()

# --- CONTEÚDO REVELADO ---
if st.session_state.aberto:
    st.balloons()
    
    # Texto da cartinha com a classe glow-text
    st.markdown("""
    <div class="glow-text">
    <h3>Minha Pequena,</h3>
    Escrevi isso para tentar colocar em palavras o que sinto por você. <br>
    Desde que você chegou, tudo ficou mais colorido e cheio de vida. <br>
    Você é a minha <b>pequenina</b> favorita, a dona do meu sorriso e o meu porto seguro. <br><br>
    Prometo estar aqui por você, hoje e sempre, minha princesa.
    </div>
    """, unsafe_allow_html=True)
    
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
