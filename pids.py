import psutil
import os

def main2():
    try:
        # pidList = psutil.pids()
        pidList = ["apple", "banana", "cherry"]
        # print(pidList)
        for pid  in (pidList + 1):
            print(pid)
            # printPIFInfo(pid)
        # printPIFInfo(pid)

    except NameError:
        print(NameError)


def printPIFInfo(pid):
    try:
        p = psutil.Process(pid)
        print(p.name())
        print(p.exe())
        print(p.status())
        print(p.username())
        print(p.create_time())
        print(p.terminal())
        print(p.uids())
        print(p.gids())
        print(p.memory_full_info())
        print(p.cpu_times)
        print(p.io_counters())
        print(p.open_files())
        print(p.connections())
        print(p.threads())
        print(p.nice())
        p.suspend()
        p.resume()
        p.terminate()

    except BaseException:
        print(BaseException)

main2()
