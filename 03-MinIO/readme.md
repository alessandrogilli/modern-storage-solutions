# 03 - MinIO
## Environment configuration
- Install [Docker and Docker compose](https://docs.docker.com/engine/install/)
- Inside this directory, open a terminal and run:
    
    ```docker compose up -d```

## mc client
### Installation
```bash
wget https://dl.min.io/client/mc/release/linux-amd64/mc

chmod +x mc

./mc --help
```

### Setup
```bash
./mc alias set myminio2 http://localhost:9000 minio minio123
```

### Commands
- Basic functions:
    ```bash
    ./mc mb myminio2/my-bucket 

    ./mc cp docker-compose.yml myminio2/my-bucket

    ./mc cat myminio2/my-bucket/docker-compose.yml

    ./mc head -n 3 myminio2/my-bucket/docker-compose.yml

    ./mc cp -r ../04-parquet myminio2/my-bucket  

    ./mc du myminio2/my-bucket
    ```
- Advanced functionalities of Object Storage:
    ```bash
    ./mc mb myminio2/public-bucket

    ./mc anonymous get myminio2/public-bucket

    ./mc anonymous set public myminio2/public-bucket

    ./mc cp cmatrix.png myminio2/public-bucket

    ./mc cp my-site.html myminio2/public-bucket
    ```

    check http://localhost:9000/public-bucket/my-site.html

## Web UI
https://localhost:9001

