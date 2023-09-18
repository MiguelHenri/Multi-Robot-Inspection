from web3 import Web3
from solcx import compile_source

def compile_sol():

	# Share data solidity source code
	compiled_sol = compile_source(
		'''
		pragma solidity >=0.7.0 <0.9.0;

		contract shareData {
			string private place;
			
			string private date;
			
			address[] private robots;
			
			mapping (address => bool) private isRobot;

			struct Time {
				uint32 secs;
				uint32 nsecs;
			}

			struct Header {
				uint32 seq;
				Time stamp;
				string frame_id;
			}

			struct Data {
				int256 value;
				int256 variance;
			}

			struct Temperature {
				Header header;
				Data data;
			}

			struct Humidity {
				Header header;
				Data data;
			}

			struct PointCloud {
				string IPFS_Cid;
			}

			mapping (address => Temperature) temperature;
			mapping (address => Humidity) humidity;
			mapping (address => PointCloud) pointCloud;

			constructor(string memory _place, string memory _date, address[] memory _robots) {
				place = _place;
				date = _date;
				robots = _robots;
				for (uint256 i = 0; i < robots.length; i++) {
				    isRobot[robots[i]] = true;
				}
			}

			function updateTemperature(Temperature memory _temp) public {

				require(isRobot[msg.sender] == true, "sender is not a robot");

				temperature[msg.sender].header.seq = _temp.header.seq;
				temperature[msg.sender].header.frame_id = _temp.header.frame_id;
				temperature[msg.sender].header.stamp.secs = _temp.header.stamp.secs;
				temperature[msg.sender].header.stamp.nsecs = _temp.header.stamp.nsecs;
				temperature[msg.sender].data.value = _temp.data.value;
				temperature[msg.sender].data.variance = _temp.data.variance;

			}

			function updateHumidity(Humidity memory _hum) public {

				require(isRobot[msg.sender] == true, "sender is not a robot");

				humidity[msg.sender].header.seq = _hum.header.seq;
				humidity[msg.sender].header.frame_id = _hum.header.frame_id;
				humidity[msg.sender].header.stamp.secs = _hum.header.stamp.secs;
				humidity[msg.sender].header.stamp.nsecs = _hum.header.stamp.nsecs;
				humidity[msg.sender].data.value = _hum.data.value;
				humidity[msg.sender].data.variance = _hum.data.variance;

			}

			function updatePointCloud(string memory _IPFS_Cid) public {
				
				require(isRobot[msg.sender] == true, "sender is not a robot");

				pointCloud[msg.sender].IPFS_Cid = _IPFS_Cid;

			}

		}
		''',
		output_values=['abi', 'bin']
	)
	return compiled_sol

def deploy(w3, compiled_sol):
	# Retrieve the contract interface
	contract_id, contract_interface = compiled_sol.popitem()

	# Getting contract bytecode (bin)
	bytecode = contract_interface['bin']

	# Getting contract abi
	abi = contract_interface['abi']

	# Set account to send the transactions
	w3.eth.default_account = ''

	# Create contract object
	shareData = w3.eth.contract(abi=abi, bytecode=bytecode)

	# Submit the transaction that deploys the contract
	tx_hash = shareData.constructor().transact()

	# Wait for the transaction to be mined, and get the transaction receipt
	tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
	
	print(tx_receipt)

	# Update contract object to make transactions (interact)
	shareData = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
	
	return shareData

def main():
	# Compiling solidity contract
	compiled_sol = compile_sol()

	# Web3.py instance
	w3 = Web3(Web3.EthereumTesterProvider("http://127.0.0.1:8545"))

	# Deploying and getting contract
	shareData = deploy(w3, compiled_sol)
    
	# Interacting with contract function
	# tx_hash = shareData.functions.updateOdom(params).transact()
	# tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
	# shareData.functions.<test view function>().call()
	# print(tx_receipt)

if __name__ == "__main__":
    main()  

