# workshop-01-ao-vivo
workshop Projeto e Processo de Dados do Zero

1. Clone o repositorio: 
```bash
https://github.com/danieltodaDS/workshop-01-ao-vivo.git
cd ~/workshop-01-ao-vivo
```

2. Configure a versao correta do Python com `pyenv`: 
```bash
pyenv install 3.11.5
pyenv local 3.11.5
```

3. Instale as dependencias do projeto: 
```bash
python -m venv .venv
source .venv/bin/activate #Linux
.venv\Scripts\Activate #Windows
pip install -r requirements.txt
```