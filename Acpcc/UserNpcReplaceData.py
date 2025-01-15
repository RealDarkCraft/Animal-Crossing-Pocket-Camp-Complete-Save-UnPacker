# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserNpcReplaceData(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserNpcReplaceData()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserNpcReplaceData(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserNpcReplaceData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserNpcReplaceData
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserNpcReplaceData
    def DailyReplaceCamp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # UserNpcReplaceData
    def DailyReplaceCottage(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # UserNpcReplaceData
    def NewDayCamp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # UserNpcReplaceData
    def NewDayCottage(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def UserNpcReplaceDataStart(builder):
    builder.StartObject(5)

def Start(builder):
    UserNpcReplaceDataStart(builder)

def UserNpcReplaceDataAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserNpcReplaceDataAddId(builder, id)

def UserNpcReplaceDataAddDailyReplaceCamp(builder, dailyReplaceCamp):
    builder.PrependBoolSlot(1, dailyReplaceCamp, 0)

def AddDailyReplaceCamp(builder, dailyReplaceCamp):
    UserNpcReplaceDataAddDailyReplaceCamp(builder, dailyReplaceCamp)

def UserNpcReplaceDataAddDailyReplaceCottage(builder, dailyReplaceCottage):
    builder.PrependBoolSlot(2, dailyReplaceCottage, 0)

def AddDailyReplaceCottage(builder, dailyReplaceCottage):
    UserNpcReplaceDataAddDailyReplaceCottage(builder, dailyReplaceCottage)

def UserNpcReplaceDataAddNewDayCamp(builder, newDayCamp):
    builder.PrependBoolSlot(3, newDayCamp, 0)

def AddNewDayCamp(builder, newDayCamp):
    UserNpcReplaceDataAddNewDayCamp(builder, newDayCamp)

def UserNpcReplaceDataAddNewDayCottage(builder, newDayCottage):
    builder.PrependBoolSlot(4, newDayCottage, 0)

def AddNewDayCottage(builder, newDayCottage):
    UserNpcReplaceDataAddNewDayCottage(builder, newDayCottage)

def UserNpcReplaceDataEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserNpcReplaceDataEnd(builder)