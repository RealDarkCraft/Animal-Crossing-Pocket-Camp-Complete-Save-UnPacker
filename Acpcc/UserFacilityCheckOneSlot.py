# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserFacilityCheckOneSlot(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserFacilityCheckOneSlot()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserFacilityCheckOneSlot(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserFacilityCheckOneSlot
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserFacilityCheckOneSlot
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserFacilityCheckOneSlot
    def FacilityId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserFacilityCheckOneSlot
    def State(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

def UserFacilityCheckOneSlotStart(builder):
    builder.StartObject(3)

def Start(builder):
    UserFacilityCheckOneSlotStart(builder)

def UserFacilityCheckOneSlotAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserFacilityCheckOneSlotAddId(builder, id)

def UserFacilityCheckOneSlotAddFacilityId(builder, facilityId):
    builder.PrependUint32Slot(1, facilityId, 0)

def AddFacilityId(builder, facilityId):
    UserFacilityCheckOneSlotAddFacilityId(builder, facilityId)

def UserFacilityCheckOneSlotAddState(builder, state):
    builder.PrependUint8Slot(2, state, 0)

def AddState(builder, state):
    UserFacilityCheckOneSlotAddState(builder, state)

def UserFacilityCheckOneSlotEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserFacilityCheckOneSlotEnd(builder)
