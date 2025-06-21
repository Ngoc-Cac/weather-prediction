# Weather Prediction System with Docker Cluster

This is a group final project for High-Performance Computing. The project looks into a high-performance computing system used for weather prediction. To simulate the system, we deployed a RESTful API and a web UI application using Docker cluster.

## The regression model
We used a dataset of weather statistics from 2012 to 2017. The dataset comprises of five numeric features about the weather like temperature and humidty. Because the data is sequential, we used a LSTM neural network to predict a sequence of daily weather data with lag duration of seven days.

## Deploying Docker Cluster
To realistically simulate a cluster of independent machines, we deployed a Docker cluster of virtual machines using VirtualBox driver. In our demonstration, we created five machines with Docker installed, where four machines are used as slaves and one machine is used as the master.

To deploy the cluster, we first built images that have specific dependencies installed for our API and Web UI. Then, we used deploy a docker stack using the docker-compose file format with two services.
