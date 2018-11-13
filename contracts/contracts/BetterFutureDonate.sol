pragma solidity ^0.4.2;

contract BetterFutureDonate{

    struct Transaction{
        string user_uuid;
        string transaction_uuid;
    }
    Transaction[] public transactions;

    function addTransaction(string _user_uuid, string _transaction_uuid) public {
        transactions.push(Transaction(_user_uuid, _transaction_uuid));
    }
    
}