import os
import argparse
import odoo
from odoo.tools.translate import trans_export

def run_export():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--db', required=True)
    parser.add_argument('-m', '--module', required=True)
    parser.add_argument('-p', '--path', required=True)
    parser.add_argument('-l', '--lang', default='it_IT')
    parser.add_argument('--db_host', default='localhost')
    parser.add_argument('--db_port', default='5423')
    parser.add_argument('--db_user', default='odoo')
    parser.add_argument('--db_password', default='myodoo')
    args = parser.parse_args()

    odoo.tools.config['addons_path'] = args.path
    odoo.tools.config['db_host'] = args.db_host
    odoo.tools.config['db_port'] = int(args.db_port)
    odoo.tools.config['db_user'] = args.db_user
    odoo.tools.config['db_password'] = args.db_password

    registry = odoo.modules.registry.Registry.new(args.db)

    # Crea il percorso automatico: ./nome_modulo/i18n/
    module_path = os.path.join(args.path, args.module)
    i18n_path = os.path.join(module_path, 'i18n')
    
    if not os.path.exists(i18n_path):
        os.makedirs(i18n_path)
        print(f"Cartella creata: {i18n_path}")

    filename = os.path.join(i18n_path, f"{args.lang}.po")

    with registry.cursor() as cr:
        with open(filename, 'wb') as f:
            trans_export(args.lang, [args.module], f, 'po', cr)
            print(f"File generato con successo in: {filename}")

if __name__ == "__main__":
    run_export()
