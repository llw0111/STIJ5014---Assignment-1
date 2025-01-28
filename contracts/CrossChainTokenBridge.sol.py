// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract CrossChainTokenBridge {
    address public admin;
    mapping(address => uint256) public lockedFunds;
    event TokensLocked(address indexed user, uint256 amount, string targetChain);
    event TokensUnlocked(address indexed user, uint256 amount);

    constructor() {
        admin = msg.sender;
    }

    function lockTokens(uint256 _amount, string memory _targetChain) external payable {
        require(msg.value == _amount, "Insufficient funds provided");
        lockedFunds[msg.sender] += _amount;
        emit TokensLocked(msg.sender, _amount, _targetChain);
    }

    function unlockTokens(address _user, uint256 _amount) external {
        require(msg.sender == admin, "Only admin can unlock tokens");
        require(lockedFunds[_user] >= _amount, "Insufficient locked funds");
        
        lockedFunds[_user] -= _amount;
        payable(_user).transfer(_amount);
        emit TokensUnlocked(_user, _amount);
    }
}