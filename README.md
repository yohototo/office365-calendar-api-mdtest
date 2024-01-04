# mdtest

- [a](#a)


 
## <a id="a"></a>  考虑考其味无穷


```
import psutil

def get_hardware_info():
    # 获取CPU信息
    cpu_info = f"CPU使用率: {psutil.cpu_percent()}%"
    
    # 获取内存信息
    mem = psutil.virtual_memory()
    total_memory = round(mem.total / (1024 * 1024 * 1024), 2)  # 总内存，转换为GB
    used_memory = round(mem.used / (1024 * 1024 * 1024), 2)    # 已使用内存，转换为GB
    memory_info = f"总内存: {total_memory}GB，已使用内存: {used_memory}GB"
    
    # 获取磁盘信息
    disk = psutil.disk_usage('/')
    total_disk = round(disk.total / (1024 * 1024 * 1024), 2)   # 总磁盘空间，转换为GB
    used_disk = round(disk.used / (1024 * 1024 * 1024), 2)     # 已使用磁盘空间，转换为GB
    disk_info = f"总磁盘空间: {total_disk}GB，已使用磁盘空间: {used_disk}GB"
    
    # 打印硬件信息
    print("VPS硬件信息:")
    print(cpu_info)
    print(memory_info)
    print(disk_info)

# 获取并打印硬件信息
get_hardware_info()
```--updating  gitazhu

// SharePoint 网站的 URL
var siteUrl = "https://your-sharepoint-site-url";

// 获取当前时间的函数
function getCurrentDateTime() {
    var now = new Date();
    return now.toISOString(); // 返回当前时间的 ISO 格式字符串
}

// 向 SharePoint 列表中添加项目，并自动记录创建时间戳
function addNewItem() {
    var listTitle = "SampleList";
    var endpointUrl = siteUrl + `/_api/web/lists/getbytitle('${listTitle}')/items`;

    var currentTime = getCurrentDateTime();

    var itemData = {
        '__metadata': { 'type': 'SP.Data.SampleListListItem' }, // 替换为列表项的类型
        'Title': 'New Item',
        'Description': 'This is a new item.',
        'CreatedTimestamp': currentTime // 假设 SharePoint 列表中有名为 CreatedTimestamp 的字段用于记录创建时间戳
        // 根据列表的字段结构添加其他必要的字段
    };

    var accessToken = getAccessToken();

    fetch(endpointUrl, {
        method: 'POST',
        headers: {
            'Accept': 'application/json;odata=verbose',
            'Content-Type': 'application/json;odata=verbose',
            'Authorization': 'Bearer ' + accessToken
        },
        body: JSON.stringify(itemData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('项目已添加到列表，创建时间戳记录成功:', data);
        // 添加成功后的操作
    })
    .catch(error => {
        console.error('添加项目时出错:', error);
    });
}

// 更新 SharePoint 列表中的项目，并自动记录最后修改时间戳
function updateItem(itemId) {
    var listTitle = "SampleList";
    var endpointUrl = siteUrl + `/_api/web/lists/getbytitle('${listTitle}')/items(${itemId})`;

    var currentTime = getCurrentDateTime();

    var itemData = {
        '__metadata': { 'type': 'SP.Data.SampleListListItem' }, // 替换为列表项的类型
        'LastModifiedTimestamp': currentTime // 假设 SharePoint 列表中有名为 LastModifiedTimestamp 的字段用于记录最后修改时间戳
        // 根据需要更新其他字段
    };

    var accessToken = getAccessToken();

    fetch(endpointUrl, {
        method: 'POST',
        headers: {
            'Accept': 'application/json;odata=verbose',
            'Content-Type': 'application/json;odata=verbose',
            'Authorization': 'Bearer ' + accessToken,
            'X-HTTP-Method': 'MERGE',
            'If-Match': '*'
        },
        body: JSON.stringify(itemData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('项目已更新，最后修改时间戳记录成功:', data);
        // 更新成功后的操作
    })
    .catch(error => {
        console.error('更新项目时出错:', error);
    });
}

// 调用函数来添加新项目并模拟更新项目的最后修改时间戳（根据需要选择执行）
addNewItem(); // 添加新项目
// updateItem(itemId); // 更新项目，需要提供相应的项目 ID

```
