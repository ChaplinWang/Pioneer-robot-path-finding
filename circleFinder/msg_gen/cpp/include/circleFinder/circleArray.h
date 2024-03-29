/* Auto-generated by genmsg_cpp for file /home/rcle271/ros_workspace/circleFinder/msg/circleArray.msg */
#ifndef CIRCLEFINDER_MESSAGE_CIRCLEARRAY_H
#define CIRCLEFINDER_MESSAGE_CIRCLEARRAY_H
#include <string>
#include <vector>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/message.h"
#include "ros/time.h"

#include "circleFinder/circleEntry.h"

namespace circleFinder
{
template <class ContainerAllocator>
struct circleArray_ : public ros::Message
{
  typedef circleArray_<ContainerAllocator> Type;

  circleArray_()
  : broadcastTime()
  , duration(0.0)
  , array()
  {
  }

  circleArray_(const ContainerAllocator& _alloc)
  : broadcastTime()
  , duration(0.0)
  , array(_alloc)
  {
  }

  typedef ros::Time _broadcastTime_type;
  ros::Time broadcastTime;

  typedef float _duration_type;
  float duration;

  typedef std::vector< ::circleFinder::circleEntry_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::circleFinder::circleEntry_<ContainerAllocator> >::other >  _array_type;
  std::vector< ::circleFinder::circleEntry_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::circleFinder::circleEntry_<ContainerAllocator> >::other >  array;


  ROS_DEPRECATED uint32_t get_array_size() const { return (uint32_t)array.size(); }
  ROS_DEPRECATED void set_array_size(uint32_t size) { array.resize((size_t)size); }
  ROS_DEPRECATED void get_array_vec(std::vector< ::circleFinder::circleEntry_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::circleFinder::circleEntry_<ContainerAllocator> >::other > & vec) const { vec = this->array; }
  ROS_DEPRECATED void set_array_vec(const std::vector< ::circleFinder::circleEntry_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::circleFinder::circleEntry_<ContainerAllocator> >::other > & vec) { this->array = vec; }
private:
  static const char* __s_getDataType_() { return "circleFinder/circleArray"; }
public:
  ROS_DEPRECATED static const std::string __s_getDataType() { return __s_getDataType_(); }

  ROS_DEPRECATED const std::string __getDataType() const { return __s_getDataType_(); }

private:
  static const char* __s_getMD5Sum_() { return "00508b03c8630a4b200fe9395178279d"; }
public:
  ROS_DEPRECATED static const std::string __s_getMD5Sum() { return __s_getMD5Sum_(); }

  ROS_DEPRECATED const std::string __getMD5Sum() const { return __s_getMD5Sum_(); }

private:
  static const char* __s_getMessageDefinition_() { return "time broadcastTime\n\
float32 duration\n\
circleEntry[] array\n\
\n\
================================================================================\n\
MSG: circleFinder/circleEntry\n\
float32 x\n\
float32 y\n\
float32 distance\n\
float32 theta\n\
float32 radius\n\
\n\
"; }
public:
  ROS_DEPRECATED static const std::string __s_getMessageDefinition() { return __s_getMessageDefinition_(); }

  ROS_DEPRECATED const std::string __getMessageDefinition() const { return __s_getMessageDefinition_(); }

  ROS_DEPRECATED virtual uint8_t *serialize(uint8_t *write_ptr, uint32_t seq) const
  {
    ros::serialization::OStream stream(write_ptr, 1000000000);
    ros::serialization::serialize(stream, broadcastTime);
    ros::serialization::serialize(stream, duration);
    ros::serialization::serialize(stream, array);
    return stream.getData();
  }

  ROS_DEPRECATED virtual uint8_t *deserialize(uint8_t *read_ptr)
  {
    ros::serialization::IStream stream(read_ptr, 1000000000);
    ros::serialization::deserialize(stream, broadcastTime);
    ros::serialization::deserialize(stream, duration);
    ros::serialization::deserialize(stream, array);
    return stream.getData();
  }

  ROS_DEPRECATED virtual uint32_t serializationLength() const
  {
    uint32_t size = 0;
    size += ros::serialization::serializationLength(broadcastTime);
    size += ros::serialization::serializationLength(duration);
    size += ros::serialization::serializationLength(array);
    return size;
  }

  typedef boost::shared_ptr< ::circleFinder::circleArray_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::circleFinder::circleArray_<ContainerAllocator>  const> ConstPtr;
}; // struct circleArray
typedef  ::circleFinder::circleArray_<std::allocator<void> > circleArray;

typedef boost::shared_ptr< ::circleFinder::circleArray> circleArrayPtr;
typedef boost::shared_ptr< ::circleFinder::circleArray const> circleArrayConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::circleFinder::circleArray_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::circleFinder::circleArray_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace circleFinder

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator>
struct MD5Sum< ::circleFinder::circleArray_<ContainerAllocator> > {
  static const char* value() 
  {
    return "00508b03c8630a4b200fe9395178279d";
  }

  static const char* value(const  ::circleFinder::circleArray_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x00508b03c8630a4bULL;
  static const uint64_t static_value2 = 0x200fe9395178279dULL;
};

template<class ContainerAllocator>
struct DataType< ::circleFinder::circleArray_<ContainerAllocator> > {
  static const char* value() 
  {
    return "circleFinder/circleArray";
  }

  static const char* value(const  ::circleFinder::circleArray_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::circleFinder::circleArray_<ContainerAllocator> > {
  static const char* value() 
  {
    return "time broadcastTime\n\
float32 duration\n\
circleEntry[] array\n\
\n\
================================================================================\n\
MSG: circleFinder/circleEntry\n\
float32 x\n\
float32 y\n\
float32 distance\n\
float32 theta\n\
float32 radius\n\
\n\
";
  }

  static const char* value(const  ::circleFinder::circleArray_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::circleFinder::circleArray_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.broadcastTime);
    stream.next(m.duration);
    stream.next(m.array);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct circleArray_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::circleFinder::circleArray_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::circleFinder::circleArray_<ContainerAllocator> & v) 
  {
    s << indent << "broadcastTime: ";
    Printer<ros::Time>::stream(s, indent + "  ", v.broadcastTime);
    s << indent << "duration: ";
    Printer<float>::stream(s, indent + "  ", v.duration);
    s << indent << "array[]" << std::endl;
    for (size_t i = 0; i < v.array.size(); ++i)
    {
      s << indent << "  array[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::circleFinder::circleEntry_<ContainerAllocator> >::stream(s, indent + "    ", v.array[i]);
    }
  }
};


} // namespace message_operations
} // namespace ros

#endif // CIRCLEFINDER_MESSAGE_CIRCLEARRAY_H

