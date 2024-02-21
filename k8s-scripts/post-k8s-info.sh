#!/bin/bash
URL=`kubectl get --all-namespaces ingress -o json 2> /dev/null| jq -r '.items[] | .spec.rules[] | .host as $host | .http.paths[] | ( $host )' |sort|uniq`

K8SVER=`kubectl -n kube-system get cm kubeadm-config -o json|jq -r .data.ClusterConfiguration|grep kubernetesVersion |awk '{print $2}'`

EXPIRE_DATE=`cat ~/.kube/config | grep client-certificate-data | cut -f2 -d : | tr -d ' ' | base64 -d | openssl x509 -text -out - | grep "Not After"|sed -e 's/^[ \t]*//'`

DASHBOARD_SRV="http://192.168.17.35:5000/feed"

#echo "url:$URL"
#echo "k8sver:$K8SVER"
#echo "expire:$EXPIRE_DATE"

json=$(jq -c -n --arg url "$URL" --arg k8sver "$K8SVER"  --arg expire "$EXPIRE_DATE" '$ARGS.named')

curl -i -H "Accept: application/json" -H "Content-Type:application/json" -X POST $DASHBOARD_SRV --data "$json"