// Auto-generated. Do not edit!

// (in-package mobile_manipulator_body.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class velocityRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.sec_int = null;
    }
    else {
      if (initObj.hasOwnProperty('sec_int')) {
        this.sec_int = initObj.sec_int
      }
      else {
        this.sec_int = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type velocityRequest
    // Serialize message field [sec_int]
    bufferOffset = _serializer.int32(obj.sec_int, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type velocityRequest
    let len;
    let data = new velocityRequest(null);
    // Deserialize message field [sec_int]
    data.sec_int = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'mobile_manipulator_body/velocityRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '635e9bf46a8b2b500c4b25026d911da1';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 sec_int
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new velocityRequest(null);
    if (msg.sec_int !== undefined) {
      resolved.sec_int = msg.sec_int;
    }
    else {
      resolved.sec_int = 0
    }

    return resolved;
    }
};

class velocityResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.msg = null;
    }
    else {
      if (initObj.hasOwnProperty('msg')) {
        this.msg = initObj.msg
      }
      else {
        this.msg = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type velocityResponse
    // Serialize message field [msg]
    bufferOffset = _serializer.string(obj.msg, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type velocityResponse
    let len;
    let data = new velocityResponse(null);
    // Deserialize message field [msg]
    data.msg = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.msg);
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'mobile_manipulator_body/velocityResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '7d96ed730776804754140b85e64c862e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string msg
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new velocityResponse(null);
    if (msg.msg !== undefined) {
      resolved.msg = msg.msg;
    }
    else {
      resolved.msg = ''
    }

    return resolved;
    }
};

module.exports = {
  Request: velocityRequest,
  Response: velocityResponse,
  md5sum() { return '4a43c3133b1d7fcbde17a0d788417bc1'; },
  datatype() { return 'mobile_manipulator_body/velocity'; }
};
