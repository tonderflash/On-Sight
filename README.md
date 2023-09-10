# Proyecto Django en Docker con Postgres

Este proyecto está diseñado como una guía para aquellos que están aprendiendo a trabajar con Django, Docker y Postgres. Incorpora las mejores prácticas en el desarrollo, unit-testing, y está configurado con GitHub Actions y Flake 8 para garantizar la calidad del código y la integración continua. 

## Características

- **Django**: Un framework web de alto nivel, escrito en Python.
- **Docker**: Una plataforma para desarrollar, enviar y correr aplicaciones en contenedores.
- **Postgres**: Un sistema de gestión de bases de datos relacional.
- **GitHub Actions**: Automatización de flujo de trabajo para CI/CD.
- **Flake 8**: Herramienta de linting para Python para mejorar la calidad del código.

## Pre-requisitos

- Docker y Docker Compose instalados en tu máquina.
- Conocimiento básico en Django, Docker y Postgres.

## Instrucciones de Configuración

1. Clonar el repositorio:

   ```bash
   git clone <url_del_repositorio>
   ```

2. Navegar al directorio del proyecto:

   ```bash
   cd <nombre_del_directorio>
   ```

3. Construir el proyecto:

   ```bash
   docker-compose build
   ```

4. Iniciar el proyecto:

   ```bash
   docker-compose up
   ```

   O si prefieres ejecutar el servidor Django directamente:

   ```bash
   docker-compose run --rm app sh -c "python manage.py runserver"
   ```
   Ejecuta el siguiente comando para iniciar el proceso de creación de un superusuario:

  ```bash
    docker-compose run --rm app sh -c "python manage.py createsuperuser"
  ```

## Cómo ejecutar comandos

Para ejecutar cualquier comando relacionado con el proyecto:

```bash
docker-compose run --rm app sh -c "<comando>"
```

Por ejemplo, para ejecutar migraciones:

```bash
docker-compose run --rm app sh -c "python manage.py migrate"
```

## Contribución y Soporte

Si tienes sugerencias, correcciones o mejoras, no dudes en hacer un pull request o crear un issue en GitHub. Si tienes dudas sobre el proyecto o te encuentras con algún problema, puedes escribirme directamente.

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Eres libre de usar, modificar y distribuir el código, pero por favor, proporciona atribución adecuada.

---

Espero que este proyecto te sirva como guía y referencia en tu aprendizajes y desarrollo. ¡Buena Suerte!
