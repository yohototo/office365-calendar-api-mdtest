# mdtest

- [a](#a)


 
## <a id="a"></a> 859款,ohhh,o,ohhhhgggfffrrr


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
```--updating  github居然不墙了？36ddggg66
