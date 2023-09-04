// SPDX-License-Identifier: GPL-3.0
// Version of compiler
pragma solidity >=0.7.0 <0.9.0;

contract shareData {

    // string that stores the place of the inspection task
    string private place;

    // string that stores the date of the inspection task
    string private date;

    // array that stores robots addresses
    address[] private robots;

    // mapping to check valid robot addresses
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

    // public variables that store robots data
    mapping (address => Temperature) temperature;
    mapping (address => Humidity) humidity;
    mapping (address => PointCloud) pointCloud;

    // function called in contract deployment
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

        pointCloud[msg.sender]f.IPFS_Cid = _IPFS_Cid;

    }

}