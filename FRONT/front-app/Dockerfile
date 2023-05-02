# Use official Node.js image as the base image
FROM node:20-alpine

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install app dependencies
RUN npm ci

# Copy app source code
COPY . .

# Build the React app for production
RUN npm run build

# Expose the port
EXPOSE 3000

# Use serve to serve the static files
CMD ["npx", "serve", "-s", "build", "-l", "3000"]
