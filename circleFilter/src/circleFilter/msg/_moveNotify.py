"""autogenerated by genmsg_py from moveNotify.msg. Do not edit."""
import roslib.message
import struct


class moveNotify(roslib.message.Message):
  _md5sum = "5a98970fd37b53d278659d2ad11c00ce"
  _type = "circleFilter/moveNotify"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float64 linear
float64 rotation
float64 duration

"""
  __slots__ = ['linear','rotation','duration']
  _slot_types = ['float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.
    
    The available fields are:
       linear,rotation,duration
    
    @param args: complete set of field values, in .msg order
    @param kwds: use keyword arguments corresponding to message field names
    to set specific fields. 
    """
    if args or kwds:
      super(moveNotify, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.linear is None:
        self.linear = 0.
      if self.rotation is None:
        self.rotation = 0.
      if self.duration is None:
        self.duration = 0.
    else:
      self.linear = 0.
      self.rotation = 0.
      self.duration = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    @param buff: buffer
    @type  buff: StringIO
    """
    try:
      _x = self
      buff.write(_struct_3d.pack(_x.linear, _x.rotation, _x.duration))
    except struct.error, se: self._check_types(se)
    except TypeError, te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    @param str: byte array of serialized message
    @type  str: str
    """
    try:
      end = 0
      _x = self
      start = end
      end += 24
      (_x.linear, _x.rotation, _x.duration,) = _struct_3d.unpack(str[start:end])
      return self
    except struct.error, e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    @param buff: buffer
    @type  buff: StringIO
    @param numpy: numpy python module
    @type  numpy module
    """
    try:
      _x = self
      buff.write(_struct_3d.pack(_x.linear, _x.rotation, _x.duration))
    except struct.error, se: self._check_types(se)
    except TypeError, te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    @param str: byte array of serialized message
    @type  str: str
    @param numpy: numpy python module
    @type  numpy: module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 24
      (_x.linear, _x.rotation, _x.duration,) = _struct_3d.unpack(str[start:end])
      return self
    except struct.error, e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

_struct_I = roslib.message.struct_I
_struct_3d = struct.Struct("<3d")
