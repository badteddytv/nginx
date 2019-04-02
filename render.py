from jinja2 import Environment, FileSystemLoader


def render(data):
    file_loader = FileSystemLoader('.')
    env = Environment(loader=file_loader)
    template = env.get_template('nginx.conf.jinja')
    output = template.render(data=data)
    return output

def save(output):
    print(output)
    file = '/usr/local/nginx/conf/nginx.conf'
    with open(file, 'w') as filetowrite:
        filetowrite.write(output)
        filetowrite.close()

def render_and_save(data):
    output = render(data)
    save(output)
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

#provide a function to template the redis value (service_host_port) and map to a file
