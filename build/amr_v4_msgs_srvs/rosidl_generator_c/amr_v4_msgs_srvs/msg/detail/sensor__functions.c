// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from amr_v4_msgs_srvs:msg/Sensor.idl
// generated code does not contain a copyright notice
#include "amr_v4_msgs_srvs/msg/detail/sensor__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


bool
amr_v4_msgs_srvs__msg__Sensor__init(amr_v4_msgs_srvs__msg__Sensor * msg)
{
  if (!msg) {
    return false;
  }
  // status
  return true;
}

void
amr_v4_msgs_srvs__msg__Sensor__fini(amr_v4_msgs_srvs__msg__Sensor * msg)
{
  if (!msg) {
    return;
  }
  // status
}

bool
amr_v4_msgs_srvs__msg__Sensor__are_equal(const amr_v4_msgs_srvs__msg__Sensor * lhs, const amr_v4_msgs_srvs__msg__Sensor * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // status
  if (lhs->status != rhs->status) {
    return false;
  }
  return true;
}

bool
amr_v4_msgs_srvs__msg__Sensor__copy(
  const amr_v4_msgs_srvs__msg__Sensor * input,
  amr_v4_msgs_srvs__msg__Sensor * output)
{
  if (!input || !output) {
    return false;
  }
  // status
  output->status = input->status;
  return true;
}

amr_v4_msgs_srvs__msg__Sensor *
amr_v4_msgs_srvs__msg__Sensor__create()
{
  amr_v4_msgs_srvs__msg__Sensor * msg = (amr_v4_msgs_srvs__msg__Sensor *)malloc(sizeof(amr_v4_msgs_srvs__msg__Sensor));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(amr_v4_msgs_srvs__msg__Sensor));
  bool success = amr_v4_msgs_srvs__msg__Sensor__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
amr_v4_msgs_srvs__msg__Sensor__destroy(amr_v4_msgs_srvs__msg__Sensor * msg)
{
  if (msg) {
    amr_v4_msgs_srvs__msg__Sensor__fini(msg);
  }
  free(msg);
}


bool
amr_v4_msgs_srvs__msg__Sensor__Sequence__init(amr_v4_msgs_srvs__msg__Sensor__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  amr_v4_msgs_srvs__msg__Sensor * data = NULL;
  if (size) {
    data = (amr_v4_msgs_srvs__msg__Sensor *)calloc(size, sizeof(amr_v4_msgs_srvs__msg__Sensor));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = amr_v4_msgs_srvs__msg__Sensor__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        amr_v4_msgs_srvs__msg__Sensor__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
amr_v4_msgs_srvs__msg__Sensor__Sequence__fini(amr_v4_msgs_srvs__msg__Sensor__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      amr_v4_msgs_srvs__msg__Sensor__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

amr_v4_msgs_srvs__msg__Sensor__Sequence *
amr_v4_msgs_srvs__msg__Sensor__Sequence__create(size_t size)
{
  amr_v4_msgs_srvs__msg__Sensor__Sequence * array = (amr_v4_msgs_srvs__msg__Sensor__Sequence *)malloc(sizeof(amr_v4_msgs_srvs__msg__Sensor__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = amr_v4_msgs_srvs__msg__Sensor__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
amr_v4_msgs_srvs__msg__Sensor__Sequence__destroy(amr_v4_msgs_srvs__msg__Sensor__Sequence * array)
{
  if (array) {
    amr_v4_msgs_srvs__msg__Sensor__Sequence__fini(array);
  }
  free(array);
}

bool
amr_v4_msgs_srvs__msg__Sensor__Sequence__are_equal(const amr_v4_msgs_srvs__msg__Sensor__Sequence * lhs, const amr_v4_msgs_srvs__msg__Sensor__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!amr_v4_msgs_srvs__msg__Sensor__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
amr_v4_msgs_srvs__msg__Sensor__Sequence__copy(
  const amr_v4_msgs_srvs__msg__Sensor__Sequence * input,
  amr_v4_msgs_srvs__msg__Sensor__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(amr_v4_msgs_srvs__msg__Sensor);
    amr_v4_msgs_srvs__msg__Sensor * data =
      (amr_v4_msgs_srvs__msg__Sensor *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!amr_v4_msgs_srvs__msg__Sensor__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          amr_v4_msgs_srvs__msg__Sensor__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!amr_v4_msgs_srvs__msg__Sensor__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
