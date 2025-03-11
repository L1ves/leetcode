# Duplicate Integer
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
#
# Example 1:
#
# Input: nums = [1, 2, 3, 3]
#
# Output: true
# Example 2:
#
# Input: nums = [1, 2, 3, 4]
#
# Output: false

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False

    ---
    name: Docker
    Build and Deploy
    Prod
    env:
    GOOGLE_AUTH_CALLBACK_URL: ${{vars.GOOGLE_AUTH_CALLBACK_URL}}
    GOOGLE_AUTH_FINISH_URL: ${{vars.GOOGLE_AUTH_FINISH_URL}}
    KUBE_CONFIG: ${{secrets.KUBE_CONFIG}}


on:
push:
branches:
- dedicated

jobs:
build:
environment: prod
runs - on: ubuntu - latest
steps:
- name: Checkout
Repository
uses: actions / checkout @ v4

- name: Install
doctl
uses: digitalocean / action - doctl @ v2
with:
    token: ${{secrets.DIGITALOCEAN_ACCESS_TOKEN}}

- name: Log in to
DigitalOcean
Container
Registry
with short - lived credentials
run: doctl
registry
login - -expiry - seconds
2400

- name: Build
Base
Docker
Image
run: docker
build - f
cicd / dev / base.dockerfile - t
base: latest.

- name: Build
ui
Docker
Image
run: >
docker
build
-f
cicd / dev / ui.dockerfile
-t
registry.digitalocean.com / goldbet - docker - registry / ui:$(echo $GITHUB_SHA | head -c7).

- name: Push
Docker
Image
to
Registry
run: docker
push
registry.digitalocean.com / goldbet - docker - registry / ui:$(echo $GITHUB_SHA | head -c7)

- name: Build
admin
Docker
Image
run: >
docker
build
-f
cicd / dev / admin.dockerfile
-t
registry.digitalocean.com / goldbet - docker - registry / admin:$(echo $GITHUB_SHA | head -c7).

- name: Push
Docker
Image
to
Registry
run: docker
push
registry.digitalocean.com / goldbet - docker - registry / admin:$(echo $GITHUB_SHA | head -c7)

- name: Build
authd
Docker
Image
run: >
docker
build
-f
cicd / dev / authd.dockerfile
--build - arg
DATABASE_URL = "${{secrets.DATABASE_URL}}"
--build - arg
AUTHD_PORT = "${{vars.AUTHD_PORT}}"
--build - arg
AUTHD_HOST = "${{vars.AUTHD_HOST}}"
-t
registry.digitalocean.com / goldbet - docker - registry / authd:$(echo $GITHUB_SHA | head -c7).

- name: Push
Docker
Image
to
Registry
run: docker
push
registry.digitalocean.com / goldbet - docker - registry / authd:$(echo $GITHUB_SHA | head -c7)

- name: Build
userd
Docker
Image
run: >
docker
build
-f
cicd / dev / userd.dockerfile
--build - arg
DATABASE_URL = "${{secrets.DATABASE_URL}}"
-t
registry.digitalocean.com / goldbet - docker - registry / userd:$(echo $GITHUB_SHA | head -c7).

- name: Push
Docker
Image
to
Registry
run: docker
push
registry.digitalocean.com / goldbet - docker - registry / userd:$(echo $GITHUB_SHA | head -c7)

- name: Build
billingd
Docker
Image
run: >
docker
build
-f
cicd / dev / billingd.dockerfile
--build - arg
DATABASE_URL = "${{secrets.DATABASE_URL}}"
-t
registry.digitalocean.com / goldbet - docker - registry / billingd:$(echo $GITHUB_SHA | head -c7).

- name: Push
Docker
Image
to
Registry
run: docker
push
registry.digitalocean.com / goldbet - docker - registry / billingd:$(echo $GITHUB_SHA | head -c7)

