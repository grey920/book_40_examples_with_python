'''
컴퓨터 정보 확인 코드 만들기
cpu 속도, 물리 코어수, 메모리, 디스크, 네트워크 정보를 확인한다
'''

import psutil

# cpu 속도
cpu = psutil.cpu_freq()
print( "cpu: ", cpu )

# cpu 물리코어 수
cpu_core = psutil.cpu_count( logical=False )
print( "cpu_core: ", cpu_core )

# 메모리 정보
memory = psutil.virtual_memory()
print( "memory: ", memory )

# 디스크 정보
disk = psutil.disk_partitions()
print( "disk: ", disk )

# 네트워크를 통해 보내고 받은 데이터량을 출력
net = psutil.net_io_counters()
print( "net: ", net )