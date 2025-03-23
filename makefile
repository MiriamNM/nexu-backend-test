# Show help (list of available commands)
help:
	@echo "Comands:"
	@echo "  make help         : Display this list of commands."
	@echo "  make create-venv  : Create a virtual environment with Python 3.11."
	@echo "  make install      : Install all necessary dependencies."
	@echo "  make test         : Run the tests."
	@echo "  make run          : Start the service and all related services (such as a DB) in Docker."
	@echo "  make down         : Stops all running services."
	@echo "  make clean        : Stops and removes all associated containers and resources."
	@echo "  make clear        : Clean temporary files."

create-venv:
	python3.11 -m venv nexu
	@echo "Entorno virtual creado con Python 3.11."
	@echo "Ejecuta 'source nexu/bin/activate' para activarlo."

pip: create-venv
	source nexu/bin/activate && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python get-pip.py
	@echo "pip instalado correctamente en el entorno virtual."

install: pip
	source nexu/bin/activate && pip install -r requirements.txt
	@echo "Ejecuta: export PYTHONPATH=$PYTHONPATH:$(pwd)/app  antes de make test-requirements"

#Para asegurar que todas las dependencias estan correctamente, sobretodo uvicorn y fastapi.
test-requirements:
	export PYTHONPATH=$PYTHONPATH:$PYTHONPATH:$(pwd)/app
	source nexu/bin/activate && pip install --no-cache-dir -r requirements.txt
	uvicorn app.app:app --host 0.0.0.0 --port 8080 --reload

# Construir la imagen
build:
	docker build -t nexu .

# Levantar los servicios con Docker Compose
up:
	docker-compose --env-file .env up --build

# Detener los servicios
down:
	docker-compose down

# Elimina volumenes e imagenes y vuelve a construir todo el contenedor
rebuild: 
	docker-compose down --volumes --rmi all
	docker-compose --env-file .env up --build
