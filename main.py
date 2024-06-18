import tkinter as tk
from home_frame_module import HomeFrame
from login_frame_module import LoginFrame
from menu_frame_module import MenuFrame

# 우측 frame의 frame 교체 함수
def view_other_frame(frame_to_show):
    for frame in right_frames:
        frame.place_forget()

    frame_to_show.place(relx=0.2, rely=0.05, relwidth=0.8, relheight=0.95)

# username 을 바꾸는 함수, login_frame에서 사용한다, LoginFrame을 생성할 때 함수포인터 전달
def update_username(new_username):
    global username
    username = new_username
    label_user.config(text=f"Username: {username}")

# 윈도우 생성 및 크기 지정
win = tk.Tk()
win.geometry("800x600")

# login user의 이름을 위한 변수
username = "guest"  

# 현재 로그인 사용자를 표시하는 frame
username_frame = tk.Frame(win, height=30, bg="lightgray")
username_frame.pack(fill="x")
label_user = tk.Label(username_frame, text=f"Username: {username}")
label_user.pack(side="left", padx=10)

# 필요한 frame을 생성
home_frame = HomeFrame(win, relief="solid", bd=2)
home_frame.place(relx=0.2, rely=0.05, relwidth=0.8, relheight=0.95)  

login_frame = LoginFrame(win, update_username, relief="solid", bd=2)

# 우측 에 필요한 frame들의 list
right_frames = [home_frame, login_frame]

# MenuFrame(좌측) 생성에 변수로 들어갈 list.  "Button text" : frame name  의 구조 
frame_list = {
    "Home": home_frame,
    "Login": login_frame,
}

# MenuFrame 생성
menu_frame = MenuFrame(win, view_other_frame, frame_list, relief="solid", bd=2)
menu_frame.place(rely=0.05, relwidth=0.2, relheight=0.95)  

# 윈도우 시작
win.mainloop()

