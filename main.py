# import streamlit as st
# from pathlib import Path
# import base64

# # --- Page Configuration ---
# st.set_page_config(
#     page_title="Software Freedom Day",
#     page_icon="🌐",
#     layout="centered"
# )

# # --- Background Gradient and Locked Level CSS ---
# # st.markdown("""
# # <style>
# # .stApp {
# #     background: linear-gradient(to right, #000000, #68A692, #000000);
# # }
# # .locked-level {
# #     background: rgba(0, 0, 0, 0.6);
# #     padding: 10px;
# #     margin: 5px 0;
# #     color: #FFF;
# #     text-align: center;
# #     border-radius: 5px;
# #     font-weight: bold;
# # }
# # </style>
# # """, unsafe_allow_html=True)



# def get_base64_of_bin_file(bin_file):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# img_path = "C:\Users\self1\Desktop\treassure hunt\images"   # or "assets/gradient.jpeg"
# img_base64 = get_base64_of_bin_file(img_path)

# st.markdown(
#     f"""
#     <style>
#     .stApp {{
#         background: url("data:image/jpeg;base64,{img_base64}");
#         background-size: cover;
#         background-repeat: no-repeat;
#         background-attachment: fixed;
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True
# )


# # --- Inject Smoke CSS if available ---
# css_file = Path("assets/smoke.css")
# if css_file.exists():
#     st.markdown(
#         f"<style>{css_file.read_text()}</style><div class='smoke-bg'></div>",
#         unsafe_allow_html=True
#     )

# # --- Session State Initialization ---
# if "level" not in st.session_state:
#     st.session_state.level = 0
# if "score" not in st.session_state:
#     st.session_state.score = 0
# if "submitted" not in st.session_state:
#     st.session_state.submitted = False

# # --- Questions (6 Levels) ---
# QUESTIONS = [
#     {"q": "SFD celebrates freedom of what kind of software? (2 words)", "a": "free software"},
#     {"q": "Which animal is the Linux mascot?", "a": "penguin"},
#     {"q": "The license protecting user freedom (3 letters)", "a": "gpl"},
#     {"q": "Popular version-control system used in open source (3 letters)", "a": "git"},
#     {"q": "Founder of the Free Software Foundation (full name)", "a": "richard stallman"},
#     {"q": "Name the OS famous for its mascot Tux", "a": "linux"}
# ]

# # --- Title and Description ---
# st.markdown("<h1 style='text-align: center;color:#C9264C'>Software Freedom Day</h1>", unsafe_allow_html=True)
# st.markdown("<h1 style='text-align: center;color:#FAF264'>Treasure Hunt</h1>", unsafe_allow_html=True)
# st.divider()
# with st.container():
#  st.markdown(
#     "<p style='text-align: center; font-size:17px;color:#FFF0F0'>"
#     "Software Freedom Day (SFD) is a worldwide celebration of Free and Open Source Software (FOSS). "
#     "Our goal is to educate the worldwide public about the benefits of using high quality FOSS in education, "
#     "government, at home, and in business. Digital Freedom Foundation coordinates SFD globally, providing support "
#     "and collaboration, while volunteer teams organize local events to impact their communities."
#     "</p>",
#     unsafe_allow_html=True
# )

# # st.markdown("<p style='text-align: center; font-size:20px;color:#239FF7'>- Digital Freedom Foundation</p>", unsafe_allow_html=True)
# # st.write("[Digital Freedom Foundation](https://digitalfreedoms.org/en/sfd)")
# # st.markdown(
# #     '<a href="https://digitalfreedoms.org/en/sfd" style="color: #FF0000; font-weight: bold;text-align:center;">Digital Freedom Foundation</a>',
# #     unsafe_allow_html=True
# # )
# # st.markdown(
# #     """
# #     <div style='text-align: center;'>
# #         <a href='https://digitalfreedoms.org/en/sfd' target='_blank'
# #         style="color:red;">
# #
# #            -- Digital Freedom Foundation
# #         </a>
# #     </div>
# #     """,
# #     unsafe_allow_html=True
# # )
# st.markdown(
#     """
#     <div style='text-align: center;'>
#         <a href='https://digitalfreedoms.org/en/sfd'
#            target='_blank'
#            style='color: #FF0000; text-decoration: none;'>
#            -- Digital Freedom Foundation
#         </a>
#     </div>
#     """,
#     unsafe_allow_html=True
# )

# st.divider()
# st.write("Answer each question to unlock the next level. Good luck! 🌐💡")

# # --- Game Display ---
# for i, q in enumerate(QUESTIONS):
#     current_level = st.session_state.level

#     if i < current_level:
#         st.success(f"✅ Level {i+1} cleared!")
#     elif i == current_level:
#         st.subheader(f"Level {i+1}")
#         st.info(q["q"])
#         ans = st.text_input("Your Answer:", key=f"answer_{i}")
#         submit_pressed = st.button("Submit", key=f"submit_{i}")

#         if submit_pressed:
#             if ans.lower().strip() == q["a"]:
#                 st.session_state.level += 1
#                 st.session_state.score += 10
#                 st.success(f"Correct! Level {i+1} completed. 🎉 Next level unlocked!")
#             else:
#                 st.error("❌ Wrong answer. Try again!")
#     else:
#         st.markdown(f"<div class='locked-level'>Level {i+1} Locked 🔒</div>", unsafe_allow_html=True)

# # --- Win Animation ---
# if st.session_state.level >= len(QUESTIONS):
#     st.balloons()
#     st.success(f"🎉 Congratulations! You completed all 6 levels with a score of {st.session_state.score} 🎯")

#     # Optional: Confetti animation if available
#     confetti_path = Path("assets/confetti.js")
#     if confetti_path.exists():
#         confetti_js = confetti_path.read_text()
#         st.markdown(
#             f"""
#             <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
#             <script>{confetti_js}</script>
#             """,
#             unsafe_allow_html=True
#         )

#     # Play Again button
#     if st.button("Play Again"):
#         st.session_state.level = 0
#         st.session_state.score = 0
    print("Operation complete! \a")