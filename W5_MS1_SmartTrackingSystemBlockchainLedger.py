# ADE'T A3101 ( WINX CLUB)

# import necessary libraries
import pandas as pd
from web3 import Web3
import time


# Load IoT sensor data from CSV (Generated in Homework 1)
df = pd.read_csv("C:\\Users\\Ken\\Documents\\MMDC 2025\\healthcare_data.csv") # Replace with your CSV file path

# Display the first few rows
print(df.head())


# Connect to local blockchain
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))


# Verify connection
if web3.is_connected():
    print("✅ Connected to Ganache successfully!")
else:
    print("❌ Connection failed. Ensure Ganache is running.")


# Replace with actual contract address from Remix
contract_address = "0xDF2f2CDc8631F7B117D405677Ec9DAfFD348d995" # Replace with your contract address

# Paste the ABI from Remix
# Replace with your contract ABI
abi = [{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": False,
				"internalType": "string",
				"name": "patientID",
				"type": "string"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "timestamp",
				"type": "uint256"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "deviceId",
				"type": "string"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "dataType",
				"type": "string"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "dataValue",
				"type": "string"
			}
		],
		"name": "DataStored",
		"type": "event"
	},
	{
		"inputs": [],
		"name": "MAX_ENTRIES",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "dataRecords",
		"outputs": [
			{
				"internalType": "string",
				"name": "patientID",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "timestamp",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "deviceId",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "dataType",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "dataValue",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "index",
				"type": "uint256"
			}
		],
		"name": "getRecord",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getTotalRecords",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_patientID",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_deviceId",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_dataType",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_dataValue",
				"type": "string"
			}
		],
		"name": "storeData",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}]  


# Load the smart contract
contract = web3.eth.contract(address=contract_address, abi=abi)


# Set default sender (first account from Ganache)
web3.eth.default_account = web3.eth.accounts[0]
print(f"✅ Connected to Smart Contract at {contract_address}")


def send_iot_data(patient_id, device_id, data_type, data_value):
    """Sends IoT data to the deployed smart contract"""
    txn = contract.functions.storeData(patient_id, device_id, data_type, data_value).transact({
        'from': web3.eth.default_account,
        'gas': 3000000
    })
   
    receipt = web3.eth.wait_for_transaction_receipt(txn)
    print(f"✅ Data Stored: {data_type} - {data_value}, Txn Hash: {receipt.transactionHash.hex()}")

# Loop through the CSV file and send  each record to the smart contract
for _, row in df.iterrows():
    send_iot_data(str(row["patient_id"]), str(row["device_id"]), str(row["data_type"]), str(row["data_value"]))
    time.sleep(1)  # Delay to prevent flooding transactions


# Get total records stored in the contract
total_records = contract.functions.getTotalRecords().call()
print(f"Total IoT records stored: {total_records}")

# Retrieve the first stored record
record = contract.functions.getRecord(0).call()
print("First Stored Record:", record)
