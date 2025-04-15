import streamlit as st

st.set_page_config(page_title="Fortune Teller", layout="centered")

st.header("Fortune Teller Game :sunglasses:", anchor="header", divider="orange")

st.write("Welcome to the Fortune Teller Game! :crystal_ball:")
st.write("You will select a color and a number and I will tell you what the future holds for you!")
st.write("Let's get started! :sparkles:")

color = st.selectbox("Select a colour", ("", "Yellow", "Green", "Blue", "Red"), index=0)
number = st.number_input("Select a number [1-8]", min_value=1, max_value=8, placeholder="Enter a number", step=1)

# Use flag to check if user made both selections
process = color != "" and number is not None

if color:
    st.write(f"Color selected: {color}")
if number:
    st.write(f"Number selected: {number}")

if st.button("🔍 Process"):
    if process:
        color_lower = color.lower()
        if color_lower in ["yellow", "green"]:
            if number == 1:
                st.write("Worried about your future career? Don't worry. You'll 100% get what you want, be patient!")
            elif number == 2:
                st.write("You will become a millionaire at the age of 35!")
            elif number == 5:
                st.write("You will have a great family with 10 kids!")
            elif number == 6:
                st.write("You will become famous and everyone will love you!")
            else:
                st.write("Try numbers 1, 2, 5, or 6 for Yellow/Green!")

        elif color_lower in ["blue", "red"]:
            if number == 3:
                st.write("You will live a happy life for 100 years at least!")
            elif number == 4:
                st.write("You will become a successful doctor one day!")
            elif number == 7:
                st.write("All your dreams will come true, just be patient!")
            elif number == 8:
                st.write("You're lucky, You will have it all one day!")
            else:
                st.write("Try numbers 3, 4, 7, or 8 for Blue/Red!")
    else:
        st.warning("Please select both a color and a number before processing.")
