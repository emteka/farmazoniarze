import autoit
import time

# CSGO: bot konczy na setpos -20.914536 -438.160706 -103.906189;setang 15.012780 178.671692 0.000000
# CS2:  bot konczy na setpos -24.977427 -438.112610 -104.580917;setang 15.106937 178.672028 0.000000

duration_ms = 800
steps = 200
delay = duration_ms / steps / 1000
# CSGO: sens 0.01
# CS2:  sens 0.83
move_distance_y = 800
press_left_after_ms = 1.5

time.sleep(3)
for _ in range(100):
    autoit.send("{W up}")
    autoit.send("{V down}")
    autoit.send("{V up}")
    time.sleep(0.2)

    autoit.send("{W down}")
    time.sleep(press_left_after_ms)
    autoit.mouse_down("left")
    x, y = autoit.mouse_get_pos()
    for i in range(steps):
        new_y = y + int((i + 1) * move_distance_y / steps)
        autoit.mouse_move(x, new_y, speed=0)
        time.sleep(delay)

    autoit.mouse_up("left")
    autoit.send("{W up}")
    time.sleep(1)
