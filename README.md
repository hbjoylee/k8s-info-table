K8S dashboard accept JSON request posted from Kubernetes server and presents infomation in simple Flask table.

# Usage

## Build docker
`./build-docker.sh`

## Start service
`./start.sh`

## Acess dashboard
Open browser and open 
[K8s Dashboard](http://localhost:5000)

## Feed data
`
curl --location 'http://localhost:5000/feed' \
--header 'Content-Type: application/json' \
--data '{
  "url": "https://internmatch-staging2-office.io",
  "k8sver": "1.26.18",
  "expire": "2023-11-22"
}'
`

## Stop service
`./stop.sh`

