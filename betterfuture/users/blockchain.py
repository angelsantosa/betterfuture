import json

from web3 import Web3

ERC20_ABI = json.loads('[{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"transactions","outputs":[{"name":"user_uuid","type":"string"},{"name":"transaction_uuid","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_user_uuid","type":"string"},{"name":"_transaction_uuid","type":"string"}],"name":"addTransaction","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
