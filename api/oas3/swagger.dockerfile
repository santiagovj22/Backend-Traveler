FROM swaggerapi/swagger-ui

COPY . /oas
ENV SWAGGER_JSON /oas/api.yaml
EXPOSE 8080
