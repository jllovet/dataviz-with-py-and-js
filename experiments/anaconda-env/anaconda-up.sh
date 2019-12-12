#!/bin/bash
docker-compose up --build -d >> ./logs/buildlogs.txt 2>&1
docker-compose logs -ft >> ./logs/servicelogs.txt 2>&1 &
# docker run --name anaconda-shell -it anaconda