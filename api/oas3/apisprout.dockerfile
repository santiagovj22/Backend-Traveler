FROM danielgtaylor/apisprout

COPY . /oas
EXPOSE 8000
CMD ["/oas/api.yaml"]
