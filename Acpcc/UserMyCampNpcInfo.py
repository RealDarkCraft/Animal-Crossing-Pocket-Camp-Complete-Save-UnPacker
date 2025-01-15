# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserMyCampNpcInfo(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserMyCampNpcInfo()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserMyCampNpcInfo(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserMyCampNpcInfo
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserMyCampNpcInfo
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserMyCampNpcInfo
    def NpcLabel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserMyCampNpcInfo
    def ActionLabel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserMyCampNpcInfo
    def ActionGroupLabel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserMyCampNpcInfo
    def VecRotateX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # UserMyCampNpcInfo
    def VecRotateY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # UserMyCampNpcInfo
    def VecRotateZ(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # UserMyCampNpcInfo
    def PositionX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # UserMyCampNpcInfo
    def PositionY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # UserMyCampNpcInfo
    def PositionZ(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # UserMyCampNpcInfo
    def JoinObjectId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserMyCampNpcInfo
    def JoinObjLabel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserMyCampNpcInfo
    def JoinObjActFileName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserMyCampNpcInfo
    def JoinObjUniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserMyCampNpcInfo
    def NpcLocatorKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserMyCampNpcInfo
    def WearTopsKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserMyCampNpcInfo
    def WearAcceKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserMyCampNpcInfo
    def WearCapKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserMyCampNpcInfo
    def WearDecoKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserMyCampNpcInfo
    def WearHandItemId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

def UserMyCampNpcInfoStart(builder):
    builder.StartObject(20)

def Start(builder):
    UserMyCampNpcInfoStart(builder)

def UserMyCampNpcInfoAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserMyCampNpcInfoAddId(builder, id)

def UserMyCampNpcInfoAddNpcLabel(builder, npcLabel):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(npcLabel), 0)

def AddNpcLabel(builder, npcLabel):
    UserMyCampNpcInfoAddNpcLabel(builder, npcLabel)

def UserMyCampNpcInfoAddActionLabel(builder, actionLabel):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(actionLabel), 0)

def AddActionLabel(builder, actionLabel):
    UserMyCampNpcInfoAddActionLabel(builder, actionLabel)

def UserMyCampNpcInfoAddActionGroupLabel(builder, actionGroupLabel):
    builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(actionGroupLabel), 0)

def AddActionGroupLabel(builder, actionGroupLabel):
    UserMyCampNpcInfoAddActionGroupLabel(builder, actionGroupLabel)

def UserMyCampNpcInfoAddVecRotateX(builder, vecRotateX):
    builder.PrependFloat32Slot(4, vecRotateX, 0.0)

def AddVecRotateX(builder, vecRotateX):
    UserMyCampNpcInfoAddVecRotateX(builder, vecRotateX)

def UserMyCampNpcInfoAddVecRotateY(builder, vecRotateY):
    builder.PrependFloat32Slot(5, vecRotateY, 0.0)

def AddVecRotateY(builder, vecRotateY):
    UserMyCampNpcInfoAddVecRotateY(builder, vecRotateY)

def UserMyCampNpcInfoAddVecRotateZ(builder, vecRotateZ):
    builder.PrependFloat32Slot(6, vecRotateZ, 0.0)

def AddVecRotateZ(builder, vecRotateZ):
    UserMyCampNpcInfoAddVecRotateZ(builder, vecRotateZ)

def UserMyCampNpcInfoAddPositionX(builder, positionX):
    builder.PrependFloat32Slot(7, positionX, 0.0)

def AddPositionX(builder, positionX):
    UserMyCampNpcInfoAddPositionX(builder, positionX)

def UserMyCampNpcInfoAddPositionY(builder, positionY):
    builder.PrependFloat32Slot(8, positionY, 0.0)

def AddPositionY(builder, positionY):
    UserMyCampNpcInfoAddPositionY(builder, positionY)

def UserMyCampNpcInfoAddPositionZ(builder, positionZ):
    builder.PrependFloat32Slot(9, positionZ, 0.0)

def AddPositionZ(builder, positionZ):
    UserMyCampNpcInfoAddPositionZ(builder, positionZ)

def UserMyCampNpcInfoAddJoinObjectId(builder, joinObjectId):
    builder.PrependInt32Slot(10, joinObjectId, 0)

def AddJoinObjectId(builder, joinObjectId):
    UserMyCampNpcInfoAddJoinObjectId(builder, joinObjectId)

def UserMyCampNpcInfoAddJoinObjLabel(builder, joinObjLabel):
    builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(joinObjLabel), 0)

def AddJoinObjLabel(builder, joinObjLabel):
    UserMyCampNpcInfoAddJoinObjLabel(builder, joinObjLabel)

def UserMyCampNpcInfoAddJoinObjActFileName(builder, joinObjActFileName):
    builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(joinObjActFileName), 0)

def AddJoinObjActFileName(builder, joinObjActFileName):
    UserMyCampNpcInfoAddJoinObjActFileName(builder, joinObjActFileName)

def UserMyCampNpcInfoAddJoinObjUniqueId(builder, joinObjUniqueId):
    builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(joinObjUniqueId), 0)

def AddJoinObjUniqueId(builder, joinObjUniqueId):
    UserMyCampNpcInfoAddJoinObjUniqueId(builder, joinObjUniqueId)

def UserMyCampNpcInfoAddNpcLocatorKey(builder, npcLocatorKey):
    builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(npcLocatorKey), 0)

def AddNpcLocatorKey(builder, npcLocatorKey):
    UserMyCampNpcInfoAddNpcLocatorKey(builder, npcLocatorKey)

def UserMyCampNpcInfoAddWearTopsKey(builder, wearTopsKey):
    builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(wearTopsKey), 0)

def AddWearTopsKey(builder, wearTopsKey):
    UserMyCampNpcInfoAddWearTopsKey(builder, wearTopsKey)

def UserMyCampNpcInfoAddWearAcceKey(builder, wearAcceKey):
    builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(wearAcceKey), 0)

def AddWearAcceKey(builder, wearAcceKey):
    UserMyCampNpcInfoAddWearAcceKey(builder, wearAcceKey)

def UserMyCampNpcInfoAddWearCapKey(builder, wearCapKey):
    builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(wearCapKey), 0)

def AddWearCapKey(builder, wearCapKey):
    UserMyCampNpcInfoAddWearCapKey(builder, wearCapKey)

def UserMyCampNpcInfoAddWearDecoKey(builder, wearDecoKey):
    builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(wearDecoKey), 0)

def AddWearDecoKey(builder, wearDecoKey):
    UserMyCampNpcInfoAddWearDecoKey(builder, wearDecoKey)

def UserMyCampNpcInfoAddWearHandItemId(builder, wearHandItemId):
    builder.PrependUint32Slot(19, wearHandItemId, 0)

def AddWearHandItemId(builder, wearHandItemId):
    UserMyCampNpcInfoAddWearHandItemId(builder, wearHandItemId)

def UserMyCampNpcInfoEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserMyCampNpcInfoEnd(builder)