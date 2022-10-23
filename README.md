# container operation
this repo will setup a simple jenkins node with installed plugins on demand
use the <docker compose up -d > to setup the container.
** plugin for integration with maven,and  email notifications is now enabeled in this docker image release .(2.4)

jenkins will not need any initialization, its ready to use out of the box. uses the below admin user
please use docker run -d -p 8080:8080 -v ibexdata:/var/jenkins_home imageforibex include the volume in order to operate fully working container.
this image has been created using the repo dockerfile as a base image
# docker hub image for jenkins <docker pull raananjovani/imageforibex:v2.0>
# user admin Pass ibex123