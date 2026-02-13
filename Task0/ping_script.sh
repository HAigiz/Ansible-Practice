#!/bin/bash
while true; do echo "$(date '+%Y-%m-%d %H:%M:%S') | Code: $(curl -s -o /dev/null -w "%{http_code}" https://s3.mdst.yandex.net) | Time: $(curl -s -o /dev/null -w "%{time_total}" https://s3.mdst.yandex.net)s"; sleep 10; done
