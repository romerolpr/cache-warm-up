import sys
from app import App
from app.shared.utils import is_empty

try:
    app = App()
    domain = input("Enter the DOMAIN (www.valesaude.com.br): ")
    domain = str(domain) if not is_empty(domain) else 'www.valesaude.com.br'
    app.run(domain=domain)
finally:
    sys.exit()