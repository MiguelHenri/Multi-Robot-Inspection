// SPDX-License-Identifier: GPL-3.0
// Version of compiler
pragma solidity >=0.7.0 <0.9.0;

contract shareData {

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

    struct Vector3 {
        uint32 x;
        uint32 y;
        uint32 z;
    }

    struct Quaternion {
        uint32 x;
        uint32 y;
        uint32 z;
        uint32 w;
    }

    struct Pose {
        Vector3 position;
        Quaternion orientation;
        uint32[36] covariance;
    }

    struct Twist {
        Vector3 linear;
        Vector3 angular;
        uint32[36] covariance;
    }

    struct Odom {
        Header header;
        string child_frame_id;
        Pose pose;
        Twist twist;
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

    // string that stores the place of the inspection task
    string private place;

    // string that stores the date of the inspection task
    string private date;

    // variable that stores the inspector address
    address private inspector;

    // array that stores robots adresses
    address[] private robots;

    // mapping to check valid robot addresses
    mapping (address => bool) private isRobot;

    // public variables that store robots data
    mapping (address => Temperature) temperatureData;
    mapping (address => Humidity) humidityData;
    mapping (address => PointCloud) pointCloudData;
    mapping (address => Odom) odomData;

    constructor(string memory _place, string memory _date, address[] memory _robots) {
        place = _place;
        date = _date;
        robots = _robots;
        for (uint256 i = 0; i < robots.length; i++) {
            isRobot[robots[i]] = true;
        }
    }

    modifier checkRobot() {
        require(isRobot[msg.sender] == true, "sender is not a robot");
        _;
    }

    function updateTemperature(Temperature memory _temp) public checkRobot() {

        temperatureData[msg.sender].header.seq = _temp.header.seq;
        temperatureData[msg.sender].header.frame_id = _temp.header.frame_id;
        temperatureData[msg.sender].header.stamp.secs = _temp.header.stamp.secs;
        temperatureData[msg.sender].header.stamp.nsecs = _temp.header.stamp.nsecs;
        temperatureData[msg.sender].data.value = _temp.data.value;
        temperatureData[msg.sender].data.variance = _temp.data.variance;

    }

    function updateHumidity(Humidity memory _hum) public checkRobot() {

        humidityData[msg.sender].header.seq = _hum.header.seq;
        humidityData[msg.sender].header.frame_id = _hum.header.frame_id;
        humidityData[msg.sender].header.stamp.secs = _hum.header.stamp.secs;
        humidityData[msg.sender].header.stamp.nsecs = _hum.header.stamp.nsecs;
        humidityData[msg.sender].data.value = _hum.data.value;
        humidityData[msg.sender].data.variance = _hum.data.variance;

    }

    function updatePointCloud(string memory _IPFS_Cid) public checkRobot() {

        pointCloudData[msg.sender].IPFS_Cid = _IPFS_Cid;

    }

    function updateOdom(Odom memory _odom) public checkRobot() {

        odomData[msg.sender].header.seq = _odom.header.seq;
        odomData[msg.sender].header.stamp.secs = _odom.header.stamp.secs;
        odomData[msg.sender].header.stamp.nsecs = _odom.header.stamp.nsecs;
        odomData[msg.sender].header.frame_id = _odom.header.frame_id;

        odomData[msg.sender].child_frame_id = _odom.child_frame_id;

        odomData[msg.sender].pose.position.x = _odom.pose.position.x;
        odomData[msg.sender].pose.position.y = _odom.pose.position.y;
        odomData[msg.sender].pose.position.z = _odom.pose.position.z;

        odomData[msg.sender].pose.orientation.x = _odom.pose.orientation.x;
        odomData[msg.sender].pose.orientation.y = _odom.pose.orientation.y;
        odomData[msg.sender].pose.orientation.z = _odom.pose.orientation.z;
        odomData[msg.sender].pose.orientation.w = _odom.pose.orientation.w;

        for (uint256 i = 0; i < 36; i++) {
            odomData[msg.sender].pose.covariance[i] = _odom.pose.covariance[i];
        }

        odomData[msg.sender].twist.linear.x = _odom.twist.linear.x;
        odomData[msg.sender].twist.linear.y = _odom.twist.linear.y;
        odomData[msg.sender].twist.linear.z = _odom.twist.linear.z;

        odomData[msg.sender].twist.angular.x = _odom.twist.angular.x;
        odomData[msg.sender].twist.angular.y = _odom.twist.angular.y;
        odomData[msg.sender].twist.angular.z = _odom.twist.angular.z;

        for (uint256 i = 0; i < 36; i++) {
            odomData[msg.sender].twist.covariance[i] = _odom.twist.covariance[i];
        }
    }

}
