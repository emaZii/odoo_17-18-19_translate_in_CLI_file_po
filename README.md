## Branch
- main-> odoo 18
- 17 -> odoo 17
- 19 -> odoo 19

### Tutorial
- copiare lo script translate_module.py nella cartella  ./odoo-folder/src18/odoo[versione]/
- Eseguire il comando:

## bash
'''
 python3 translate_module.py -d lab18 -m academy_system -p ../lab18 --db_port 5423 --db_user odoo --db_password myodoo 
'''

### Cosa fa questo comando:

- python3 translate_module.py: lancia lo script nella cartella attuale.
- -p ../lab18: dice a Odoo di "uscire" dalla cartella attuale e cercare i moduli dentro la cartella lab18.
- -m academy_system: cerca la cartella academy_system dentro lab18.
- Risultato: lo script creerà il file in ~/odoo-folder/src18/lab18/academy_system/i18n/it_IT.po.

----------------------------------------------------------------------

In alternativa mettere nel workspace quello che ce scritto in workspace.code-workspaceil 
file lo trovate nella repository basta copiare e incollare e corregere i percorsi delle cartella con i vostri

--------------------------------------------------------------------------------------

## Nota: 
- Il modulo a cui si deve esportare la traduzione deve essere installato su odoo se no il file .po sarà vuoto


