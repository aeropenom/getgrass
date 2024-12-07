import subprocess
import datetime

# Nama layanan proxy
SERVICE = "squid"

def restart_proxy():
    # Cek status layanan proxy
    try:
        status = subprocess.check_output(["systemctl", "is-active", "--quiet", SERVICE])
        print(f"{datetime.datetime.now()}: Proxy service is running.")
    except subprocess.CalledProcessError:
        # Jika proxy tidak aktif, restart
        print(f"{datetime.datetime.now()}: Proxy service is down, restarting...")
        subprocess.run(["sudo", "systemctl", "restart", SERVICE])
        print(f"{datetime.datetime.now()}: Proxy service restarted.")

if __name__ == "__main__":
    restart_proxy()
  
