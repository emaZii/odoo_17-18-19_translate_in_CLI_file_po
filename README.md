bash
'''
 python3 translate_module.py -d lab18 -m academy_system -p . --db_port 5423 --db_user odoo --db_password myodoo
'''

### Cosa fa questo comando :
- python3 translate_module.py: lancia il tuo script di traduzione.
- -d lab18: dice a Odoo di estrarre i termini dal database chiamato lab18.
- -m academy_system: specifica il modulo di cui vuoi generare le traduzioni.
- -p .: indica che il modulo si trova nella cartella corrente.
- --db_port 5423: si collega alla porta che Docker espone sul tuo PC.
- --db_user odoo e --db_password myodoo: usa le credenziali che abbiamo appena trovato nel tuo file YAML.
