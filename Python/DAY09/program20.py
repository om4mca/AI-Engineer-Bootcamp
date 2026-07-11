#--------------------------------------------
# AI Engineer Bootcamp
# Day 8
# Program: Digital Clock
# Author: Om Roy
# Date: 11-07-2026
#--------------------------------------------


import sys
import time
import tkinter as tk


class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("System Clock")
        self.root.geometry("420x150")
        self.root.resizable(False, False)
        
        # Configure matching dark mode theme palette
        self.bg_color = "#1e1e2e"       # Deep slate blue
        self.text_color = "#cdd6f4"     # Soft crisp white
        self.accent_color = "#f5c2e7"   # Calm pink highlights
        
        self.root.configure(bg=self.bg_color)
        
        # Top Header Container Frame
        self.header_frame = tk.Frame(self.root, bg=self.bg_color)
        self.header_frame.pack(fill="x", pady=(10, 0))
        
        # Mode indicator display label
        self.mode_label = tk.Label(
            self.header_frame, 
            text="LIVE SYSTEM TIME", 
            font=("Helvetica", 10, "bold"), 
            bg=self.bg_color, 
            fg=self.accent_color
        )
        self.mode_label.pack()
        
        # Primary Time Display text label
        self.time_label = tk.Label(
            self.root, 
            text="", 
            font=("Consolas", 44, "bold"), 
            bg=self.bg_color, 
            fg=self.text_color
        )
        self.time_label.pack(expand=True)
        
        # Secondary Date Display label below time element
        self.date_label = tk.Label(
            self.root, 
            text="", 
            font=("Helvetica", 12), 
            bg=self.bg_color, 
            fg=self.accent_color
        )
        self.date_label.pack(pady=(0, 15))
        
        # Start the continuous event updating cycle loop
        self.update_clock_ticks()

    def update_clock_ticks(self):
        """Fetches latest system time updates and maps them onto window objects."""
        # Get localized time configurations
        current_time_str = time.strftime("%I:%M:%S %p")  # 12-Hour layout with AM/PM
        current_date_str = time.strftime("%A • %B %d, %Y") # Full calendar textual layout
        
        # Bind string text updates to active UI labels
        self.time_label.config(text=current_time_str)
        self.date_label.config(text=current_date_str)
        
        # Schedule the next tick execution pass in exactly 200 milliseconds
        # Low latency intervals ensure accurate second transitions
        self.root.after(200, self.update_clock_ticks)


def main():
    # Instantiate native window environments safely across execution shells
    root = tk.Tk()
    app = DigitalClock(root)
    
    try:
        root.mainloop()
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    main()