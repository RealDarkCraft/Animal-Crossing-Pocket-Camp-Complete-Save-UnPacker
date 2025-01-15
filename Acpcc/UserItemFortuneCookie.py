# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserItemFortuneCookie(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserItemFortuneCookie()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserItemFortuneCookie(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserItemFortuneCookie
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserItemFortuneCookie
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserItemFortuneCookie
    def Guid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserItemFortuneCookie
    def Route(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserItemFortuneCookie
    def LottedItemIds(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # UserItemFortuneCookie
    def LottedItemIdsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint32Flags, o)
        return 0

    # UserItemFortuneCookie
    def LottedItemIdsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # UserItemFortuneCookie
    def LottedItemIdsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # UserItemFortuneCookie
    def LottedItemQuantities(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # UserItemFortuneCookie
    def LottedItemQuantitiesAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # UserItemFortuneCookie
    def LottedItemQuantitiesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # UserItemFortuneCookie
    def LottedItemQuantitiesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

    # UserItemFortuneCookie
    def BonusItemId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserItemFortuneCookie
    def BonusItemQuantity(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # UserItemFortuneCookie
    def OmenMessageId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserItemFortuneCookie
    def EatingId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

def UserItemFortuneCookieStart(builder):
    builder.StartObject(9)

def Start(builder):
    UserItemFortuneCookieStart(builder)

def UserItemFortuneCookieAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserItemFortuneCookieAddId(builder, id)

def UserItemFortuneCookieAddGuid(builder, guid):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(guid), 0)

def AddGuid(builder, guid):
    UserItemFortuneCookieAddGuid(builder, guid)

def UserItemFortuneCookieAddRoute(builder, route):
    builder.PrependInt32Slot(2, route, 0)

def AddRoute(builder, route):
    UserItemFortuneCookieAddRoute(builder, route)

def UserItemFortuneCookieAddLottedItemIds(builder, lottedItemIds):
    builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(lottedItemIds), 0)

def AddLottedItemIds(builder, lottedItemIds):
    UserItemFortuneCookieAddLottedItemIds(builder, lottedItemIds)

def UserItemFortuneCookieStartLottedItemIdsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartLottedItemIdsVector(builder, numElems):
    return UserItemFortuneCookieStartLottedItemIdsVector(builder, numElems)

def UserItemFortuneCookieAddLottedItemQuantities(builder, lottedItemQuantities):
    builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(lottedItemQuantities), 0)

def AddLottedItemQuantities(builder, lottedItemQuantities):
    UserItemFortuneCookieAddLottedItemQuantities(builder, lottedItemQuantities)

def UserItemFortuneCookieStartLottedItemQuantitiesVector(builder, numElems):
    return builder.StartVector(1, numElems, 1)

def StartLottedItemQuantitiesVector(builder, numElems):
    return UserItemFortuneCookieStartLottedItemQuantitiesVector(builder, numElems)

def UserItemFortuneCookieAddBonusItemId(builder, bonusItemId):
    builder.PrependUint32Slot(5, bonusItemId, 0)

def AddBonusItemId(builder, bonusItemId):
    UserItemFortuneCookieAddBonusItemId(builder, bonusItemId)

def UserItemFortuneCookieAddBonusItemQuantity(builder, bonusItemQuantity):
    builder.PrependUint8Slot(6, bonusItemQuantity, 0)

def AddBonusItemQuantity(builder, bonusItemQuantity):
    UserItemFortuneCookieAddBonusItemQuantity(builder, bonusItemQuantity)

def UserItemFortuneCookieAddOmenMessageId(builder, omenMessageId):
    builder.PrependUint32Slot(7, omenMessageId, 0)

def AddOmenMessageId(builder, omenMessageId):
    UserItemFortuneCookieAddOmenMessageId(builder, omenMessageId)

def UserItemFortuneCookieAddEatingId(builder, eatingId):
    builder.PrependUint32Slot(8, eatingId, 0)

def AddEatingId(builder, eatingId):
    UserItemFortuneCookieAddEatingId(builder, eatingId)

def UserItemFortuneCookieEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserItemFortuneCookieEnd(builder)