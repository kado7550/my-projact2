import streamlit as st
import numpy as np

# 오목판 크기
BOARD_SIZE = 15

# 게임 상태 저장
if "board" not in st.session_state:
    st.session_state.board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)  # 0: 빈칸, 1: 흑돌, 2: 백돌
    st.session_state.turn = 1  # 1: 흑돌, 2: 백돌
    st.session_state.winner = 0

def check_win(board, x, y):
    """5목 체크: 가로, 세로, 대각선"""
    player = board[x, y]
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # →, ↓, ↘, ↙

    for dx, dy in directions:
        count = 1
        for dir in [1, -1]:
            nx, ny = x, y
            while True:
                nx += dx * dir
                ny += dy * dir
                if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and board[nx, ny] == player:
                    count += 1
                else:
                    break
        if count >= 5:
            return player
    return 0

def reset_game():
    st.session_state.board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)
    st.session_state.turn = 1
    st.session_state.winner = 0

# UI
st.title("🕹️ 2인용 오목 게임 (Gomoku)")
st.write("흑(●)과 백(○)이 번갈아 두는 전통적인 2인용 오목 게임입니다. 5목을 먼저 완성하는 사람이 승리합니다!")

# 게임판 표시
for i in range(BOARD_SIZE):
    cols = st.columns(BOARD_SIZE)
    for j in range(BOARD_SIZE):
        cell = st.session_state.board[i, j]
        if cell == 0 and st.session_state.winner == 0:
            if cols[j].button(" ", key=f"{i}-{j}"):
                st.session_state.board[i, j] = st.session_state.turn
                winner = check_win(st.session_state.board, i, j)
                if winner:
                    st.session_state.winner = winner
                else:
                    st.session_state.turn = 2 if st.session_state.turn == 1 else 1
        else:
            symbol = "●" if cell == 1 else ("○" if cell == 2 else " ")
            cols[j].markdown(f"<div style='text-align: center; font-size: 20px'>{symbol}</div>", unsafe_allow_html=True)

# 현재 상태
if st.session_state.winner:
    winner = "흑(●)" if st.session_state.winner == 1 else "백(○)"
    st.success(f"🎉 {winner} 승리!")
    if st.button("🔁 다시 시작"):
        reset_game()
else:
    turn = "흑(●)" if st.session_state.turn == 1 else "백(○)"
    st.info(f"현재 차례: {turn}")
