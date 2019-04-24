import subprocess


def reload_config():
    subprocess.Popen('/usr/local/nginx/sbin/nginx -s reload', shell=True)


def template():
    pass


def start():
    subprocess.Popen([
        '/usr/local/nginx/sbin/nginx',
        '-g',
        '"daemon off;"'],
        shell=True
        )
