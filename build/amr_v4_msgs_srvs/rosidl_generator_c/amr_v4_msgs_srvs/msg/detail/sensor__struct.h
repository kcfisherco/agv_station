// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from amr_v4_msgs_srvs:msg/Sensor.idl
// generated code does not contain a copyright notice

#ifndef AMR_V4_MSGS_SRVS__MSG__DETAIL__SENSOR__STRUCT_H_
#define AMR_V4_MSGS_SRVS__MSG__DETAIL__SENSOR__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/Sensor in the package amr_v4_msgs_srvs.
typedef struct amr_v4_msgs_srvs__msg__Sensor
{
  bool status;
} amr_v4_msgs_srvs__msg__Sensor;

// Struct for a sequence of amr_v4_msgs_srvs__msg__Sensor.
typedef struct amr_v4_msgs_srvs__msg__Sensor__Sequence
{
  amr_v4_msgs_srvs__msg__Sensor * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} amr_v4_msgs_srvs__msg__Sensor__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AMR_V4_MSGS_SRVS__MSG__DETAIL__SENSOR__STRUCT_H_
