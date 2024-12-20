# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserFootPrintInfo(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserFootPrintInfo()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserFootPrintInfo(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserFootPrintInfo
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserFootPrintInfo
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserFootPrintInfo
    def PlayerId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # UserFootPrintInfo
    def PlayerIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # UserFootPrintInfo
    def PlayerIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # UserFootPrintInfo
    def NotifyStatus(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserFootPrintInfo
    def FootPrintId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # UserFootPrintInfo
    def CheckedSendAnimalHistoryIds(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # UserFootPrintInfo
    def CheckedSendAnimalHistoryIdsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint64Flags, o)
        return 0

    # UserFootPrintInfo
    def CheckedSendAnimalHistoryIdsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # UserFootPrintInfo
    def CheckedSendAnimalHistoryIdsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

def UserFootPrintInfoStart(builder):
    builder.StartObject(5)

def Start(builder):
    UserFootPrintInfoStart(builder)

def UserFootPrintInfoAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserFootPrintInfoAddId(builder, id)

def UserFootPrintInfoAddPlayerId(builder, playerId):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(playerId), 0)

def AddPlayerId(builder, playerId):
    UserFootPrintInfoAddPlayerId(builder, playerId)

def UserFootPrintInfoStartPlayerIdVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartPlayerIdVector(builder, numElems):
    return UserFootPrintInfoStartPlayerIdVector(builder, numElems)

def UserFootPrintInfoAddNotifyStatus(builder, notifyStatus):
    builder.PrependInt32Slot(2, notifyStatus, 0)

def AddNotifyStatus(builder, notifyStatus):
    UserFootPrintInfoAddNotifyStatus(builder, notifyStatus)

def UserFootPrintInfoAddFootPrintId(builder, footPrintId):
    builder.PrependUint64Slot(3, footPrintId, 0)

def AddFootPrintId(builder, footPrintId):
    UserFootPrintInfoAddFootPrintId(builder, footPrintId)

def UserFootPrintInfoAddCheckedSendAnimalHistoryIds(builder, checkedSendAnimalHistoryIds):
    builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(checkedSendAnimalHistoryIds), 0)

def AddCheckedSendAnimalHistoryIds(builder, checkedSendAnimalHistoryIds):
    UserFootPrintInfoAddCheckedSendAnimalHistoryIds(builder, checkedSendAnimalHistoryIds)

def UserFootPrintInfoStartCheckedSendAnimalHistoryIdsVector(builder, numElems):
    return builder.StartVector(8, numElems, 8)

def StartCheckedSendAnimalHistoryIdsVector(builder, numElems):
    return UserFootPrintInfoStartCheckedSendAnimalHistoryIdsVector(builder, numElems)

def UserFootPrintInfoEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserFootPrintInfoEnd(builder)
