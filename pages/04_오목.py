import streamlit as st
import numpy as np

BOARD_SIZE = 15
STAR_POINTS = [(3, 3), (3, 11), (7, 7), (11, 3), (11, 11)]

# 초기화
if "board" not in st.session_state:
    st.session_state.board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)
    st.session_state.turn = 1
    st.session_state.winner = 0

def check_win(board, x, y):
    player = board[x, y]
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
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

# 스타일 적용
st.markdown("""
<style>
    div[data-testid="column"] {
        padding: 0px !important;
    }
    button[kind="secondary"] {
        background-color: #e6c07b !important;
        border: none !important;
        height: 38px !important;
        width: 38px !important;
        padding: 0px !important;
    }
    .stone {
        font-size: 26px;
        line-height: 38px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

st.title("🎯 현실감 있는 2인용 오목 게임")
st.caption("전통 오목판 스타일의 15x15 바둑판입니다. 흑(●), 백(○) 번갈아가며 두세요. 5목이면 승리!")

# 보드 출력
for i in range(BOARD_SIZE):
    cols = st.columns(BOARD_SIZE)
    for j in range(BOARD_SIZE):
        cell = st.session_state.board[i, j]
        symbol = ""
        is_star = (i, j) in STAR_POINTS

        if cell == 1:
            symbol = "●"  # 흑돌
        elif cell == 2:
            symbol = "○"  # 백돌
        elif is_star:
            symbol = "•"  # 천원 or 별점
        else:
            symbol = "╋"  # 선 교차점

        if cell == 0 and st.session_state.winner == 0:
            if cols[j].button(" ", key=f"{i}-{j}"):
                st.session_state.board[i, j] = st.session_state.turn
                winner = check_win(st.session_state.board, i, j)
                if winner:
                    st.session_state.winner = winner
                else:
                    st.session_state.turn = 2 if st.session_state.turn == 1 else 1
        else:
            cols[j].markdown(f"<div class='stone'>{symbol}</div>", unsafe_allow_html=True)

# 게임 상태
if st.session_state.winner:
    winner = "흑(●)" if st.session_state.winner == 1 else "백(○)"
    st.success(f"🏆 {winner} 승리!")
    if st.button("🔄 게임 다시 시작"):
        reset_game()
else:
    turn = "흑(●)" if st.session_state.turn == 1 else "백(○)"
    st.info(f"🕹️ 현재 차례: {turn}")
