// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from amr_v4_msgs_srvs:msg/Sensor.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "amr_v4_msgs_srvs/msg/detail/sensor__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace amr_v4_msgs_srvs
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void Sensor_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) amr_v4_msgs_srvs::msg::Sensor(_init);
}

void Sensor_fini_function(void * message_memory)
{
  auto typed_message = static_cast<amr_v4_msgs_srvs::msg::Sensor *>(message_memory);
  typed_message->~Sensor();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember Sensor_message_member_array[1] = {
  {
    "status",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(amr_v4_msgs_srvs::msg::Sensor, status),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers Sensor_message_members = {
  "amr_v4_msgs_srvs::msg",  // message namespace
  "Sensor",  // message name
  1,  // number of fields
  sizeof(amr_v4_msgs_srvs::msg::Sensor),
  Sensor_message_member_array,  // message members
  Sensor_init_function,  // function to initialize message memory (memory has to be allocated)
  Sensor_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t Sensor_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &Sensor_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace amr_v4_msgs_srvs


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<amr_v4_msgs_srvs::msg::Sensor>()
{
  return &::amr_v4_msgs_srvs::msg::rosidl_typesupport_introspection_cpp::Sensor_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, amr_v4_msgs_srvs, msg, Sensor)() {
  return &::amr_v4_msgs_srvs::msg::rosidl_typesupport_introspection_cpp::Sensor_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
