// SPDX-License-Identifier: GPL-3.0
// Version of compiler
pragma solidity >=0.7.0 <0.9.0;

contract calibration {

    // array that stores valid robots adresses
    address[] private robots;

    // mapping to check valid robot addresses
    mapping (address => bool) private isRobot;

    // mapping to store calibration data
    mapping (address => string) private data;

    // function called in contract deployment
    constructor(address[] memory _robots) {
        robots = _robots;
        for (uint256 i = 0; i < robots.length; i++) {
            isRobot[robots[i]] = true;
        }
    }

    function sendCalibrationData(address _robot, string memory _info) public {
        
        require(isRobot[_robot] == true, "it is not a valid robot");

        // require technician

        data[_robot] = _info;

    }

}