- name: Build
notificationd
Docker
Image
run: >
docker
build
-f
cicd / dev / notificationd.dockerfile
--build - arg
DATABASE_URL = "${{secrets.DATABASE_URL}}"
-t
registry.digitalocean.com / goldbet - docker - registry / notificationd:$(echo $GITHUB_SHA | head -c7).

- name: Push
Docker
Image
to
Registry
run: docker
push
registry.digitalocean.com / goldbet - docker - registry / notificationd:$(echo $GITHUB_SHA | head -c7)

- name: Build
igaming - provider
Docker
Image
run: >
docker
build
-f
cicd / dev / igaming - provider.dockerfile
--build - arg
DATABASE_URL = "${{secrets.DATABASE_URL}}"
-t
registry.digitalocean.com / goldbet - docker - registry / igaming - provider:$(echo $GITHUB_SHA | head -c7).

- name: Push
Docker
Image
to
Registry
run: docker
push
registry.digitalocean.com / goldbet - docker - registry / igaming - provider:$(echo $GITHUB_SHA | head -c7)

- name: Build
api - gateway
Docker
Image
run: >
docker
build
-f
cicd / dev / api - gateway.dockerfile
-t
registry.digitalocean.com / goldbet - docker - registry / api - gateway:$(echo $GITHUB_SHA | head -c7).

- name: Push
Docker
Image
to
Registry
run: docker
push
registry.digitalocean.com / goldbet - docker - registry / api - gateway:$(echo $GITHUB_SHA | head -c7)

- name: Build
gb - nginx
Docker
Image
run: >
docker
build
-f
cicd / dev / nginx.dockerfile
-t
registry.digitalocean.com / goldbet - docker - registry / gb - nginx:$(echo $GITHUB_SHA | head -c7).

- name: Push
Docker
Image
to
Registry
run: docker
push
registry.digitalocean.com / goldbet - docker - registry / gb - nginx:$(echo $GITHUB_SHA | head -c7)

migrate:
environment: prod
runs - on: ubuntu - latest
needs: build
env:
DATABASE_URL: ${{secrets.PUBLIC_DATABASE_URL}}
SHADOW_DATABASE_URL: ${{secrets.PUBLIC_SHADOW_DATABASE_URL}}
PRISMA_SCHEMA_DISABLE_ADVISORY_LOCK: 1
steps:
- uses: actions / checkout @ main
- uses: actions / setup - node @ v4
with:
    node - version: "latest"
- run: npx
prisma
migrate
deploy

deploy:
environment: prod
runs - on: ubuntu - latest
needs: migrate
steps:
- uses: actions / checkout @ v4
- uses: actions - hub / kubectl @ master
env:
KUBE_CONFIG: ${{secrets.KUBE_CONFIG}}
with:
    args: get
    pods

- name: Update
deployment
file
run: >
TAG =$(echo $GITHUB_SHA | head -c7) & &
sed - i
's|<IMAGE>|registry.digitalocean.com/goldbet-docker-registry/api-gateway:'${TAG}
'|'
$GITHUB_WORKSPACE / kuber / dev / api - gateway.manifest.yaml

- name: Update
deployment
file
run: >
TAG =$(echo $GITHUB_SHA | head -c7) & &
sed - i
's|<IMAGE>|registry.digitalocean.com/goldbet-docker-registry/ui:'${TAG}
'|'
$GITHUB_WORKSPACE / kuber / dev / ui.manifest.yaml

- name: Update
deployment
file
run: >
TAG =$(echo $GITHUB_SHA | head -c7) & &
sed - i
's|<IMAGE>|registry.digitalocean.com/goldbet-docker-registry/authd:'${TAG}
'|'
$GITHUB_WORKSPACE / kuber / dev / authd.manifest.yaml

- name: Update
deployment
file
run: >
TAG =$(echo $GITHUB_SHA | head -c7) & &
sed - i
's|<IMAGE>|registry.digitalocean.com/goldbet-docker-registry/userd:'${TAG}
'|'
$GITHUB_WORKSPACE / kuber / dev / userd.manifest.yaml

