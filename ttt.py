import streamlit as st

st.title("🎮 Tic-Tac-Toe Game")

if "board" not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.current_player = "x"
    st.session_state.winner = None

def check_winner(board):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for i, j, k in wins:
        if board[i] == board[j] == board[k] and board[i] != "":
            return board[i]
    if "" not in board:
        return "Draw"
    return None

def play(index):
    if st.session_state.board[index] == "" and st.session_state.winner is None:
        st.session_state.board[index] = st.session_state.current_player
        st.session_state.winner = check_winner(st.session_state.board)
        if st.session_state.winner is None:
            st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"

cols = st.columns(3)
for i in range(3):
    for j in range(3):
        idx = i*3 + j
        with cols[j]:
            if st.button(st.session_state.board[idx] or " ", key=idx):
                play(idx)

if st.session_state.winner == "Draw":
    st.success("It's a Draw")
elif st.session_state.winner:
    st.success(f"🎉 Player {st.session_state.winner} wins!")
else:
    st.info(f"Player {st.session_state.current_player}'s turn")

if st.button("🔄 Reset Game"):
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None
