# Frontend Dockerfile
FROM node:18-alpine

WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy source code
COPY . .

# Build the app
RUN npm run build

# Expose port and start the app
EXPOSE 3000
CMD ["npm", "start"]
