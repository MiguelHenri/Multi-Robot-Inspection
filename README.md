# ⚙ Multi-Robot Inspection

A ROS-Blockchain framework for multi-robot systems applied to industrial safety inspections.

# 🗺 Overview

This framework presupposes you have a robot (or simulator) running ROS and sharing odometry data through ROS topics. 

It bridges the ROS topic to an IBFT Hyperledger Besu blockchain network using the Web3.py library. Each robot has a PythonAPI capable of transacting to the blockchain network.

See Hyperledger Besu documentation: https://besu.hyperledger.org/23.4.0/private-networks/tutorials/ibft
See Web3.py documentation: https://web3py.readthedocs.io/en/stable/

# 🖋 Smart Contracts

This framework presents two smart contracts: Share Data and Calibration.

Each robot's PythonAPI uses the Share Data contract to transact and share data collected in inspection tasks into the blockchain network.

Technicians use the calibration contract to keep the robots calibrated and safe.

# 🕹 How to Run

First, you will need an odometry ROS topic running in a Linux Terminal. You can save the odometry data collected into a file.

Then, [to-do]

