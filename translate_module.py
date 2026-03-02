import os
import argparse
import odoo
from odoo import api, SUPERUSER_ID
from odoo.modules.registry import Registry
from odoo.tools.translate import trans_export, TranslationModuleReader

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

if addons_path not in odoo.addons.__path__:
    odoo.addons.__path__.append(addons_path)

try:
    odoo.tools.config.parse([
        '--addons-path=' + addons_path,
        '--db_port=' + args.db_port,
        '--db_user=' + args.db_user,
        '--db_password=' + args.db_password,
    ])
except TypeError:
    odoo.tools.config['addons_path'] = addons_path
    odoo.tools.config['db_host'] = '127.0.0.1'
    odoo.tools.config['db_port'] = int(args.db_port)
    odoo.tools.config['db_user'] = args.db_user
    odoo.tools.config['db_password'] = args.db_password

registry = Registry.new(args.db)

i18n_path = os.path.join(addons_path, args.module, 'i18n')

if not os.path.exists(i18n_path):
    os.makedirs(i18n_path, exist_ok=True)
    print(f"Cartella creata: {i18n_path}")

if args.lang == 'en_US':
    filename = os.path.join(i18n_path, f"{args.module}.pot")
    export_lang = False
    export_format = 'pot'
else:
    filename = os.path.join(i18n_path, f"{args.lang}.po")
    export_lang = args.lang
    export_format = 'po'

with registry.cursor() as cr:
    env = api.Environment(cr, SUPERUSER_ID, {})
    reader_lang = TranslationModuleReader(cr, modules=[args.module], lang=export_lang)
    with open(filename, 'wb') as f:
        trans_export(export_lang, [args.module], f, export_format, env)
        print(f"File creato con successo: {filename}")

odoo.modules.registry.Registry.delete(args.db)
