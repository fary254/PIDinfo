import psutil
import time
import os

def get_process_info(pid):
    p = psutil.Process(pid)
    memory_info = p.memory_info()
    gpu_memory = p.memory_info().vms
    memory_addr = hex(id(p))
    memfullinfo = p.memory_full_info()
    connections = p.connections()
    io_counters = p.io_counters()
    threads = p.num_threads()
    OPENFILES = p.open_files()
    status = p.status()
    terminal = p.terminal()
    return memory_info, gpu_memory, memory_addr, memfullinfo, connections, io_counters, threads, OPENFILES, status, terminal

def monitor_process(pid):
    try:
        while True:
            memory_info, gpu_memory, memory_addr, memfullinfo, connections, io_counters,threads, OPENFILES, status, terminal = get_process_info(pid)
            print(f"Process memory: {memory_info.rss} bytes")
            print(f"GPU memory: {gpu_memory} bytes")
            print(f"Memory address: {memory_addr}")
            print(f"status: {status}")
            print("                                 ")
            print(f"Memory full info: {memfullinfo}")
            print("                                 ")
            print(f"connections: {connections}")
            print("                                 ")
            print(f"io counters: {io_counters}")
            print(f"opened files: {OPENFILES}")
            print(f"threads: {threads}")
            print(f"terminal: {terminal}")

            time.sleep(1)
            os.system('clear')
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    pid = int(input("Enter the PID of the process to monitor: "))
    monitor_process(pid)
