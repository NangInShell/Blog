import pyautogui

# 从txt文件中读取鼠标点击位置
def read_mouse_positions(file_path):
    positions = []
    with open(file_path, 'r') as file:
        for line in file:
            print(line)
            x, y = line.strip().split(',')
            positions.append((x, y))
    return positions

# 等待一段时间，确保你的焦点在需要操作的应用程序上
pyautogui.sleep(1)

# txt文件的路径
file_path = 'mouse_positions.txt'

# 读取鼠标点击位置
positions = read_mouse_positions(file_path)

# 逐个操作鼠标点击
for x, y in positions:
    pyautogui.click(int(x),int(y))
    print(x,y)
    # 可选：添加延时，等待一段时间再进行下一次点击
    # pyautogui.sleep(0.1)  # 1秒的延时，你可以根据需要调整时间
