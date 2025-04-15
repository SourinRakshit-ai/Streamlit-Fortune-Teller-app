import streamlit as st

# Set page config first
st.set_page_config(page_title="🔮 Mystic Fortune Teller", layout="centered")

# Handle reset by checking a session flag
if "reset_triggered" not in st.session_state:
    st.session_state.reset_triggered = False

if st.session_state.reset_triggered:
    st.session_state.update({
        "color_key": "",
        "number_key": None,
        "reset_triggered": False  # Reset the trigger
    })

# App Header
st.markdown("<h1 style='text-align: center; color: #8A2BE2;'>🔮 Mystic Fortune Teller Game</h1>", unsafe_allow_html=True)
st.markdown("<hr style='border: 2px solid #8A2BE2;'>", unsafe_allow_html=True)

# Intro
st.markdown("""
<div style='text-align: center; font-size: 18px;'>
    ✨ Welcome to the <b>Mystic Fortune Teller</b>! ✨<br>
    Choose a color and a number, and the crystal ball will reveal your destiny! 🔮
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Inputs with keys
color = st.selectbox(
    "🌈 Select a color",
    ("", "Yellow", "Green", "Blue", "Red"),
    index=0,
    key="color_key"
)

number = st.number_input(
    "🔢 Select a number [1-8]",
    min_value=1,
    max_value=8,
    placeholder="Enter a number",
    value=st.session_state.get("number_key", None),
    key="number_key"
)

process = 0
if st.session_state.color_key and st.session_state.number_key:
    st.success(f"🎯 You selected: **{st.session_state.color_key}** and **{st.session_state.number_key}**")
    st.markdown("🔔 You are ready to play!")
    process = 1

# Buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("🔍 Abracadabra..."):
        if process == 1:
            color = st.session_state.color_key.lower()
            number = st.session_state.number_key
            if color in ("yellow", "green"):
                if number == 1:
                    st.info("🌟 Worried about your career? You'll 100% get what you want – be patient!")
                elif number == 2:
                    st.success("💰 You will become a millionaire at the age of 35!")
                elif number == 5:
                    st.warning("👶 You will have a great family with 10 kids!")
                elif number == 6:
                    st.success("🌟 You will become famous and loved by everyone!")
                else:
                    st.error("⛔ Only numbers 1, 2, 5, 6 are valid for Yellow/Green!")
            elif color in ("blue", "red"):
                if number == 3:
                    st.success("💖 You will live a happy life for 100+ years!")
                elif number == 4:
                    st.success("🏥 You will become a successful doctor one day!")
                elif number == 7:
                    st.success("🌈 All your dreams will come true – just be patient!")
                elif number == 8:
                    st.success("🎉 You're lucky – you will have it all one day!")
                else:
                    st.error("⛔ Only numbers 3, 4, 7, 8 are valid for Blue/Red!")
        else:
            st.warning("⛔ Please select both a color and a number to proceed.")

with col2:
    if st.button("🔄 Reset"):
        st.session_state.reset_triggered = True
        st.rerun()