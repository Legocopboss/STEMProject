def clear_frame(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()
