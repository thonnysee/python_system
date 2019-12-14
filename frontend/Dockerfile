FROM node:alpine as build-deps
WORKDIR /usr/src/app
COPY frontend/package*.json ./
COPY frontend/yarn.lock ./
RUN yarn
COPY ./frontend ./
RUN yarn build

CMD ["npm", "run", "start"]