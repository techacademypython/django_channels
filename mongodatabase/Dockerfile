FROM mongo:3.6.3

MAINTAINER <Munis Isazade> munisisazade@gmail.com

# Enviroment
ENV AUTH yes
ENV MONGODB_ADMIN_USER root
ENV MONGODB_ADMIN_PASS tmdfUNectyJqWab3zGZ3dQD72qE2CwUD3wfd
ENV MONGODB_APPLICATION_DATABASE api_test
ENV MONGODB_APPLICATION_USER api_user
ENV MONGODB_APPLICATION_PASS TC6eHtutV6U488r8ugav95S93d6AzJh6Aab

EXPOSE 27017 27017

ADD run.sh /run.sh

ADD set_mongodb_password.sh /set_mongodb_password.sh

RUN chmod +x /run.sh

RUN chmod +x /set_mongodb_password.sh

CMD ["/run.sh"]