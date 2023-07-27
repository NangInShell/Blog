import pyautogui
import keyboard

with open('mouse_positions.txt', 'w') as file:
    while True:
        if keyboard.is_pressed('s'):
            print('You Pressed A Key!')
            x, y = pyautogui.position()
            print(f"鼠标点击后的位置：X={x}, Y={y}")
            file.write(f"{x}, {y}\n")
            pyautogui.sleep(1)
        elif keyboard.is_pressed('q'):
            print('退出')
            break
        else:
            n=1
