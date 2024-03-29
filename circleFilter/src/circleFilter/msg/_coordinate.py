"""autogenerated by genmsg_py from coordinate.msg. Do not edit."""
import roslib.message
import struct


class coordinate(roslib.message.Message):
  _md5sum = "fa83e32d0048a022a60f823f2d5ea524"
  _type = "circleFilter/coordinate"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float64 x
float64 y
float64 theta
int8 beaconcount

"""
  __slots__ = ['x','y','theta','beaconcount']
  _slot_types = ['float64','float64','float64','int8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.
    
    The available fields are:
       x,y,theta,beaconcount
    
    @param args: complete set of field values, in .msg order
    @param kwds: use keyword arguments corresponding to message field names
    to set specific fields. 
    """
    if args or kwds:
      super(coordinate, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.x is None:
        self.x = 0.
      if self.y is None:
        self.y = 0.
      if self.theta is None:
        self.theta = 0.
      if self.beaconcount is None:
        self.beaconcount = 0
    else:
      self.x = 0.
      self.y = 0.
      self.theta = 0.
      self.beaconcount = 0

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
      buff.write(_struct_3db.pack(_x.x, _x.y, _x.theta, _x.beaconcount))
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
      end += 25
      (_x.x, _x.y, _x.theta, _x.beaconcount,) = _struct_3db.unpack(str[start:end])
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
      buff.write(_struct_3db.pack(_x.x, _x.y, _x.theta, _x.beaconcount))
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
      end += 25
      (_x.x, _x.y, _x.theta, _x.beaconcount,) = _struct_3db.unpack(str[start:end])
      return self
    except struct.error, e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

_struct_I = roslib.message.struct_I
_struct_3db = struct.Struct("<3db")
