import subprocess
import time
import os
import sys

# 指定输出文件路径
output_dir = "memory_profiles"
os.environ["PPROF_TMPDIR"] = output_dir
os.makedirs(output_dir, exist_ok=True)


def capture_memory_profile(pprof_address):
    # 使用subprocess执行go tool pprof命令来采集内存信息
    command = f"go tool pprof -proto {pprof_address}"
    subprocess.run(command, shell=True, check=True)


if __name__ == "__main__":
    # 采集内存信息的间隔时间（秒）
    # capture_interval = 60 * 60 * 12  # 每12小时采集一次，你可以根据需要进行调整
    # e.g python memory_profiler.py http://127.0.0.1:8080/debug/pprof/allocs\?debug\=1
    # 上面的地址可以换成pod的ip和端口
    capture_interval = 60  # 每60秒采集一次，你可以根据需要进行调整

    print("Starting memory profiler")

    if len(sys.argv) != 2:
        print("Usage: python memory_profiler.py <pprof_address>")
        sys.exit(1)

    pprof_address = sys.argv[1]
    print(f"Capturing memory profile every {capture_interval} seconds to {output_dir}")

    while True:
        try:
            capture_memory_profile(pprof_address)
        except Exception as e:
            print(f"Error capturing memory profile: {str(e)}")

        time.sleep(capture_interval)
