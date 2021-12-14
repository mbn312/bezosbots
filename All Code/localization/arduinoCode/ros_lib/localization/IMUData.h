#ifndef _ROS_localization_IMUData_h
#define _ROS_localization_IMUData_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace localization
{

  class IMUData : public ros::Msg
  {
    public:
      typedef float _gyro_xdot_type;
      _gyro_xdot_type gyro_xdot;
      typedef float _gyro_ydot_type;
      _gyro_ydot_type gyro_ydot;
      typedef float _gyro_zdot_type;
      _gyro_zdot_type gyro_zdot;
      typedef float _accel_xdotdot_type;
      _accel_xdotdot_type accel_xdotdot;
      typedef float _accel_ydotdot_type;
      _accel_ydotdot_type accel_ydotdot;
      typedef float _accel_zdotdot_type;
      _accel_zdotdot_type accel_zdotdot;

    IMUData():
      gyro_xdot(0),
      gyro_ydot(0),
      gyro_zdot(0),
      accel_xdotdot(0),
      accel_ydotdot(0),
      accel_zdotdot(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const override
    {
      int offset = 0;
      union {
        float real;
        uint32_t base;
      } u_gyro_xdot;
      u_gyro_xdot.real = this->gyro_xdot;
      *(outbuffer + offset + 0) = (u_gyro_xdot.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_gyro_xdot.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_gyro_xdot.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_gyro_xdot.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->gyro_xdot);
      union {
        float real;
        uint32_t base;
      } u_gyro_ydot;
      u_gyro_ydot.real = this->gyro_ydot;
      *(outbuffer + offset + 0) = (u_gyro_ydot.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_gyro_ydot.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_gyro_ydot.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_gyro_ydot.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->gyro_ydot);
      union {
        float real;
        uint32_t base;
      } u_gyro_zdot;
      u_gyro_zdot.real = this->gyro_zdot;
      *(outbuffer + offset + 0) = (u_gyro_zdot.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_gyro_zdot.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_gyro_zdot.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_gyro_zdot.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->gyro_zdot);
      union {
        float real;
        uint32_t base;
      } u_accel_xdotdot;
      u_accel_xdotdot.real = this->accel_xdotdot;
      *(outbuffer + offset + 0) = (u_accel_xdotdot.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_accel_xdotdot.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_accel_xdotdot.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_accel_xdotdot.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->accel_xdotdot);
      union {
        float real;
        uint32_t base;
      } u_accel_ydotdot;
      u_accel_ydotdot.real = this->accel_ydotdot;
      *(outbuffer + offset + 0) = (u_accel_ydotdot.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_accel_ydotdot.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_accel_ydotdot.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_accel_ydotdot.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->accel_ydotdot);
      union {
        float real;
        uint32_t base;
      } u_accel_zdotdot;
      u_accel_zdotdot.real = this->accel_zdotdot;
      *(outbuffer + offset + 0) = (u_accel_zdotdot.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_accel_zdotdot.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_accel_zdotdot.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_accel_zdotdot.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->accel_zdotdot);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer) override
    {
      int offset = 0;
      union {
        float real;
        uint32_t base;
      } u_gyro_xdot;
      u_gyro_xdot.base = 0;
      u_gyro_xdot.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_gyro_xdot.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_gyro_xdot.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_gyro_xdot.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->gyro_xdot = u_gyro_xdot.real;
      offset += sizeof(this->gyro_xdot);
      union {
        float real;
        uint32_t base;
      } u_gyro_ydot;
      u_gyro_ydot.base = 0;
      u_gyro_ydot.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_gyro_ydot.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_gyro_ydot.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_gyro_ydot.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->gyro_ydot = u_gyro_ydot.real;
      offset += sizeof(this->gyro_ydot);
      union {
        float real;
        uint32_t base;
      } u_gyro_zdot;
      u_gyro_zdot.base = 0;
      u_gyro_zdot.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_gyro_zdot.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_gyro_zdot.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_gyro_zdot.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->gyro_zdot = u_gyro_zdot.real;
      offset += sizeof(this->gyro_zdot);
      union {
        float real;
        uint32_t base;
      } u_accel_xdotdot;
      u_accel_xdotdot.base = 0;
      u_accel_xdotdot.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_accel_xdotdot.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_accel_xdotdot.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_accel_xdotdot.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->accel_xdotdot = u_accel_xdotdot.real;
      offset += sizeof(this->accel_xdotdot);
      union {
        float real;
        uint32_t base;
      } u_accel_ydotdot;
      u_accel_ydotdot.base = 0;
      u_accel_ydotdot.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_accel_ydotdot.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_accel_ydotdot.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_accel_ydotdot.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->accel_ydotdot = u_accel_ydotdot.real;
      offset += sizeof(this->accel_ydotdot);
      union {
        float real;
        uint32_t base;
      } u_accel_zdotdot;
      u_accel_zdotdot.base = 0;
      u_accel_zdotdot.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_accel_zdotdot.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_accel_zdotdot.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_accel_zdotdot.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->accel_zdotdot = u_accel_zdotdot.real;
      offset += sizeof(this->accel_zdotdot);
     return offset;
    }

    virtual const char * getType() override { return "localization/IMUData"; };
    virtual const char * getMD5() override { return "b20a1fe10123a54b8d05841512909482"; };

  };

}
#endif
