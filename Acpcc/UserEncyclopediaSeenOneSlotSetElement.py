# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserEncyclopediaSeenOneSlotSetElement(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserEncyclopediaSeenOneSlotSetElement()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserEncyclopediaSeenOneSlotSetElement(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserEncyclopediaSeenOneSlotSetElement
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserEncyclopediaSeenOneSlotSetElement
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserEncyclopediaSeenOneSlotSetElement
    def KeyName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserEncyclopediaSeenOneSlotSetElement
    def IsCheck(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # UserEncyclopediaSeenOneSlotSetElement
    def KeyId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

def UserEncyclopediaSeenOneSlotSetElementStart(builder):
    builder.StartObject(4)

def Start(builder):
    UserEncyclopediaSeenOneSlotSetElementStart(builder)

def UserEncyclopediaSeenOneSlotSetElementAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserEncyclopediaSeenOneSlotSetElementAddId(builder, id)

def UserEncyclopediaSeenOneSlotSetElementAddKeyName(builder, keyName):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(keyName), 0)

def AddKeyName(builder, keyName):
    UserEncyclopediaSeenOneSlotSetElementAddKeyName(builder, keyName)

def UserEncyclopediaSeenOneSlotSetElementAddIsCheck(builder, isCheck):
    builder.PrependBoolSlot(2, isCheck, 0)

def AddIsCheck(builder, isCheck):
    UserEncyclopediaSeenOneSlotSetElementAddIsCheck(builder, isCheck)

def UserEncyclopediaSeenOneSlotSetElementAddKeyId(builder, keyId):
    builder.PrependUint32Slot(3, keyId, 0)

def AddKeyId(builder, keyId):
    UserEncyclopediaSeenOneSlotSetElementAddKeyId(builder, keyId)

def UserEncyclopediaSeenOneSlotSetElementEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserEncyclopediaSeenOneSlotSetElementEnd(builder)