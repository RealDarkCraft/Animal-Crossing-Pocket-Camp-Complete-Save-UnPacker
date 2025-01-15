# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserOfflineCraft(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserOfflineCraft()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserOfflineCraft(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserOfflineCraft
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserOfflineCraft
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserOfflineCraft
    def IsDoneBoostDialog(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # UserOfflineCraft
    def BoostDegree(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def UserOfflineCraftStart(builder):
    builder.StartObject(3)

def Start(builder):
    UserOfflineCraftStart(builder)

def UserOfflineCraftAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserOfflineCraftAddId(builder, id)

def UserOfflineCraftAddIsDoneBoostDialog(builder, isDoneBoostDialog):
    builder.PrependBoolSlot(1, isDoneBoostDialog, 0)

def AddIsDoneBoostDialog(builder, isDoneBoostDialog):
    UserOfflineCraftAddIsDoneBoostDialog(builder, isDoneBoostDialog)

def UserOfflineCraftAddBoostDegree(builder, boostDegree):
    builder.PrependInt32Slot(2, boostDegree, 0)

def AddBoostDegree(builder, boostDegree):
    UserOfflineCraftAddBoostDegree(builder, boostDegree)

def UserOfflineCraftEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserOfflineCraftEnd(builder)