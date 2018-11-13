var names = ["ONU", "UNICEF"]
var addresses = ["0x2963bb92cd3b5f1bd3447f55e409b9f1681cba5a", "0x7b7ef3882401022889730eee448bffcb92f290fc"]

var BetterFutureDonate = artifacts.require("./BetterFutureDonate.sol");
module.exports = function(deployer) {
    deployer.deploy(BetterFutureDonate);
};