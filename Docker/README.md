# container operation
this is a simple jenkins node with installed plugins on demand
** plugin for integration with maven,and email notifications are now enabeled in this docker image release

jenkins will not need any initialization, its ready to use out of the box.
execute <docker run -d -p 8080:8080 -v ibexdata:/var/jenkins_home raananjovani/imageforibex:v2.0> include the volume in order to operate fully working container with data persistent .
this image has been created using the repo dockerfile as a base image
# docker hub image for image pulling <docker pull raananjovani/imageforibex:v2.0>
# user admin Pass ibex123 for jenkins 