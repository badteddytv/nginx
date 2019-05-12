from jinja2 import Environment, FileSystemLoader
from jinja2.exceptions import TemplateNotFound
from logger import log


def render(data, filename):
    file_loader = FileSystemLoader('.')
    env = Environment(loader=file_loader)
    template = env.get_template(filename)
    output = template.render(data=data)
    return output


def save(output, directory='.'):
    file = '/usr/local/nginx/conf/{}/nginx.conf'.format(directory)
    with open(file, 'w') as filetowrite:
        filetowrite.write(output)
        filetowrite.close()


def render_and_save(data):
    try:
        http_output = render(data, 'http.nginx.conf.jinja')
        save(http_output, 'http_servers')
    except TemplateNotFound:
        log.info('no http template supplied')

    try:
        rtmp_output = render(data, 'rtmp.nginx.conf.jinja')
        save(rtmp_output, 'rtmp_servers')
    except TemplateNotFound:
        log.info('no rtmp template supplied')


if __name__ == '__main__':
    data = {'api':
            [
                {
                    'host': 'boobs',
                    'port': 6969
                },
                {
                    'host': 'bbss',
                    'port': 324
                }

            ],
            'web':
            [
                {
                    'host': 'boobs',
                    'port': 6969
                },
                {
                    'host': 'bbss',
                    'port': 324
                }

            ]
            }
    render_and_save(data)
