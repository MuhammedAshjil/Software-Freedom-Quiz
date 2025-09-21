import streamlit as st
from pathlib import Path
import random

# ===============================
# 🌐 PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="Software Freedom Day –Quiz",
    page_icon="🌐",
    layout="centered"
)

# ===============================
# 🎨 GLOBAL CSS
# ===============================
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.pexels.com/photos/3826435/pexels-photo-3826435.jpeg");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        color: #ffffff;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .locked-level {
        background: rgba(0,0,0,0.6);
        padding: 10px;
        margin: 5px 0;
        color: #FFF;
        text-align: center;
        border-radius: 5px;
        font-weight: bold;
    }
    @keyframes float {
        0% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0); }
    }
    .float-title{
        text-align:center;
    }
    .float-title span {
        display:inline-block;
        font-size:50px;
        color: #FF4040;
        animation: float 2s ease-in-out infinite;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Optional extra smoke animation if file exists
css_file = Path("assets/smoke.css")
if css_file.exists():
    st.markdown(f"<style>{css_file.read_text()}</style><div class='smoke-bg'></div>",
                unsafe_allow_html=True)

# ===============================
# 🧩 SESSION STATE
# ===============================
if "level" not in st.session_state:
    st.session_state.level = 0
if "score" not in st.session_state:
    st.session_state.score = 0

# ===============================
# ❓ QUESTIONS
# ===============================
QUESTIONS = [
    {"q": "SFD celebrates freedom of what kind of software? (2 words)", "a": "free software"},
    {"q": "Which animal is the Linux mascot?", "a": "penguin"},
    {"q": "The license protecting user freedom (3 letters)", "a": "gpl"},
    {"q": "Popular version-control system used in open source (3 letters)", "a": "git"},
    {"q": "Founder of the Free Software Foundation (full name)", "a": "richard stallman"},
    {"q": "Name the OS famous for its mascot Tux", "a": "linux"}
]

# ===============================
# 🏆 HEADER
# ===============================
st.markdown(
    """
    <h1 class="float-title" style="font-family:georgia;color:blue;">
      <span>Q</span><span>U</span><span>I</span><span>Z</span>
    </h1>
    """,
    unsafe_allow_html=True
)
st.markdown(
    "<h2 style='text-align:center;font-family:verdana;'>Based on <b>Software Freedom Day</b></h2>",
    unsafe_allow_html=True
)


# st.image("https://media.tenor.com/DQRSMm8uuq4AAAAi/tamil-hindu.gif")


# ===============================
# ℹ️ INTRODUCTION
# ===============================
st.divider()
st.markdown(
    """
    <p style='text-align:center;font-size:17px;'>
    Software Freedom Day (SFD) is a worldwide celebration of Free and Open Source Software (FOSS). 
    Our goal is to educate the public about the benefits of using high-quality FOSS in education, 
    government, at home, and in business.
    </p>
    <div style='text-align:center;'>
      <a href='https://digitalfreedoms.org/en/sfd' target='_blank'
         style='font-family:Garamond;text-decoration:none;'>
         <u>-- Digital Freedom Foundation</u>
      </a>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()
st.subheader("Answer each question to unlock the next :orange[level]!")
st.markdown(
    """
    <div style="display:flex; justify-content:center;">
        <img src="https://media.tenor.com/DQRSMm8uuq4AAAAi/tamil-hindu.gif" width="300">
    </div>
    """,
    unsafe_allow_html=True
)

# ===============================
# 🕹️ GAME LOOP
# ===============================
for i, q in enumerate(QUESTIONS):
    current_level = st.session_state.level

    if i < current_level:
        st.success(f"✅ Level {i+1} cleared!")
    elif i == current_level:
        st.subheader(f"Level {i+1}")
        st.info(q["q"])
        ans = st.text_input("Your Answer:", key=f"ans_{i}")
        if st.button("Submit", key=f"submit_{i}"):
            if ans.lower().strip() == q["a"]:
                st.session_state.level += 1
                st.session_state.score += 10
                st.success(f"🎉 Correct! Level {i+1} completed.")
                st.balloons()
            else:
                st.error("❌ Wrong answer. Try again!")
                st.image("https://media.tenor.com/ve3YH1XBAyIAAAAi/uarrr-disappointed.gif", caption="Disappointed…")
    else:
        st.markdown(f"<div class='locked-level'>Level {i+1} Locked 🔒</div>", unsafe_allow_html=True)

# ===============================
# 🎉 WIN STATE
# ===============================
if st.session_state.level >= len(QUESTIONS):
    if st.session_state.level >= len(QUESTIONS):
        # st.balloons()  # built-in falling balloons 🎈

        st.markdown(
            """
            <style>
            @keyframes fall {
                0%   {transform: translateY(-10vh) rotate(0deg);}
                100% {transform: translateY(110vh) rotate(720deg);}
            }
            .confetti-piece {
                position: fixed;
                top: -10vh;
                width: 15px;
                height: 15px;
                opacity: 0.9;
                border-radius: 2px;
                animation: fall 4s linear infinite;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # create many colored confetti divs with random left positions & animation delays
        colors = ["#FF595E", "#FFCA3A", "#8AC926", "#1982C4", "#6A4C93", "#FF9F1C","#FA0096","#00FAE1","#000CFA","#00FA15"]
        pieces = ""
        for i in range(60):  # number of confetti pieces
            left = random.randint(0, 100)  # percentage across the screen
            delay = round(random.uniform(0, 4), 2)  # animation delay
            color = random.choice(colors)
            pieces += (
                f'<div class="confetti-piece" '
                f'style="left:{left}vw; background:{color}; '
                f'animation-delay:{delay}s;"></div>'
            )

        st.markdown(pieces, unsafe_allow_html=True)

        st.markdown(
            """
            <div style="text-align:center;">
                <h1>Congratulations! You Cleared All Levels </h1>
                <img src="https://media.tenor.com/z93T38sX_HAAAAAi/woo-yey.gif" width="500">
            </div>
            """,
            unsafe_allow_html=True
        )
    # st.success(f"🎯 Congratulations! You completed all 6 levels "
    #            f"with a total score of **{st.session_state.score}**")

    if st.button("Play Again"):
        st.session_state.level = 0
        st.session_state.score = 0
# st.markdown(
#     """
#     <div style="text-align:center;color:#94BBE9;opacity:0.5;">
#         <h5 style="font-family:Courier New"><br><br><br><i>
#         Created Ashjil </i>
#         </h5>
#
#     </div>
#     """,
#     unsafe_allow_html=True
# )
