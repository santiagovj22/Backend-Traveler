FROM node:latest as builder
LABEL maintainer=jalasoftbootcamp@jalasoft.com
ENV NODE_OPTIONS '--max_old_space_size=4096'
WORKDIR /react/app
COPY . .
RUN (npm install && npm run build)

FROM nginx:alpine
WORKDIR /usr/share/nginx/html
COPY --from=builder /react/app/build .
COPY nginx.conf /etc/nginx/nginx.conf
