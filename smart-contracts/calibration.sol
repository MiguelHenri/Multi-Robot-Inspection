// SPDX-License-Identifier: GPL-3.0
// Version of compiler
pragma solidity >=0.7.0 <0.9.0;

contract calibration {

    // variable that stores owner address
    address private owner;

    // mapping to check valid robot addresses
    mapping (address => bool) private isRobot;

    // mapping to check valid inspectors addresses
    mapping (address => bool) private isInspector;

    // mapping to store calibration data
    mapping (address => string) private data;

    constructor(address[] memory _robots, address[] memory _inspectors) {
        owner = msg.sender;
        for (uint256 i = 0; i < _robots.length; i++) {
            isRobot[_robots[i]] = true;
        }
        for (uint256 i = 0; i < _inspectors.length; i++) {
            isInspector[_inspectors[i]] = true;
        }
    }

    function addRobot(address _robot) public {

        require (isRobot[_robot] == false, "already a valid robot");
        require (msg.sender == owner, "you are not the owner");

        // add valid robot
        isRobot[_robot] = true;

    }

    function removeRobot(address _robot) public {

        require (isRobot[_robot] == true, "not a valid robot");
        require (msg.sender == owner, "you are not the owner");

        // remove robot
        isRobot[_robot] = false;

    }

    function sendCalibrationData(address _robot, string memory _calibrationInfo) public {
        
        require (isRobot[_robot] == true, "it is not a valid robot");
        require (isInspector[msg.sender] == true, "not a valid inspector");

        data[_robot] = _calibrationInfo;

    }
}
