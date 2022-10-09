'''
필요한 정보만 출력하기
'''

import psutil

# cpu 속도
cpu = psutil.cpu_freq()
cpu_current_ghz = round( cpu.current / 1000, 2 )
print( f"cpu 속도: {cpu_current_ghz}Ghz" )

# cpu 물리코어 수
cpu_core = psutil.cpu_count( logical=False )
print( f"코어: {cpu_core} 개" )

# 메모리 정보
memory = psutil.virtual_memory()
memory_total = round( memory.total / 1024**3 ) # 1024**3이 GB인가벼
print( f"메모리: {memory_total}GB" )

# 디스크 정보
disk = psutil.disk_partitions()
# 디스크는 여러 개가 있을 수 있으므로 찾은 수만큼 반복
for p in disk:
    print( p.mountpoint, p.fstype, end=" " )
    du = psutil.disk_usage( p.mountpoint )
    disk_total = round( du.total / 1024**3 )
    print( f"디스크 크기: {disk_total}GB" )
    

# 네트워크를 통해 보내고 받은 데이터량을 MB 단위로 출력
net = psutil.net_io_counters()
sent = round( net.bytes_sent / 1024**2, 1 )
recv = round( net.bytes_recv / 1024**2, 1 )
print( f"보내기: {sent}MB 받기: {recv}MB" )