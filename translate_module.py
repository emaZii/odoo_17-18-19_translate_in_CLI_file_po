import os
import argparse
import odoo
from odoo.tools.translate import trans_export

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--db', required=True)
parser.add_argument('-m', '--module', required=True)
parser.add_argument('-p', '--path', required=True)
parser.add_argument('-l', '--lang', default='it_IT')
parser.add_argument('--db_port', default='5432')
parser.add_argument('--db_user', default='odoo')
parser.add_argument('--db_password', default='')
args = parser.parse_args()

addons_path = os.path.abspath(args.path)

odoo.tools.config['--addons-path'] = addons_path
odoo.tools.config['--db_password'] = args.db_password
odoo.tools.config['--db_port'] = args.db_port
odoo.tools.config['--db_user'] = args.db_user
    

registry = odoo.modules.registry.Registry.new(args.db)
    
i18n_path = os.path.join(addons_path, args.module, 'i18n')
    
if not os.path.exists(i18n_path):
    os.makedirs(i18n_path, exist_ok=True)
    print(f"Cartella creata: {i18n_path}")

if args.lang == 'en_US':
    filename = os.path.join(i18n_path, f"{args.module}.po")
    export_lang = True
    export_format = 'po'
elif args.lang == 'it_IT':
    filename = os.path.join(i18n_path, f"{args.module}.po")
    export_lang = True
    export_format = 'po'
else:
    filename = os.path.join(i18n_path, f"{args.lang}.po")
    export_lang = args.lang
    export_format = 'po'
    
with registry.cursor() as cr:
    with open(filename, 'wb') as f:
        trans_export(export_lang, [args.module], f, export_format, cr)
        print(f"File creato con successo: {filename}")
            
registry = odoo.modules.registry.Registry.delete(args.db)
