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

from O365 import Account

# 替换为你的应用程序的客户端 ID 和客户端密钥
client_id = 'your_client_id'
client_secret = 'your_client_secret'

# 创建一个 O365 账户
credentials = (client_id, client_secret)
account = Account(credentials)

# 登录到账户
if not account.is_authenticated:
    # 如果没有授权，进行授权
    account.authenticate(scopes=['basic', 'message_all'])
    # 或者使用 account.authenticate(scopes=['basic', 'message_all', 'onedrive_all']) 来获取更多权限

# 创建一封新邮件
m = account.new_message()
m.to.add('to_example@example.com')  # 替换为你要发送的收件人邮箱地址
m.subject = '通关啦！'
m.body = "恭喜你，成功通关迷宫游戏！"
m.send()

print("通关消息已发送！")

