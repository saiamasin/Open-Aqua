import threading
import subprocess
from time import sleep

def run_script(script_name):
    subprocess.run(["python", script_name])
    

if __name__ == "__main__":
    script1_thread = threading.Thread(target=run_script, args=("relay_temp_switch.py",))
    script2_thread = threading.Thread(target=run_script, args=("temp_to_txtfile.py",))
    script3_thread = threading.Thread(target=run_script, args=("video_feed.py",))
    script4_thread = threading.Thread(target=run_script, args=("relay_light_switch.py",))

    script1_thread.start()
    script2_thread.start()
    script3_thread.start()
    script4_thread.start()

    script1_thread.join()
    script2_thread.join()
    script3_thread.join()
    script4_thread.join()

    print("All scripts have finished executing.")
