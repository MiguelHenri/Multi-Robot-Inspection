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

In our tests and research system evaluation we used the [CoppeliaSim](https://coppeliarobotics.com/) to simulate four robots collecting data. We collected odometry (pose) data into .txt files.

Our framework can handle any data type (Share Data contract and PythonAPI may be adapted for another data type). 

For big data, such as point cloud, you should use [IPFS](https://docs.ipfs.tech/).

## Blockchain

To run the IBFT Hyperledger Besu blockchain network, check:

- [How to run Besu](https://besu.hyperledger.org/23.4.0/private-networks/tutorials/ibft).

Our network was configured with four validator nodes and a 2-second block production.

## PythonAPI

With the data collected and the blockchain network running, the PythonAPI creates transactions using [Web3.py](https://web3py.readthedocs.io/en/stable/.).

Before sending transactions, make sure the Share Data contract is deployed into the network, you can do this using [RemixIDE](https://remix.ethereum.org/) and [Metamask](https://metamask.io/). Set the local network with the same ChainID as your local blockchain and save the contract address. 

In our research, we collected the transaction time. You can run using:

```bash
../python$ python3.py time_evaluation.py
```

⚠️ Make sure:
- The files, contract address, and private keys are named correctly;
- The file paths are set correctly;
- You have all python files installed;
- Your blockchain network is running fine;
- Your data is not too big (will take a long time).

For running in real-time, ensure your evaluation can read the data from a ROS-topic. You can do this using [subprocess](https://docs.python.org/3/library/subprocess.html).

# 🤝 Contributor
- https://github.com/rodrigodg1
