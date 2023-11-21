# 定义地图
map = [
    "#####",
    "#   #",
    "#   #",
    "#O  #",
    "#####"
]

# 定义玩家初始位置
player_x, player_y = 3, 1

# 定义箱子初始位置
box_x, box_y = 3, 2

# 游戏循环
while True:
    # 打印地图
    for row in map:
        print(row)

    # 玩家移动
    move = input("请输入移动方向（上：w，下：s，左：a，右：d）：")
    if move == "w":
        if map[player_y - 1][player_x] == " ":
            player_y -= 1
        elif map[player_y - 1][player_x] == "O" and map[player_y - 2][player_x] == " ":
            player_y -= 1
            box_y -= 1
    elif move == "s":
        if map[player_y + 1][player_x] == " ":
            player_y += 1
        elif map[player_y + 1][player_x] == "O" and map[player_y + 2][player_x] == " ":
            player_y += 1
            box_y += 1
    elif move == "a":
        if map[player_y][player_x - 1] == " ":
            player_x -= 1
        elif map[player_y][player_x - 1] == "O" and map[player_y][player_x - 2] == " ":
            player_x -= 1
            box_x -= 1
    elif move == "d":
        if map[player_y][player_x + 1] == " ":
            player_x += 1
        elif map[player_y][player_x + 1] == "O" and map[player_y][player_x + 2] == " ":
            player_x += 1
            box_x += 1

    # 更新地图
    map[box_y] = map[box_y][:box_x] + "O" + map[box_y][box_x + 1:]
    map[player_y] = map[player_y][:player_x] + "P" + map[player_y][player_x + 1:]

    # 判断是否胜利
    if map[box_y][box_x] == "X":
        print("恭喜你，通关了！")
        break
