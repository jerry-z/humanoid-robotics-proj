// Auto-generated. Do not edit!

// (in-package map_annotator.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class UserAction {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.command = null;
      this.name = null;
      this.updated_name = null;
    }
    else {
      if (initObj.hasOwnProperty('command')) {
        this.command = initObj.command
      }
      else {
        this.command = '';
      }
      if (initObj.hasOwnProperty('name')) {
        this.name = initObj.name
      }
      else {
        this.name = '';
      }
      if (initObj.hasOwnProperty('updated_name')) {
        this.updated_name = initObj.updated_name
      }
      else {
        this.updated_name = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type UserAction
    // Serialize message field [command]
    bufferOffset = _serializer.string(obj.command, buffer, bufferOffset);
    // Serialize message field [name]
    bufferOffset = _serializer.string(obj.name, buffer, bufferOffset);
    // Serialize message field [updated_name]
    bufferOffset = _serializer.string(obj.updated_name, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type UserAction
    let len;
    let data = new UserAction(null);
    // Deserialize message field [command]
    data.command = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [name]
    data.name = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [updated_name]
    data.updated_name = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.command.length;
    length += object.name.length;
    length += object.updated_name.length;
    return length + 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'map_annotator/UserAction';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '02b53ace3ff4f0b2c6988ccd36fc2910';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string CREATE=create
    string DELETE=delete
    string GOTO=goto
    string RENAME=rename
    string command
    string name # The name of the pose the command applies to
    string updated_name # If command is RENAME, this is the new name of the pose
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new UserAction(null);
    if (msg.command !== undefined) {
      resolved.command = msg.command;
    }
    else {
      resolved.command = ''
    }

    if (msg.name !== undefined) {
      resolved.name = msg.name;
    }
    else {
      resolved.name = ''
    }

    if (msg.updated_name !== undefined) {
      resolved.updated_name = msg.updated_name;
    }
    else {
      resolved.updated_name = ''
    }

    return resolved;
    }
};

// Constants for message
UserAction.Constants = {
  CREATE: 'create',
  DELETE: 'delete',
  GOTO: 'goto',
  RENAME: 'rename',
}

module.exports = UserAction;
