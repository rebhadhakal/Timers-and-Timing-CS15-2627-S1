import time
baseline=0
for attempt in range(1, 6):
    timer_length =2
    start_time =time.monotonic()
    while True:
        current_time = time.monotonic()
        elapsed_time = current_time-start_time
        if elapsed_time >=timer_length:
            break
    go_time =time.monotonic()
    input("Go!")
    button_time = time.monotonic()
    reaction_time = button_time-go_time
    print("Reaction time:", reaction_time, "seconds")
    if attempt==1:
        baseline=reaction_time
    elif reaction_time<baseline:
        baseline=reaction_time
print("Fastest reaction time:",baseline, "seconds")