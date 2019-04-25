from jinja2 import Environment, FileSystemLoader


def render(data, directory='.'):
    file_loader = FileSystemLoader(directory)
    env = Environment(loader=file_loader)
    template = env.get_template('nginx.conf.jinja')
    output = template.render(data=data)
    return output


def save(output, directory='.'):
    file = '/usr/local/nginx/conf/{}/nginx.conf'.format(directory)
    with open(file, 'w') as filetowrite:
        filetowrite.write(output)
        filetowrite.close()


def render_and_save(data):
    http_output = render(data, 'http_templates')
    rtmp_output = render(data, 'rtmp_templates')

    save(http_output, 'http_servers')
    save(rtmp_output, 'rtmp_servers')


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
