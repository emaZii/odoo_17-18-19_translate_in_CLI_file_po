import sys
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
    args = parser.parse_args()

    odoo.tools.config.parse(['--addons-path=' + args.path])
    registry = odoo.modules.registry.Registry.new(args.db)
    
    i18n_path = os.path.join(args.path, args.module, 'i18n')
    
    if not os.path.exists(i18n_path):
        os.mkdir(i18n_path)
        print(i18n_path)
        
    filename = os.path.join(i18n_path, f"{args.lang}.po")
    
    with registry.cursor() as cr:
        with open(filename, 'wb') as f:
            trans_export(args.lang, [args.module], f, 'po', cr)
            print(f"File creato con successo: {filename}")

if __name__ == "__main__":
    run_export()
