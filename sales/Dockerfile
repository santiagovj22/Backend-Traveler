#creando una imagen a partir de un contenedor
#instancio la imagen
# FROM nginx:latest 

#copio toda los archivos que estan dentro del build
#tambien con la configuracion de leer todas las rutas dentro del nginx
# COPY nginx.conf /etc/nginx/conf.d/default.conf

FROM docker:latest as builder
WORKDIR /react/app
COPY . .
RUN (npm install && npm run build)

FROM nginx:alpine
WORKDIR  /usr/share/nginx/html
COPY --from=builder /react/app/build .
COPY nginx.conf /etc/nginx/conf.d/default.conf
