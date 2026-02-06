import streamlit as st

# Configuração da página
st.set_page_config(page_title="Para Minha Pequena", page_icon="❤️", layout="centered")

# --- ESTILO CSS (Corações caindo e Design) ---
st.markdown("""
    <style>
    /* Fundo da página */
    .stApp {
        background-color: #fff5f5;
    }

    /* Animação dos corações */
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

    /* Card decorativo */
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
    </style>

    <div class="heart" style="left:10%; animation-delay:0s;">❤️</div>
    <div class="heart" style="left:25%; animation-delay:2s;">❤️</div>
    <div class="heart" style="left:40%; animation-delay:1s;">❤️</div>
    <div class="heart" style="left:60%; animation-delay:3s;">❤️</div>
    <div class="heart" style="left:75%; animation-delay:0.5s;">❤️</div>
    <div class="heart" style="left:90%; animation-delay:1.5s;">❤️</div>
    """, unsafe_allow_stdio=True)

# --- CONTEÚDO DO SITE ---

st.title("💌 Uma surpresa para você...")

# Componente de Cartinha (Expander)
with st.expander("Clique aqui para abrir sua cartinha, minha princesa..."):
    st.write(f"""
    Minha pequena, 
    
    Escrevi isso para tentar colocar em palavras o que sinto por você. 
    Desde que você chegou, tudo ficou mais colorido e cheio de vida. 
    Você é a minha pequenina favorita, a dona do meu sorriso e o meu porto seguro.
    
    Prometo estar aqui por você, hoje e sempre.
    """)
    st.balloons() # Efeito extra de celebração ao abrir

st.write("---")

# Link do Vídeo (Papoulas - Yago Oproprio)
st.subheader("Nossa trilha sonora 🎵")
video_url = "http://www.youtube.com/watch?v=cyX-BUNcCqs"
st.video(video_url)

# Card Decorativo com a frase da música
st.markdown(f"""
    <div class="romantic-card">
        <i>"Eu mato, eu quebro, eu passo, eu quebro, eu chuto, eu vandalizo obstáculos só pra poder te ver passar..."</i>
        <br><br>
        <b>Minha princesa,</b> essa letra diz tudo. Não existe barreira no mundo que eu não enfrentaria por você. 
        Você é a razão do meu esforço e a paz no meu caos.
    </div>
    """, unsafe_allow_html=True)

# Declaração Final
st.markdown("<br>", unsafe_allow_html=True)
st.subheader("Eu te amo, minha pequena! ❤️")
st.write("Você é, e sempre será, a minha pequenina mais preciosa.")
