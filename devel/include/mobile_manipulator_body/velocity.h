// Generated by gencpp from file mobile_manipulator_body/velocity.msg
// DO NOT EDIT!


#ifndef MOBILE_MANIPULATOR_BODY_MESSAGE_VELOCITY_H
#define MOBILE_MANIPULATOR_BODY_MESSAGE_VELOCITY_H

#include <ros/service_traits.h>


#include <mobile_manipulator_body/velocityRequest.h>
#include <mobile_manipulator_body/velocityResponse.h>


namespace mobile_manipulator_body
{

struct velocity
{

typedef velocityRequest Request;
typedef velocityResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct velocity
} // namespace mobile_manipulator_body


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::mobile_manipulator_body::velocity > {
  static const char* value()
  {
    return "4a43c3133b1d7fcbde17a0d788417bc1";
  }

  static const char* value(const ::mobile_manipulator_body::velocity&) { return value(); }
};

template<>
struct DataType< ::mobile_manipulator_body::velocity > {
  static const char* value()
  {
    return "mobile_manipulator_body/velocity";
  }

  static const char* value(const ::mobile_manipulator_body::velocity&) { return value(); }
};


// service_traits::MD5Sum< ::mobile_manipulator_body::velocityRequest> should match
// service_traits::MD5Sum< ::mobile_manipulator_body::velocity >
template<>
struct MD5Sum< ::mobile_manipulator_body::velocityRequest>
{
  static const char* value()
  {
    return MD5Sum< ::mobile_manipulator_body::velocity >::value();
  }
  static const char* value(const ::mobile_manipulator_body::velocityRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::mobile_manipulator_body::velocityRequest> should match
// service_traits::DataType< ::mobile_manipulator_body::velocity >
template<>
struct DataType< ::mobile_manipulator_body::velocityRequest>
{
  static const char* value()
  {
    return DataType< ::mobile_manipulator_body::velocity >::value();
  }
  static const char* value(const ::mobile_manipulator_body::velocityRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::mobile_manipulator_body::velocityResponse> should match
// service_traits::MD5Sum< ::mobile_manipulator_body::velocity >
template<>
struct MD5Sum< ::mobile_manipulator_body::velocityResponse>
{
  static const char* value()
  {
    return MD5Sum< ::mobile_manipulator_body::velocity >::value();
  }
  static const char* value(const ::mobile_manipulator_body::velocityResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::mobile_manipulator_body::velocityResponse> should match
// service_traits::DataType< ::mobile_manipulator_body::velocity >
template<>
struct DataType< ::mobile_manipulator_body::velocityResponse>
{
  static const char* value()
  {
    return DataType< ::mobile_manipulator_body::velocity >::value();
  }
  static const char* value(const ::mobile_manipulator_body::velocityResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // MOBILE_MANIPULATOR_BODY_MESSAGE_VELOCITY_H