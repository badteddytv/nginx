import time
import subprocess

subprocess.Popen([
            '/usr/local/nginx/sbin/nginx',
            '-g',
            '"daemon off;"'],
            shell=True
            )

while True:
    print('reloading')
    subprocess.Popen(
            '/usr/local/nginx/sbin/nginx -s reload -g "daemon off;"',
            shell=True)
    time.sleep(3)
