"""
open edge, search chat.com in very the top searchbar, do a research about the history of morocco, 
wait until the chatbot fully respond, with the mouse select with the full answer you get and copy it, open word, click on blank document, then paste it in

open edge, search chat.com in very the top searchbar, do a research about the history of morocco, select the whole answer you get and copy it, open word, click on blank document, then paste it in

open edge, type chat.com in the small searchbar at the very top, do a research about the history of morocco, 
wait until the chatbot fully respond, with the mouse select with the full answer you get and copy it, open word, click on blank document, then paste it in

open edge, type chat.com in the small searchbar at the very top, do a research about the history of morocco, 
wait until the chatbot fully respond, with the mouse select with the full answer you get and copy it, open word, click on blank document, then paste it in

python main.py --model openai
"""

import tkinter as tk
from tkinter import ttk
from utils.agent import create_clevrr_agent
from utils.prompt import prompt
from utils.contants import *
import time

# color palettechat.com
BG_COLOR = "#F0F4F8"  
TEXT_COLOR = "#2C3E50"  
ACCENT_COLOR = "#3498DB"  
BUTTON_COLOR = "#2980B9"  
BUTTON_TEXT_COLOR = "white"

# fonts
TITLE_FONT = ("Segoe UI", 16, "bold")
BODY_FONT = ("Segoe UI", 10)
BUTTON_FONT = ("Segoe UI", 10, "bold")

def main():
    # i'm creating the agent executor
    agent_executor = create_clevrr_agent(MODELS['gemini'], prompt)
    
    root = tk.Tk()
    root.title("Novaa Computer")
    root.configure(bg=BG_COLOR)

    # setting modern, responsive window size
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = int(screen_width * 0.15)
    window_height = int(screen_height * 0.2)
    root.geometry(f"{window_width}x{window_height}")
    root.minsize(100, 300)  # Minimum window size

    # configuring grid
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # title label
    label_title = tk.Label(
        root, 
        text="Novaa version zero", 
        font=TITLE_FONT, 
        bg=BG_COLOR, 
        fg=TEXT_COLOR,
        padx=15,
        pady=10
    )
    label_title.grid(row=0, column=0, sticky="ew")

    # Text area with improved scrollbar and styling
    text_frame = tk.Frame(root, bg=BG_COLOR)
    text_frame.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
    text_frame.grid_columnconfigure(0, weight=1)
    text_frame.grid_rowconfigure(0, weight=1)

    txt = tk.Text(
        text_frame, 
        bg="white", 
        fg=TEXT_COLOR, 
        font=BODY_FONT,
        borderwidth=1,
        relief="solid",
        padx=10,
        pady=10
    )
    txt.grid(row=0, column=0, sticky="nsew")

    scrollbar = ttk.Scrollbar(text_frame, command=txt.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")
    txt.configure(yscrollcommand=scrollbar.set)

    # Bottom frame with modern entry and button
    bottom_frame = tk.Frame(root, bg=BG_COLOR)
    bottom_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
    bottom_frame.grid_columnconfigure(0, weight=1)

    e = tk.Entry(
        bottom_frame, 
        bg="white", 
        fg=TEXT_COLOR, 
        font=BODY_FONT,
        borderwidth=1,
        relief="solid",
        highlightthickness=1,
        highlightcolor=ACCENT_COLOR
    )
    e.grid(row=0, column=0, sticky="ew", padx=(0, 10))

    def send():
        user_input = e.get().lower()
        txt.insert(tk.END, f"\nYou -> {user_input}")
        txt.see(tk.END)  # Auto-scroll to the bottom
        time.sleep(1.5)
        response = agent_executor.invoke({"input": user_input})
        txt.insert(tk.END, f"\nBot -> {response.get('output')}")
        txt.see(tk.END)  # Auto-scroll to the bottom
        e.delete(0, tk.END)

    def on_enter_pressed(event):
        send()

    # Styled button with hover effect and send functionality
    btn_send = tk.Button(
        bottom_frame, 
        text="Send", 
        font=BUTTON_FONT, 
        bg=BUTTON_COLOR, 
        fg=BUTTON_TEXT_COLOR,
        activebackground="#2C3E50",
        relief="flat",
        padx=15,
        command=send
    )
    btn_send.grid(row=0, column=1, sticky="ew")

    # Bind Enter key to send
    e.bind('<Return>', on_enter_pressed)

    # Optional: Add hover effects
    def on_enter(e):
        e.widget['background'] = '#2C3E50'

    def on_leave(e):
        e.widget['background'] = BUTTON_COLOR

    btn_send.bind("<Enter>", on_enter)
    btn_send.bind("<Leave>", on_leave)

    # Make window float on top if needed
    root.attributes('-topmost', True)
    
    root.mainloop()

if __name__ == "__main__":
    main()