import requests

# 从 config.py 文件中获取访问令牌
from config import O365_ACCESS_TOKEN, ONEDRIVE_ACCESS_TOKEN

# Office 365 Calendar API Endpoint
calendar_api_url = 'https://graph.microsoft.com/v1.0/me/events'

# 设置请求头部
headers = {
    'Authorization': 'Bearer ' + O365_ACCESS_TOKEN,
    'Content-Type': 'application/json'
}

# 创建日历事件
new_event = {
    'subject': '会议',
    'start': {
        'dateTime': '2024-01-06T12:00:00',
        'timeZone': 'Pacific Standard Time'
    },
    'end': {
        'dateTime': '2024-01-06T13:00:00',
        'timeZone': 'Pacific Standard Time'
    }
}

# 发送创建日历事件的请求
response = requests.post(calendar_api_url, headers=headers, json=new_event)

if response.status_code == 201:
    print('成功创建日历事件:', response.json())
else:
    print('无法创建日历事件:', response.text)

# 使用 OneDrive API Endpoint 读取笔记本内容
onedrive_url = 'https://graph.microsoft.com/v1.0/me/drive/root/children'
headers['Authorization'] = 'Bearer ' + ONEDRIVE_ACCESS_TOKEN

# 获取 OneDrive 中的文件和文件夹列表
onedrive_response = requests.get(onedrive_url, headers=headers)

if onedrive_response.status_code == 200:
    items = onedrive_response.json()['value']
    if items:
        for item in items:
            print('文件名:', item['name'], ' | 类型:', item['folder'] if 'folder' in item else '文件')
    else:
        print('OneDrive 中没有文件或文件夹')
else:
    print('无法获取 OneDrive 文件列表:', onedrive_response.text)

<Configuration>
    <Add SourcePath="\\Server\Share" OfficeClientEdition="64" Channel="MonthlyEnterprise">
        <Product ID="O365ProPlusRetail">
            <Language ID="en-us" />
            <Language ID="ja-jp" />
        </Product>
        <Product ID="VisioProRetail">
            <Language ID="en-us" />
            <Language ID="ja-jp" />
        </Product>
    </Add>
    <Updates Enabled="TRUE" UpdatePath="\\Server\Share" />
    <Display Level="None" AcceptEULA="TRUE" />
</Configuration>

