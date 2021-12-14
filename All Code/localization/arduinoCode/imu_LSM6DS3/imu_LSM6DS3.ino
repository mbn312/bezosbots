#include <Arduino_LSM6DS3.h>

#include <ros.h>
#include <localization/IMUData.h>

//Set up the ros node and publisher
localization::IMUData imu_msg;
ros::Publisher pub_imu("imu_data", &imu_msg);
ros::NodeHandle nh;

void setup() {
  if (!IMU.begin()) {
    nh.logfatal("IMU FAIL!");
    while (1);
  }

  nh.initNode();
  nh.advertise(pub_imu);
}

void loop() {
  if (IMU.accelerationAvailable()) {
    IMU.readAcceleration(imu_msg.accel_xdotdot, imu_msg.accel_ydotdot, imu_msg.accel_zdotdot);
  }
  if (IMU.gyroscopeAvailable()) {
    IMU.readGyroscope(imu_msg.gyro_xdot, imu_msg.gyro_ydot, imu_msg.gyro_zdot);
  }

  pub_imu.publish(&imu_msg);

  nh.spinOnce();
}
