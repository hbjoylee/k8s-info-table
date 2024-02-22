K8S dashboard accept JSON request posted from Kubernetes server and presents infomation in simple Flask table.

# Usage

## Build docker
`./build-docker.sh`

## Start service
`./start.sh`

## Access dashboard
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

## Clean up existing data 
1. Stop container `./stop.sh`
2. Remove container `docker rm -v k8s_dashboard`
3. Start container `./start.sh`
4. Check [dashboard](http://localhost:5000) 

# Post from Kubernetes server
Update `DASHBOARD_SRV` in `post-k8s-info.sh` script.
 
Check if `jq` installed on target Kubernetes server otherwise install with command below:

`sudo apt install jq -y`

## Copy scripts to Kubernetes server
`scp -r /k8s-scripts/post-k8s-info.sh target_srv:~/`

## Add cron job to check every day
`0 0 */1 * * /bin/bash ~/k8s-scripts/post-k8s-info.sh`

# Development
## Column change 
1. Add/remove columns in `models.py`
2. `flask db init` if you don't have migrations directory exist otherwise will see error `Directory migrations already exists and is not empty` which is safe to ignore 
3. `flask db migrate -m "Adding/Removing column x."`
4. `flask db upgrade`