- name: Update
deployment
file
run: >
TAG =$(echo $GITHUB_SHA | head -c7) & &
sed - i
's|<IMAGE>|registry.digitalocean.com/goldbet-docker-registry/billingd:'${TAG}
'|'
$GITHUB_WORKSPACE / kuber / dev / billingd.manifest.yaml

- name: Update
deployment
file
run: >
TAG =$(echo $GITHUB_SHA | head -c7) & &
sed - i
's|<IMAGE>|registry.digitalocean.com/goldbet-docker-registry/igaming-provider:'${TAG}
'|'
$GITHUB_WORKSPACE / kuber / dev / igaming - provider.manifest.yaml

- name: Update
deployment
file
run: >
TAG =$(echo $GITHUB_SHA | head -c7) & &
sed - i
's|<IMAGE>|registry.digitalocean.com/goldbet-docker-registry/notificationd:'${TAG}
'|'
$GITHUB_WORKSPACE / kuber / dev / notificationd.manifest.yaml

- name: Update
deployment
file
run: >
TAG =$(echo $GITHUB_SHA | head -c7) & &
sed - i
's|<IMAGE>|registry.digitalocean.com/goldbet-docker-registry/gb-nginx:'${TAG}
'|'
$GITHUB_WORKSPACE / kuber / dev / nginx.manifest.yaml

- name: Update
deployment
file
run: >
TAG =$(echo $GITHUB_SHA | head -c7) & &
sed - i
's|<IMAGE>|registry.digitalocean.com/goldbet-docker-registry/admin:'${TAG}
'|'
$GITHUB_WORKSPACE / kuber / dev / admin.manifest.yaml

