#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            port=dict(type='int', required=True),
            dest=dict(type='str', required=True)
        )
    )
    port = module.params['port']
    dest = module.params['dest']

    content = f"""server {{
    listen {port};
    root /var/www/localhost/htdocs;
    index index.html;
    location /files {{
        alias /var/www/files/;
        autoindex on;
    }}
}}"""
    try:
        with open(dest, 'w') as f:
            f.write(content)
        module.exit_json(changed=True)
    except Exception as e:
        module.fail_json(msg=str(e))

if __name__ == '__main__':
    main()
