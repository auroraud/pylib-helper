import psutil
import time

# most simple code here.


# obtain all modules, can be used for hella things.
# the modules refresh
def get_modules_from_process(target_executable):
    while True:
        for process in psutil.process_iter(['pid', 'name', 'memory_info', 'exe']):
            if process.info['exe'] and target_executable in process.info['exe']:
                print(f"Modules for {target_executable} (PID {process.info['pid']}):")
                try:
                    process_info = process.memory_info()
                    for module in psutil.Process(process.info['pid']).memory_maps(grouped=True):
                        print(f"  {module}")
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    print(f"Error accessing information for PID {process.info['pid']}")
        time.sleep(5)  

if __name__ == "__main__":
    target_executable = "Windows10Universal.exe"
    get_modules_from_process(target_executable)
