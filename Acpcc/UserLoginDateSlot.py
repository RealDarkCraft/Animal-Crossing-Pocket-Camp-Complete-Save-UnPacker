# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserLoginDateSlot(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserLoginDateSlot()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserLoginDateSlot(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserLoginDateSlot
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserLoginDateSlot
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserLoginDateSlot
    def LoginTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def UserLoginDateSlotStart(builder):
    builder.StartObject(2)

def Start(builder):
    UserLoginDateSlotStart(builder)

def UserLoginDateSlotAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserLoginDateSlotAddId(builder, id)

def UserLoginDateSlotAddLoginTime(builder, loginTime):
    builder.PrependInt64Slot(1, loginTime, 0)

def AddLoginTime(builder, loginTime):
    UserLoginDateSlotAddLoginTime(builder, loginTime)

def UserLoginDateSlotEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserLoginDateSlotEnd(builder)