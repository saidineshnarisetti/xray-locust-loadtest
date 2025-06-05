# Set your JFrog domain
export JFROG_DOMAIN=trialf6dxqy.jfrog.io

# Login to Docker with JFrog credentials
docker login $JFROG_DOMAIN

# Pull, tag, and push Alpine 3.9
docker pull alpine:3.9
docker tag alpine:3.9 $JFROG_DOMAIN/docker-local/alpine:3.9
docker push $JFROG_DOMAIN/docker-local/alpine:3.9