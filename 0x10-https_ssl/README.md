# Background Context
## What happens when you don’t secure your website traffic?
![Boum!!!!](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/276/xCmOCgw.gif)

# Resources

* [What is HTTPS?](https://www.instantssl.com/http-vs-https)
* [What are the 2 main elements that SSL is providing](https://www.sslshopper.com/why-ssl-the-purpose-of-using-ssl-certificates.html)
* [HAProxy SSL termination on Ubuntu16.04](https://docs.ionos.com/cloud)
* [SSL termination](https://en.wikipedia.org/wiki/TLS_termination_proxy)
* [Bash function](https://tldp.org/LDP/abs/html/complexfunct.html)

![Load Balancer](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/276/FlhGPEK.png)


# Learning Objectives
## General
* General
* What is HTTPS SSL 2 main roles
* What is the purpose encrypting traffic
* What SSL termination means

# Command to run for security setting up
* sudo apt update
* sudo apt install snapd
* sudo apt-get remove certbot
* sudo apt-get install certbot
* sudo certbot certonly --standalone --preferred-challenges http --http-01-port 80 -d example.com -d www.example.com
* sudo ls /etc/letsencrypt/live/your_domain_name
* sudo mkdir -p /etc/haproxy/certs
* DOMAIN='example.com' sudo -E bash -c 'cat /etc/letsencrypt/live/$DOMAIN/fullchain.pem /etc/letsencrypt/live/$DOMAIN/privkey.pem > /etc/haproxy/certs/$DOMAIN.pem'
* sudo chmod -R go-rwx /etc/haproxy/certs
* sudo nano /etc/haproxy/haproxy.cfg

# Content of hproxy/haproxy.cfg
* Refer to 100-redirect_http_to_https
