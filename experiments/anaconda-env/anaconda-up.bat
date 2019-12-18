docker-compose up --build -d >> ./logs/buildlogs.txt 2>&1
docker-compose logs -ft >> ./logs/servicelogs.txt 2>&1 &
echo "A link to log in for the first time to the jupyter notebook that started in the container will be available in logs/servicelogs.txt"
