import time
import webbrowser

total_breaks = 3
break_count = 0

print("This program startesd on " + time.ctime())

while(break_count < total_breaks):
    time.sleep(10)
    print("Time for a break")
    webbrowser.open_new_tab("https://www.google.com")
    break_count =  break_count + 1
