""" open edge, search chat.com in very the top searchbar, 
do a research about the history of morocco, wait until the chatbot fully respond, 
select the full answer you get and copy it, open word, click on blank document, then paste it in
"""
from utils.agent import create_clevrr_agent
from utils.prompt import prompt
from utils.contants import *

import time

import pyautogui as pg

pg.PAUSE = 2

import argparse
from tkinter import *


def main():
    # Initialize the argument parser
    parser = argparse.ArgumentParser(description="Launch the application with optional model and UI settings.")
    
    # Add arguments
    parser.add_argument('--model', type=str, default='gemini', choices=['openai', 'gemini'],
                        help="Choose the model to use. Default is 'gemini'. Options: 'openai', 'gemini'.")
    parser.add_argument('--float-ui', type=int, default=1, choices=[0, 1],
                        help="Enable or disable the float UI. Default is 1 (enabled). Pass 0 to disable.")
    
    # Parse the arguments
    args = parser.parse_args()

    # Convert float-ui argument to boolean
    float_ui = bool(args.float_ui)

    # Print out the configurations
    print(f"Using model: {args.model}")
    print(f"Float UI is {'enabled' if float_ui else 'disabled'}")

    # Create the agent executor
    agent_executor = create_clevrr_agent(MODELS[args.model], prompt)

    # Initialize the GUI
    root = Tk()
    root.title("Novaa Computer")
    
    # Set the window size to fill the whole screen vertically and 20% horizontally
    """screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = int(screen_width * 0.3)
    window_height = screen_height - 150
    root.geometry(f"{window_width}x{window_height}")"""

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = int(screen_width * 0.2)  # 20% of the screen width
    window_height = int(screen_height * 0.3)  # 60% of the screen height
    root.geometry(f"{window_width}x{window_height}")

    # Define the send function
    def send():
        # pg.hotkey("alt", "tab")
        user_input = e.get().lower()
        txt.insert(END, f"\nYou -> {user_input}")
        time.sleep(1.5)
        response = agent_executor.invoke({"input": user_input})
        txt.insert(END, f"\nBot -> {response.get('output')}")

        e.delete(0, END)
    
    
    # --- Inside main(), after creating root ---

    # Configure the main window’s grid so row=1 (the text area) expands
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # 1) Top label (row=0)
    label_title = Label(
        root, 
        bg=BG_COLOR, 
        fg=TEXT_COLOR, 
        text="First version of novaa Computer", 
        font=FONT_BOLD, 
        pady=10, 
        width=30, 
        height=2
    )
    label_title.grid(row=0, column=0, columnspan=2, sticky="nsew")

    # 2) Text area + scrollbar (row=1)
    txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT)
    txt.grid(row=1, column=0, columnspan=1, sticky="nsew")

    scrollbar = Scrollbar(root, command=txt.yview)
    scrollbar.grid(row=1, column=1, sticky="ns")  # put the scrollbar to the right of the text
    txt.configure(yscrollcommand=scrollbar.set)

    # 3) Bottom frame for entry + button (row=2)
    frame_bottom = Frame(root)
    frame_bottom.grid(row=2, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

    # Let the entry expand in this frame
    frame_bottom.grid_columnconfigure(0, weight=1)

    # Entry widget
    e = Entry(frame_bottom, bg="#FCFCFC", fg=TEXT_COLOR, font=FONT)
    e.grid(row=0, column=0, sticky="ew", padx=(0, 5))

    # Send button
    btn_send = Button(frame_bottom, text="Send", font=FONT_BOLD, bg=BG_GRAY, command=send)
    btn_send.grid(row=0, column=1, sticky="ew")

    
    
    
    
    
    
    """ # Set up the GUI components
    Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="First version of novaa Computer", font=FONT_BOLD, pady=10, width=30, height=2).grid(row=0)
    
    txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=40, height=15)
    txt.grid(row=1, column=0, columnspan=2)
    
    scrollbar = Scrollbar(txt)
    scrollbar.place(relheight=1, relx=0.974) """

    # Modify the Entry and Button layout
    """ frame = Frame(root)
    frame.grid(row=2, column=0, columnspan=2, pady=5, padx=5, sticky="ew")

    e = Entry(frame, bg="#FCFCFC", fg=TEXT_COLOR, font=FONT)
    e.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 5))  # Added padding on the right

    Button(frame, text="Send", font=FONT_BOLD, bg=BG_GRAY, command=send).pack(side=RIGHT, fill=Y) """


    """ # Modify the Entry and Button layout
    frame = Frame(root)
    frame.grid(row=2, column=0, columnspan=2, pady=5, padx=5, sticky="ew")

    e = Entry(frame, bg="#FCFCFC", fg=TEXT_COLOR, font=FONT)
    e.pack(side=LEFT, fill=BOTH, expand=True)

    Button(frame, text="Send", font=FONT_BOLD, bg=BG_GRAY, command=send, width=8).pack(side=RIGHT) """

    
    """ e = Entry(root, bg="#FCFCFC", fg=TEXT_COLOR, font=FONT, width=10)
    e.grid(row=2, column=0)
    
    Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY, command=send).grid(row=2, column=0)
    Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY, command=send, width=8)\
    .grid(row=2, column=1, sticky="ew", padx=5, pady=5) """

    # Set window attributes and start the main loop
    root.attributes('-topmost', float_ui)
    root.mainloop()

if __name__ == "__main__":
    main()
