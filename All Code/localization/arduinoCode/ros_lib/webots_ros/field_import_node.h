#ifndef _ROS_SERVICE_field_import_node_h
#define _ROS_SERVICE_field_import_node_h
#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace webots_ros
{

static const char FIELD_IMPORT_NODE[] = "webots_ros/field_import_node";

  class field_import_nodeRequest : public ros::Msg
  {
    public:
      typedef uint64_t _field_type;
      _field_type field;
      typedef int32_t _position_type;
      _position_type position;
      typedef const char* _filename_type;
      _filename_type filename;

    field_import_nodeRequest():
      field(0),
      position(0),
      filename("")
    {
    }

    virtual int serialize(unsigned char *outbuffer) const override
    {
      int offset = 0;
      *(outbuffer + offset + 0) = (this->field >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->field >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (this->field >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (this->field >> (8 * 3)) & 0xFF;
      *(outbuffer + offset + 4) = (this->field >> (8 * 4)) & 0xFF;
      *(outbuffer + offset + 5) = (this->field >> (8 * 5)) & 0xFF;
      *(outbuffer + offset + 6) = (this->field >> (8 * 6)) & 0xFF;
      *(outbuffer + offset + 7) = (this->field >> (8 * 7)) & 0xFF;
      offset += sizeof(this->field);
      union {
        int32_t real;
        uint32_t base;
      } u_position;
      u_position.real = this->position;
      *(outbuffer + offset + 0) = (u_position.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_position.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_position.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_position.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->position);
      uint32_t length_filename = strlen(this->filename);
      varToArr(outbuffer + offset, length_filename);
      offset += 4;
      memcpy(outbuffer + offset, this->filename, length_filename);
      offset += length_filename;
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer) override
    {
      int offset = 0;
      this->field =  ((uint64_t) (*(inbuffer + offset)));
      this->field |= ((uint64_t) (*(inbuffer + offset + 1))) << (8 * 1);
      this->field |= ((uint64_t) (*(inbuffer + offset + 2))) << (8 * 2);
      this->field |= ((uint64_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->field |= ((uint64_t) (*(inbuffer + offset + 4))) << (8 * 4);
      this->field |= ((uint64_t) (*(inbuffer + offset + 5))) << (8 * 5);
      this->field |= ((uint64_t) (*(inbuffer + offset + 6))) << (8 * 6);
      this->field |= ((uint64_t) (*(inbuffer + offset + 7))) << (8 * 7);
      offset += sizeof(this->field);
      union {
        int32_t real;
        uint32_t base;
      } u_position;
      u_position.base = 0;
      u_position.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_position.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_position.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_position.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->position = u_position.real;
      offset += sizeof(this->position);
      uint32_t length_filename;
      arrToVar(length_filename, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_filename; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_filename-1]=0;
      this->filename = (char *)(inbuffer + offset-1);
      offset += length_filename;
     return offset;
    }

    virtual const char * getType() override { return FIELD_IMPORT_NODE; };
    virtual const char * getMD5() override { return "ddb176ab5df764526d3b579fb7de9823"; };

  };

  class field_import_nodeResponse : public ros::Msg
  {
    public:
      typedef int32_t _success_type;
      _success_type success;

    field_import_nodeResponse():
      success(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const override
    {
      int offset = 0;
      union {
        int32_t real;
        uint32_t base;
      } u_success;
      u_success.real = this->success;
      *(outbuffer + offset + 0) = (u_success.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_success.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_success.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_success.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->success);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer) override
    {
      int offset = 0;
      union {
        int32_t real;
        uint32_t base;
      } u_success;
      u_success.base = 0;
      u_success.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_success.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_success.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_success.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->success = u_success.real;
      offset += sizeof(this->success);
     return offset;
    }

    virtual const char * getType() override { return FIELD_IMPORT_NODE; };
    virtual const char * getMD5() override { return "3c2bcf2ff0894cb3058b1bf4c8c4175a"; };

  };

  class field_import_node {
    public:
    typedef field_import_nodeRequest Request;
    typedef field_import_nodeResponse Response;
  };

}
#endif
