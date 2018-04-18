import time
import webbrowser

total_breaks = 3
break_count = 0

print("This program has started on "+time.ctime())
while(break_count < total_breaks):
    time.sleep(40*60)
    webbrowser.open("https://www.youtube.com/watch?v=fJ9rUzIMcZQ")
    break_count = break_count + 1
