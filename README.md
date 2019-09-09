# Battle For Castile: Match Consumer

[![CircleCI](https://circleci.com/gh/battleforcastile/battleforcastile-match-consumer/tree/master.svg?style=svg)](https://circleci.com/gh/battleforcastile/battleforcastile-match-consumer/tree/master)

This micro-service handles the consumption of pending matches
## 1. Installation and set up

> This guide assumes that there's a K8s cluster (with Helm-tiller) and a rabbitmq server in place.

#### 1.1 Run `helm install helm/battleforcastile-match-consumer --set rabbitmqpassword=... --set rabbitmquser=... --set secretkey=...` and in a few minutes it should be deployed! :)

* The value of `rabbitmqpassword` is the `base64` of the rabbitmq password
* The value of `rabbitmquser` is the `base64` value of the rabbitmq user
* The value of `secretkey` is the `base64` value of the secret key of your Flask App (can be random)
