import streamlit as st
import random

st.title("Number Guessing Game")
st.write("I'm thinking of a number between 1 and 100. Can you guess it?")

if 'number' not in st.session_state:
    st.session_state.number = random.randint(1,100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button("Guess"):
    if not st.session_state.game_over:
        st.session_state.attempts += 1

        if guess < st.session_state.number:
            st.warning("Too low! Try again.")
        elif guess > st.session_state.number:
            st.warning("Too high! Try again.")
        else:
            st.success(f"Correct! The number was {st.session_state.number}")
            st.info(f"You took {st.session_state.attempts} attempts.")
            st.session_state.game_over = True

if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.number = random.randint(1,100)
        st.session_state.attempts = 0
        st.session_state.game_over = False