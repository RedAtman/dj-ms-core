# Deploy to production using Kubernetes

> **Note:** This is just an example.
> Please, review all the files in the `k8s` directory before applying them to your cluster.


---
## Prerequisites

> I assume that you have a Kubernetes cluster and `kubectl` installed.
> Other things I will try to describe here.

Copy example files

```shell
cp -r k8s/examples/app k8s/app
```

Create a namespace

```shell
kubectl create namespace ms-django
```


---
### PostgreSQL

If you don't have a PostgreSQL database, you can install it using the following commands:

```shell
kubectl create namespace postgres
kubectl apply -f k8s/examples/postgres -n postgres
```

You will need to create a database and a user for your application.

Get pod name:

```shell
kubectl get pods -n postgres
```

You should see something like this:

```shell
NAME                       READY   STATUS    RESTARTS   AGE
postgres-bbb44c799-g7v9j   1/1     Running   0          2m
```

Then you can connect to the database:

```shell
kubectl exec -it <pod-name> -n postgres -- psql -U postgres
```

Create a database:

```sql
CREATE DATABASE ms_django;
```

Create a user:

```sql
CREATE USER ms_django WITH ENCRYPTED PASSWORD 'ms_django';
```

Grant permissions and exit:

```sql
GRANT ALL PRIVILEGES ON DATABASE ms_django TO ms_django;
exit;
```


---
### RabbitMQ

If you don't have a RabbitMQ cluster, you can install it using the following commands:

Install RabbitMQ cluster connector:

```shell
kubectl apply -f "https://github.com/rabbitmq/cluster-operator/releases/latest/download/cluster-operator.yml" -n rabbitmq
```

Install RabbitMQ cluster:

```shell
kubectl create namespace rabbitmq
kubectl apply -f k8s/examples/rabbitmq -n rabbitmq
```

You will need to create a user for your application.

Get pod name:

```shell
kubectl get pods -n rabbitmq
```

You should see something like this:

```shell
NAME                       READY   STATUS    RESTARTS   AGE
rabbitmq-7c78d7f66b-n84jr  1/1     Running   0          2m
```

Create a user:

```shell
kubectl exec -it <pod-name> -n rabbitmq -- rabbitmqctl add_user ms_django ms_django
```

Grant permissions:

```shell
kubectl exec -it <pod-name> -n rabbitmq -- rabbitmqctl set_user_tags ms_django administrator
kubectl exec -it <pod-name> -n rabbitmq -- rabbitmqctl set_permissions -p / ms_django ".*" ".*" ".*"
```


---
### Ingress

If you don't have an Ingress controller, you can install ingres-nginx using the following commands:

```shell
kubectl apply -f k8s/examples/ingress-nginx
```


---
### TLS

> **NOTE:** If you have a TLS certificate for your domain, you should add it first.
> Otherwise, you can use the self-signed certificates by `Cert Manager`.

To add a TLS certificate, you should create a secret with the following files:
  - `tls.crt` - certificate
  - `tls.key` - private key

Then you can create a secret and deploy the application:

```shell
kubectl delete secret ms-django-tls-secret -n ms-django
kubectl create secret tls ms-django-tls-secret --cert=k8s/app/tls.crt --key=k8s/app/tls.key -n ms-django
```

Then you should add the following lines to the `Ingress` resource under the `spec` section:

```yaml
...
  tls:
    - hosts:
        - app.dj-ms.dev
      secretName: ms-django-tls-secret
...
```


---
### Cert Manager

If you don't have a Cert Manager, you can install it using the following commands:

```shell
kubectl create namespace cert-manager
kubectl apply -f k8s/examples/cert-manager -n cert-manager
```

To enable automatic TLS certificate generation, add the following **annotation** to the `Ingress` resource:

```yaml
...
  ...
    cert-manager.io/cluster-issuer: letsencrypt-production
...
```

Then add following lines to the `Ingress` resource under the `spec` section:

```yaml
...
  tls:
    - hosts:
        - app.dj-ms.dev
      secretName: ms-django-tls-secret
...
```


---
## Deploy

First of all, you should review all the files in the `k8s/app` directory.
Change the values as you need.

After that, you should create an `.env` file in the `k8s/app` directory.
It should contain the following variables:
  - `DJANGO_DEBUG` - normally `False` for production
  - `DJANGO_SECRET_KEY` - some random string. You can generate one with `openssl rand -base64 32`
  - `DATABASE_URL` - Postgres connection string, e.g. `postgres://ms_django:ms_django@postgres.postgres:5432/ms_django`
  - `DJANGO_ALLOWED_HOSTS` - your domain name. For example, `app.dj-ms.dev`
  - `DJANGO_CSRF_TRUSTED_ORIGINS` - usually the same as `DJANGO_ALLOWED_HOSTS` but with `https://` prefix. For example, `https://app.dj-ms.dev`
  - `BROKER_URL` - RabbitMQ connection string, e.g. `amqp://ms_django:ms_django@rabbitmq.rabbitmq:5672`

Then you can create a secret and deploy the application:

```shell
kubectl delete secret ms-django-secret -n ms-django
kubectl create secret generic ms-django-secret --from-env-file=k8s/app/.env -n ms-django
kubectl apply -f k8s/app -n ms-django
```


---
## Access your application

After successful deployment, you should be able to access your application at `https://app.example.com/admin`.
But if it's first time you deploy your application, you should create a superuser.

```shell
kubectl get pods -n ms-django
```

```shell
kubectl exec -it <pod-name> -n ms-django -- python manage.py createsuperuser
```

Then you can access your application at `https://app.example.com/admin` and log in with the credentials you have just created.
