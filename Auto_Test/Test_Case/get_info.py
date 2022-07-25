
import psutil

def Get_sys_info():


    # cpu信息
    cpu = str(psutil.cpu_percent(interval=1)) + '%'
    # cpu = psutil.cpu_percent(interval=1, percpu=True)

    # 内存信息
    mem = psutil.virtual_memory()
    mem_total = round(mem.total / 1024 / 1024 / 1024, 0)
    mem_free = round(mem.free / 1024 / 1024 / 1024)
    mem_percent = str(mem.percent) + '%'
    mem_used = round(mem.used / 1024 / 1024 / 1024)

    # 磁盘信息(磁盘空间使用占比)
    disk1 = str(psutil.disk_usage('C:/').percent) + '%'
    disk2 = str(psutil.disk_usage('D:/').percent) + '%'

    return mem_free,mem_total,mem_percent,mem_used,cpu,disk1,disk2

if __name__ == "__main__":

    def job():
        mem_free, mem_total, mem_percent, mem_used, cpu, disk1, disk2 = Get_sys_info()
        now_time = datetime.now()
        list1 = [now_time, mem_free, mem_total, mem_percent, mem_used, cpu, disk1, disk2]
        tuple_list = tuple([str(i) for i in list1])
        print(tuple_list)