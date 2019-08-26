# Battle For Castile: Match Consumer

[![CircleCI](https://circleci.com/gh/battleforcastile/battleforcastile-match-consumer/tree/master.svg?style=svg)](https://circleci.com/gh/battleforcastile/battleforcastile-match-consumer/tree/master)

This micro-service handles the consumption of pending matches
## 1. Installation and set up

> This guide assumes that there's a K8s cluster (with Helm-tiller) and a rabbitmq server in place.

#### 1.1 Go to `/helm/battleforcastile-match-consumer/` folder and copy the content from `templates-examples` to `templates`
```
cp helm/battleforcastile-match-consumer/templates-examples/* helm/battleforcastile-match-consumer/templates/*
```

#### 1.3 Uncomment the content from `battleforcastile-match-consumer-secrets.yml` (from `templates`) and replace:
 - The value of `secret_key` by the `base64` value of the secret key of your Flask App (can be random)

#### 1.4 Run `helm install helm/battleforcastile-match-consumer` and in a few minutes it should be deployed! :)
