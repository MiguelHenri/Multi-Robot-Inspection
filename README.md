# ⚙ Multi-Robot Inspection

A ROS-Blockchain framework for multi-robot systems applied to industrial safety inspections.

# 🗺 Overview

This framework was made for research purposes. It presupposes you have at least a robot (or simulator) running ROS and sharing odometry data through a ROS topic (publisher node). It makes a bridge between the ROS topic and an IBFT Hyperledger Besu blockchain network using a PythonAPI (Web3.py).

# 🖋 Smart Contracts

This framework presents two smart contracts:

- `Share Data`: Each robot's PythonAPI uses the Share Data contract to transact and share the data collected in inspection tasks into the blockchain network.

- `Calibration`: Technicians use the calibration contract to keep the robots calibrated and safe.

# 🕹 How to Run

## Data Acquisition

We used the [CoppeliaSim](https://coppeliarobotics.com/) to simulate four robots collecting data in our tests and research system evaluation. We collected odometry (pose) data into .txt files. Check [/data](https://github.com/MiguelHenri/Multi-Robot-Inspection/tree/main/data) for more information. 

Our framework can handle any data type (Share Data contract and PythonAPI may be adapted for another data type). 

For big data, such as point cloud, you should use [IPFS](https://docs.ipfs.tech/).

## Blockchain

To run the IBFT Hyperledger Besu blockchain network, check:

- [How to run Besu](https://besu.hyperledger.org/23.4.0/private-networks/tutorials/ibft).

Our network was configured with four validator nodes and a 2-second block production.

## PythonAPI

Before running any Python code, create and activate a virtual environment and install the dependencies:

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

With the data collected and the blockchain network running, the PythonAPI creates transactions using [Web3.py](https://web3py.readthedocs.io/en/stable/.).

Before sending transactions, make sure the Share Data contract is deployed into the network, you can do this using [RemixIDE](https://remix.ethereum.org/) and [Metamask](https://metamask.io/). Set the local network with the same ChainID as your local blockchain and save the contract address. 

In our research, we collected the transaction time. You can run using:

```bash
$ python3 time_evaluation.py
```

⚠️ Make sure:
- The files, contract address, and private keys are named correctly;
- The file paths are set correctly (e.g. pose1.txt);
- You have all Python files installed;
- Your blockchain network is running fine.

To run in real-time, ensure your evaluation can read the data from a ROS topic. You can do this using [subprocess](https://docs.python.org/3/library/subprocess.html).

## Faulty Node Evaluation

We collected the transaction time with a faulty validator node in our blockchain Besu network. To do this, just kill one of the validator nodes' terminal.  

##  Delayed Evaluation

Our research also collected the transaction time when inducing a delay in the blockchain network. To do this, run this [Linux Traffic Control](https://access.redhat.com/documentation/pt-br/red_hat_enterprise_linux/8/html/configuring_and_managing_networking/linux-traffic-control_configuring-and-managing-networking) command:

```bash
$ sudo tc qdisc add dev lo root netem delay 100ms
```
- Command example for inducing 100ms delay. 
- Make sure your Besu network interface is 'lo'.

Check if the delay is working and running:

```bash
$ sudo tc qdisc show dev lo
```

## Centralized Evaluation

For research purposes, we also assessed transaction times with a centralized database.
> We employed PostgreSQL for this purpose.

To run the code, make sure you have PostgreSQL installed and running. Configure the database constants in the `main` function of `centralized.py`. Then, execute the following command:
```bash
$ python3 centralized.py
```

## Charts

Check [/charts](https://github.com/MiguelHenri/Multi-Robot-Inspection/tree/main/charts) for the three Python scripts employed to build the evaluation box-plot graphs. They use [matplotlib](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html).

# 🤝 Contributor
- https://github.com/rodrigodg1
