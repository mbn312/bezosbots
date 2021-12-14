#ifndef _ROS_SERVICE_node_get_number_of_contact_points_h
#define _ROS_SERVICE_node_get_number_of_contact_points_h
#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace webots_ros
{

static const char NODE_GET_NUMBER_OF_CONTACT_POINTS[] = "webots_ros/node_get_number_of_contact_points";

  class node_get_number_of_contact_pointsRequest : public ros::Msg
  {
    public:
      typedef uint64_t _node_type;
      _node_type node;
      typedef bool _includeDescendants_type;
      _includeDescendants_type includeDescendants;

    node_get_number_of_contact_pointsRequest():
      node(0),
      includeDescendants(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const override
    {
      int offset = 0;
      *(outbuffer + offset + 0) = (this->node >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->node >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (this->node >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (this->node >> (8 * 3)) & 0xFF;
      *(outbuffer + offset + 4) = (this->node >> (8 * 4)) & 0xFF;
      *(outbuffer + offset + 5) = (this->node >> (8 * 5)) & 0xFF;
      *(outbuffer + offset + 6) = (this->node >> (8 * 6)) & 0xFF;
      *(outbuffer + offset + 7) = (this->node >> (8 * 7)) & 0xFF;
      offset += sizeof(this->node);
      union {
        bool real;
        uint8_t base;
      } u_includeDescendants;
      u_includeDescendants.real = this->includeDescendants;
      *(outbuffer + offset + 0) = (u_includeDescendants.base >> (8 * 0)) & 0xFF;
      offset += sizeof(this->includeDescendants);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer) override
    {
      int offset = 0;
      this->node =  ((uint64_t) (*(inbuffer + offset)));
      this->node |= ((uint64_t) (*(inbuffer + offset + 1))) << (8 * 1);
      this->node |= ((uint64_t) (*(inbuffer + offset + 2))) << (8 * 2);
      this->node |= ((uint64_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->node |= ((uint64_t) (*(inbuffer + offset + 4))) << (8 * 4);
      this->node |= ((uint64_t) (*(inbuffer + offset + 5))) << (8 * 5);
      this->node |= ((uint64_t) (*(inbuffer + offset + 6))) << (8 * 6);
      this->node |= ((uint64_t) (*(inbuffer + offset + 7))) << (8 * 7);
      offset += sizeof(this->node);
      union {
        bool real;
        uint8_t base;
      } u_includeDescendants;
      u_includeDescendants.base = 0;
      u_includeDescendants.base |= ((uint8_t) (*(inbuffer + offset + 0))) << (8 * 0);
      this->includeDescendants = u_includeDescendants.real;
      offset += sizeof(this->includeDescendants);
     return offset;
    }

    virtual const char * getType() override { return NODE_GET_NUMBER_OF_CONTACT_POINTS; };
    virtual const char * getMD5() override { return "b268dc6fc1acdb62a2e31eb22edd378d"; };

  };

  class node_get_number_of_contact_pointsResponse : public ros::Msg
  {
    public:
      typedef int32_t _numberOfContactPoints_type;
      _numberOfContactPoints_type numberOfContactPoints;

    node_get_number_of_contact_pointsResponse():
      numberOfContactPoints(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const override
    {
      int offset = 0;
      union {
        int32_t real;
        uint32_t base;
      } u_numberOfContactPoints;
      u_numberOfContactPoints.real = this->numberOfContactPoints;
      *(outbuffer + offset + 0) = (u_numberOfContactPoints.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_numberOfContactPoints.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_numberOfContactPoints.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_numberOfContactPoints.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->numberOfContactPoints);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer) override
    {
      int offset = 0;
      union {
        int32_t real;
        uint32_t base;
      } u_numberOfContactPoints;
      u_numberOfContactPoints.base = 0;
      u_numberOfContactPoints.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_numberOfContactPoints.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_numberOfContactPoints.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_numberOfContactPoints.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->numberOfContactPoints = u_numberOfContactPoints.real;
      offset += sizeof(this->numberOfContactPoints);
     return offset;
    }

    virtual const char * getType() override { return NODE_GET_NUMBER_OF_CONTACT_POINTS; };
    virtual const char * getMD5() override { return "2614f5acd0e58fdc4bc77a1795306071"; };

  };

  class node_get_number_of_contact_points {
    public:
    typedef node_get_number_of_contact_pointsRequest Request;
    typedef node_get_number_of_contact_pointsResponse Response;
  };

}
#endif
