# champagne_coding-26022020
Champagne Coding with Redpill Linpro on February 26, 2020

## Set-up

To re-create the environment:
- Make sure ```conda``` is installed
- ```conda create --name champagne_coding --file environment.txt``` OR ```conda create --name champagne_coding --file explicit_env.txt```
-- __NOTE:__ if this doesn't work and you're using Windows, you may have to install the Python packages as you go through the code
- ```conda activate champagne_coding```
- Start a jupyter notebook (```jupyter notebook```) 



## Docker

Running the code locally:

```
docker build . -t champ
docker run -p 8080:8080  --volume="$PWD:/app" champ
docker tag champ docker-registry-default.apps.redpill-linpro.com/champagne-coding/champ
docker login -u default -p $(oc whoami -t) docker-registry-default.apps.redpill-linpro.com
```


triggers:
    - type: ConfigChange
    - imageChangeParams:
        automatic: true
        containerNames:
          - gitlab-runner
        from:
          kind: ImageStreamTag
          name: 'gitlab-runner:alpine'
          namespace: gitlab
        lastTriggeredImage: >-
          docker.io/gitlab/gitlab-runner@sha256:9b96b923979e3060604b0ff97ab1a70a22769208a168ff50b0f77c7275969f54
      type: ImageChange


oc tag docker.io/gitlab/gitlab-runner:alpine gitlab-runner:alpine --scheduled
