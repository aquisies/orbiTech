#!/bin/bash

# TODO: Crear directorio app/api/endpoints
mkdir -p FASTAPI/app/api/endpoints
touch FASTAPI/app/api/endpoints/__init__.py
touch FASTAPI/app/api/endpoints/hubspot.py
touch FASTAPI/app/api/endpoints/clickup.py

# TODO: Crear directorio app/database
mkdir -p FASTAPI/app/database
touch FASTAPI/app/database/__init__.py
touch FASTAPI/app/database/models.py
touch FASTAPI/app/database/crud.py

# TODO: Crear directorio app/utils
mkdir -p FASTAPI/app/utils
touch FASTAPI/app/utils/__init__.py
touch FASTAPI/app/utils/logging.py

# TODO: Crear archivo requirements.txt
touch FASTAPI/requirements.txt

# TODO: Crear archivo README.md
touch FASTAPI/README.md

pip install -r requirements.txt