- name: Create
configmap
uses: actions - hub / kubectl @ master
env:
KUBE_CONFIG: ${{secrets.KUBE_CONFIG}}
with:
    args: |
    kubectl
    create
    configmap
    gb - config
    --
    from

    -literal = DATABASE_URL = "${{ secrets.DATABASE_URL }}"
    --
    from

    -literal = API_GATEWAY_PORT = 5000
    --
    from

    -literal = AUTHD_PORT = 5001
    --
    from

    -literal = USERD_PORT = 5002
    --
    from

    -literal = BILLINGD_PORT = 5003
    --
    from

    -literal = IGAMING_PROVIDER_PORT = 5004
    --
    from

    -literal = NOTIFICATIOND_PORT = 5006
    --
    from

    -literal = USERD_HOST = userd
    --
    from

    -literal = AUTHD_HOST = authd
    --
    from

    -literal = BILLINGD_HOST = billingd
    --
    from

    -literal = NOTIFICATIOND_HOST = notificationd
    --
    from

    -literal = API_GATEWAY_HOST = api - gateway
    --
    from

    -literal = IGAMING_PROVIDER_HOST = igaming - provider
    --
    from

    -literal = CHANGELLY_PAY_PRIVATE_KEY = "${{ secrets.CHANGELLY_PAY_PRIVATE_KEY }}"
    --
    from

    -literal = CHANGELLY_PAY_PUBLIC_KEY = "${{ secrets.CHANGELLY_PAY_PUBLIC_KEY }}"
    --
    from

    -literal = NATS_TOKEN = "${{ secrets.NATS_TOKEN }}"
    --
    from

    -literal = NATS_URL = nats: // nats: 4222
    --
    from

    -literal = GOOGLE_AUTH_CLIENT_ID = "${{ secrets.GOOGLE_AUTH_CLIENT_ID }}"
    --
    from

    -literal = GOOGLE_AUTH_CLIENT_SECRET = "${{ secrets.GOOGLE_AUTH_CLIENT_SECRET }}"
    --
    from

    -literal = GOOGLE_AUTH_CALLBACK_URL = "${{ vars.GOOGLE_AUTH_CALLBACK_URL }}"
    --
    from

    -literal = GOOGLE_AUTH_FINISH_URL = "${{ vars.GOOGLE_AUTH_FINISH_URL }}"
    --
    from

    -literal = FACEBOOK_AUTH_CLIENT_ID = "${{ secrets.FACEBOOK_AUTH_CLIENT_ID }}"
    --
    from

    -literal = FACEBOOK_AUTH_CLIENT_SECRET = "${{ secrets.FACEBOOK_AUTH_CLIENT_SECRET }}"
    --
    from

    -literal = FACEBOOK_AUTH_CALLBACK_URL = "${{ vars.FACEBOOK_AUTH_CALLBACK_URL }}"
    --
    from

    -literal = SOFTSWISS_BACKEND_URL = "${{ vars.SOFTSWISS_BACKEND_URL }}"
    --
    from

    -literal = SOFTSWISS_CDN_URL = "${{ vars.SOFTSWISS_CDN_URL }}"
    --
    from

    -literal = SOFTSWISS_AUTH_TOKEN = "${{ secrets.SOFTSWISS_AUTH_TOKEN }}"
    --
    from

    -literal = SOFTSWISS_CASINO_ID = "${{ vars.SOFTSWISS_CASINO_ID }}"
    --
    from

    -literal = OAUTH_FINISH_PATH = "${{ vars.OAUTH_FINISH_PATH }}"
    --
    from

    -literal = NEXT_PUBLIC_GOLDBET_S3_URL = "${{ vars.GOLDBET_S3_URL }}"
    --
    from

    -literal = GOLDBET_S3_URL = "${{ vars.GOLDBET_S3_URL }}"
    --
    from

    -literal = COINLAYER_ACCESS_KEY = "${{ secrets.COINLAYER_ACCESS_KEY }}"
    --
    from

    -literal = MANY_APIS_ACCESS_KEY = "${{ secrets.MANY_APIS_ACCESS_KEY }}"
    --
    from

    -literal = CUSTOMER_IO_SITE_ID = "${{ secrets.CUSTOMER_IO_SITE_ID }}"
    --
    from

    -literal = CUSTOMER_IO_API_KEY = "${{ secrets.CUSTOMER_IO_API_KEY }}"
    --
    from

    -literal = CUSTOMER_IO_APP_KEY = "${{ secrets.CUSTOMER_IO_APP_KEY }}"
    --
    from

    -literal = INTERKASSA_API_ENDPOINT = "${{ vars.INTERKASSA_API_ENDPOINT }}"
    --
    from

    -literal = INTERKASSA_PROD_MODE = "${{ vars.INTERKASSA_PROD_MODE }}"
    --
    from

    -literal = BILLBLEND_API_ENDPOINT = "${{ vars.BILLBLEND_API_ENDPOINT }}"
    --
    from

    -literal = BASE_CALLBACK_URL = "${{ vars.BASE_CALLBACK_URL }}"
    --
    from

    -literal = UI_URL = "${{ vars.UI_URL }}"
    --
    from

    -literal = ALANBASE_EVENTS_ENDPOINT = "${{ vars.ALANBASE_EVENTS_ENDPOINT }}"
    --
    from

    -literal = REDIS_HOST = "${{ vars.REDIS_HOST }}"
    --
    from

    -literal = DESCOPE_PROJECT_ID = "${{ secrets.DESCOPE_PROJECT_ID }}"
    --
    from

    -literal = SAFE_AUTH_URL = "${{ vars.SAFE_AUTH_URL }}"
    --
    from

    -literal = BSG_API_KEY = "${{ secrets.BSG_API_KEY }}"
    --
    from

    -literal = NODE_ENV = "production"
    --
    from

    -literal = NODE_OPTIONS = "--dns-result-order=ipv4first"
    --
    from

    -literal = SPORTBOOK_API_KEY = "${{ secrets.SPORTBOOK_API_KEY }}"
    --validate = false - -dry - run = client - o
    yaml | kubectl
    apply - f -

- name: Deploy
to
ovh
Kubernetes
uses: actions - hub / kubectl @ master
env:
KUBE_CONFIG: ${{secrets.KUBE_CONFIG}}
with:
    args: kubectl
    apply - f $GITHUB_WORKSPACE / kuber / prod
