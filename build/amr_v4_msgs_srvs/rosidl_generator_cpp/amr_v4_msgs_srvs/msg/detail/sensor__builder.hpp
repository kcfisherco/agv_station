// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from amr_v4_msgs_srvs:msg/Sensor.idl
// generated code does not contain a copyright notice

#ifndef AMR_V4_MSGS_SRVS__MSG__DETAIL__SENSOR__BUILDER_HPP_
#define AMR_V4_MSGS_SRVS__MSG__DETAIL__SENSOR__BUILDER_HPP_

#include "amr_v4_msgs_srvs/msg/detail/sensor__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace amr_v4_msgs_srvs
{

namespace msg
{

namespace builder
{

class Init_Sensor_status
{
public:
  Init_Sensor_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::amr_v4_msgs_srvs::msg::Sensor status(::amr_v4_msgs_srvs::msg::Sensor::_status_type arg)
  {
    msg_.status = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_v4_msgs_srvs::msg::Sensor msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_v4_msgs_srvs::msg::Sensor>()
{
  return amr_v4_msgs_srvs::msg::builder::Init_Sensor_status();
}

}  // namespace amr_v4_msgs_srvs

#endif  // AMR_V4_MSGS_SRVS__MSG__DETAIL__SENSOR__BUILDER_HPP_
