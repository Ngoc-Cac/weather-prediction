# Weather Prediction System with Docker Cluster

This is a group final project for High-Performance Computing. The project looks into a high-performance computing system used for weather prediction. To simulate the system, we deployed a RESTful API and a web UI application using Docker cluster.

## The regression model
We used a dataset of weather statistics from 2012 to 2017. The dataset comprises of five numeric features about the weather like temperature and humidty. Because the data is sequential, we used a LSTM neural network to predict a sequence of daily weather data with lag duration of seven days.

## Deploying Docker Cluster
To realistically simulate a cluster of independent machines, we deployed a Docker cluster of virtual machines using VirtualBox driver. In our demonstration, we created five machines with Docker installed, where four machines are used as slaves and one machine is used as the master:

<a name="table1"></a>
<table align="center">
    <caption>Table 1. Configurations of machines within the Docker Cluster</caption>
    <thead>
        <tr>
            <td>Machine</td>
            <td>Name</td>
            <td>Role</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>M1</td>
            <td>master</td>
            <td>Manage and schedule jobs, serving as an endpoint for the hosted services</td>
        </tr>
        <tr>
            <td>M2</td>
            <td>api-worker1</td>
            <td rowspan=2>Execute tasks related to the API service</td>
        </tr>
        <tr>
            <td>M3</td>
            <td>api-worker2</td>
        </tr>
        <tr>
            <td>M4</td>
            <td>web-worker1</td>
            <td rowspan=2>Execute tasks related to the Web UI service</td>
        </tr>
        <tr>
            <td>M5</td>
            <td>api-worker2</td>
        </tr>
    </tbody>
</table>

To deploy the cluster, we first built images that have specific dependencies installed for our API and Web UI. The Dockerfiles for these images can be found in [`docker-stacks`](./docker-stacks/). The images are also publicly available at [trinhngoccac/py-with-fastapi](https://hub.docker.com/r/trinhngoccac/py-with-fastapi) and [trinhngoccac/chakra-ui](https://hub.docker.com/r/trinhngoccac/chakra-ui).

Then, the virtual machines are created with the same configuration in [Table 1](#table1) with Docker pre-installed. To simplify the creation process, we used the [docker-machine](https://github.com/docker/machine) tool provided by Docker.

After creation of virtual machines, we created a cluster on the master node and linked other machines to this cluster. Once every machine has successfully joined the cluster, we then proceeed to deploy the services using the `docker stack deploy` command with a docker-compose file that has listed out the services and configurations. This file is provided at [docker-stack.yml](./docker-stack.yml).

---
### Our contributors:
<a href="https://github.com/Ngoc-Cac">
    <img src="https://avatars.githubusercontent.com/u/144905277?v=4" alt="drawing" width="60">
</a>
<a href="https://github.com/dothimykhanh">
    <img src="https://avatars.githubusercontent.com/u/120184309?v=4" alt="drawing" width="60">
</a>
<a href="https://github.com/NguyenTNTh">
    <img src="https://avatars.githubusercontent.com/u/203326835?v=4" alt="drawing" width="60">
</a>
<a href="https://github.com/phiyenng">
    <img src="https://avatars.githubusercontent.com/u/145342146?v=4" alt="drawing" width="60">
</a>