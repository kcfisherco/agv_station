// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from amr_v4_msgs_srvs:msg/Sensor.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "amr_v4_msgs_srvs/msg/detail/sensor__rosidl_typesupport_introspection_c.h"
#include "amr_v4_msgs_srvs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "amr_v4_msgs_srvs/msg/detail/sensor__functions.h"
#include "amr_v4_msgs_srvs/msg/detail/sensor__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void Sensor__rosidl_typesupport_introspection_c__Sensor_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  amr_v4_msgs_srvs__msg__Sensor__init(message_memory);
}

void Sensor__rosidl_typesupport_introspection_c__Sensor_fini_function(void * message_memory)
{
  amr_v4_msgs_srvs__msg__Sensor__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember Sensor__rosidl_typesupport_introspection_c__Sensor_message_member_array[1] = {
  {
    "status",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(amr_v4_msgs_srvs__msg__Sensor, status),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Sensor__rosidl_typesupport_introspection_c__Sensor_message_members = {
  "amr_v4_msgs_srvs__msg",  // message namespace
  "Sensor",  // message name
  1,  // number of fields
  sizeof(amr_v4_msgs_srvs__msg__Sensor),
  Sensor__rosidl_typesupport_introspection_c__Sensor_message_member_array,  // message members
  Sensor__rosidl_typesupport_introspection_c__Sensor_init_function,  // function to initialize message memory (memory has to be allocated)
  Sensor__rosidl_typesupport_introspection_c__Sensor_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Sensor__rosidl_typesupport_introspection_c__Sensor_message_type_support_handle = {
  0,
  &Sensor__rosidl_typesupport_introspection_c__Sensor_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_amr_v4_msgs_srvs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, amr_v4_msgs_srvs, msg, Sensor)() {
  if (!Sensor__rosidl_typesupport_introspection_c__Sensor_message_type_support_handle.typesupport_identifier) {
    Sensor__rosidl_typesupport_introspection_c__Sensor_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Sensor__rosidl_typesupport_introspection_c__Sensor_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
