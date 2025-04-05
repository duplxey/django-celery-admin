# Running Background Tasks from Django Admin

## Want to learn how to build this?

Check out the [post](x).

## Want to use this project?

1. Fork/Clone

1. Spin up the project using [Docker Compose](https://docs.docker.com/compose/):

   ```sh
   $ docker compose up --build -d
   ```

1. Create a superuser:

   ```sh
   $ docker compose exec web python manage.py createsuperuser
   ```
   
1. Navigate to [http://localhost:8000/admin/reports/report/](http://localhost:8000/admin/reports/report/) in your browser and kick off a task by clicking "Generate report".
