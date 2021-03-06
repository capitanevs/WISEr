# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:52:40 2020

Still to define if it will be kept

@author: Mike - Manfredda
"""
from enum import Enum as StandardEnum

#==============================================================================
#  Class Enum
#==============================================================================
class Enum(StandardEnum):
	'''
	Decorator (used as subclass) for making the comparisong between enums behave
	as we want.
	'''
	
	def __eq__(self, other):
		'''
		Useless here: it should be applied to any member
		'''
		if self.value == other.value:
			return True
		else:
			return False
		
#	@classmethod
#	def ListRoles(cls):
#		role_names = [member.value for role, member in cls.__members__.items()]
#		return role_names
#
#		
		
#==============================================================================
#  Class LogBuffer
#==============================================================================
class LogBuffer():
	'''
	Used to make any class capable of carrying debug information.
	Does not require intitialization.
	Example:
	a = LogBuffer()
	a._LogBuffer__Add('s')
	a._LogBuffer__Add('ss')
	a._LogBuffer__LogBuffer
	a._LogBuffer__Str
	a._LogBuffer__Print()
	'''
	def __init__(self):
		self.__LogBuffer = []

	def __Add(self,x : str):
		try:
			self.__LogBuffer.append(x)
		except:
			self.__init__()
			self._LogBuffer.append(x)
			
	
	@property
	def __Str(self):
		return '\n'.join(self.__LogBuffer)

	def __Print(self):
		print(self.__Str)	

#==============================================================================
#  Exists
#==============================================================================
def Exists(var):
	'''
	Check if a certain variable/object exists.
	'''
	try:
	   var
	   return True
	except:
		return False
	   # Do something.

def SetAttr(x, StrAttr : str, Value):
	
	TokList = StrAttr.split('.')
	if len(TokList) ==1:
		setattr(x, TokList[0], Value)
	
	elif len(TokList)>1:
		
		for Tok in TokList:
			y = getattr(x,Tok)
			GeldedTokList = '.'.join(TokList[1:])
			print(GeldedTokList)
			SetAttr(y,GeldedTokList, Value)

#==============================================================================
#  FUN: GetTheNotNone
#==============================================================================
def GetTheNotNone(ArgList):
	'''
	Return the first element which is not None.
	Used in certain case for parameter handling.
	It can be used ia try...except structure
	
	try:
		c = GetTheNotNone([a,b])
	except:
		c = a
		
	'''
	
	for _ in ArgList:
		if _ is not None:
			return _
	return None

#==============================================================================
#  FUN: IsArrayLike
#==============================================================================
def IsArrayLike(x):
	import numpy as np
	if type(x) == list:
		return True
	elif type(x) == np.ndarray:
		return True
	else:
		return False

#==============================================================================
#  FUN: IsValidArrayLike
#==============================================================================
def IsValidArray(x, Complex = False):
	'''
	Check that all the values of x are float, with no nan, no string, no inf
	
	'''
	import numpy as np
	if Complex:
		return np.any(np.iscomplex(x))
	else:
		return np.any(np.isreal((x)))


#==============================================================================
#  FUN: IsValidPythonName
#==============================================================================	
def IsValidPythonName(x):
	try:
		exec('%s = 42' % x)
		return True
	except:
		return False	
#==============================================================================
#  FUN: MergeDictionaries
#==============================================================================	
def IsValidPythonName(x):
	try:
		exec('%s = 42' % x)
		return True
	except:
		return False

#==============================================================================
#  Class: FrozenClass
#==============================================================================
class FrozenClass(object):
    __isfrozen = False
    def __setattr__(self, key, value):
        if self.__isfrozen and not hasattr(self, key):
            raise TypeError( "%r is a frozen class" % self )
        object.__setattr__(self, key, value)

    def _freeze(self):
        self.__isfrozen = True
		
#==============================================================================
#  Class: DataContainer
#==============================================================================
class DataContainer():
	'''

	DataContainer class is a struct-like object conceived for easy-to-use data
	storage. It is designed with user-friendliness in mind rather than performance.
	So it is more suitable for gathering many light-wight data rather than heavy-weight
	ones.

	Still to define
	--------

	The ListAttr function list only certain preferred data types.
	One should define this preferred data types in this class....

	At the present moment NO FILTER is included (th Preset argument is set to None)
	across the code

	See Also
	-----
	The function will have remarking ramifications in the development of WISErLab plotting
	and data storage tools.

	Example 1
	-----
	>>> D = DataContainer()
	D.Name = 'lambda'
	D.Value = 5e-9
	D.Unit = 'm'
	print(D)

	Example 2
	-----
	>>> D = DataContainer(Name = 'lambda', Value = 5e-9)
	print(D)

	Example 3 (Nesting)
	-----
	>>> D = DataContainer()
	D.x = 1
	D.y = DataContainer()
	D.y.yy = 10

	>>> Items = D._GetItems()
	print('\n'.join([str(_[0]) +':\t' + str(_[1]) for _ in Items]))

	SubItems = D._GetSubItems()
	print('\n'.join([str(_[0]) +':\t' + str(_[1]) for _ in SubItems]))

	print(D)

	'''


	#==============================
	#  FUN: __init__
	#==============================
	@staticmethod
	def _GetNonMagicAttributes():
		Attrs = dir(DataContainer)
		AttrList = []
		for Attr in Attrs:
			if Attr[0] != '_':
					AttrList.append(Attr)
		return AttrList


	#==============================
	#  FUN: __init__
	#==============================
	def __init__(self, **kwargs):

		Items = list( kwargs.items())

		#Loop on Parameter list
		for Item in Items:
			setattr(self,Item[0], Item[1]) # e.g. ParameterName = ParameterValue

#	#==============================
	#  FUN: __str__
	#==============================
	def __str__(self):
		'''
		return report in the form

		field1: value
		field2: value
		field3/subfield1: value

		Uses the GetSubItems function.
		'''

#		Values = [locals()[_] for _ in GetNonMagicAttributes()]
#		a = '\n'.join([str(_[0]) +':\t' + str(_[1]) for _ in Values])
		SubItems = self._GetSubItems()
		b =  '\n'.join([str(_[0]) +':\t' + str(_[1]) for _ in SubItems])
		a = ''
		return a + '\n' + b


	#==============================
	#  FUN: _GetItems
	#==============================
	def _GetItems(self):
		'''
		Returns a list of tuples in the form (attribute, object)
		'''
		Attr, Obj = ListAttr(self)

		TupleList = []
		for i, a in enumerate(Attr):
			o = Obj[i]
			TupleList.append((a,o))
		return TupleList

	#==============================
	#  FUN: _GetSubItems
	#==============================
	def _GetSubItems(self, TypeList = [None], Preset = None):
		'''
		Returns a list of tuples


		Philosophy:
		-------------
		Potentially, I want to get all the attributes (this is why TypeList
		and Preset are set to None, i.e. any type and no preset).
		However, the Recursion is locked only to DataContainer types.

		*Preset* will be locked outside the class, by the functions using
		this class for handling h5 files (which are somehow "friend functions").
		In that case, we want to be sure that only h5-compatible datatypes are selected.
		*Preset* behavior is defined inside the class, and it is "hardcoded".

		However, if for example you want to use other datatypes (because you
		are not using h5 files), you still have flexibility from the outside,
		with no need of modifing the inner code. This is provided by the
		*TypeList* parameter, where you can specify the types which are returned
		by the function.

		'''
		Attr, Obj = ListAttrRecursive(self, RecursionTypeList = [DataContainer])

		TupleList = []
		for i, a in enumerate(Attr):
			o = Obj[i]
			TupleList.append((a,o))
		return TupleList

	pass
a = DataContainer(x=1)


def InvertDictionary (Dictionary = dict() ):
	my_dict = Dictionary
	from collections import defaultdict
	my_inverted_dict = defaultdict(list)
	{my_inverted_dict[v].append(k) for k, v in my_dict.items()}
	return dict(my_inverted_dict)

#==============================================================================
#  FUN: ListAttributes
#==============================================================================
def ListAttr(x,
			 TypeList = None,
			 Preset = None,
			 ReturnObject = False,
			 IncludeCallable = False):
	'''

    Listra gli attributi di un oggetto (oggetto, classe, istanza, whatever)
    restituiendo l'elenco dei nomi e degli oggetti.,

    Type : serve per filtrare un tipo specifico.

    Parameters
    ------------------------
    x : whatever
        Can be any kind of python object. So for instance it can be either a TangoDevice object or a TangoDevice.Tango object

    TypeList : list
        List of type to include in the result list. Examples:
			*int*
			*[int]*
			*[int, float]*
			*[numpy.ndarray, int, str]*

		PresetTypeList : string
			Experimental: defines sets of commonly used types. The behavior oh this parameter
			is entirely defined within the code of the function. Currently implemented values:
				- 'math' : corresponds to TypeList = [int, float, numpy.ndarray]
				- 'mathstr' : corresponds to TypeList = [int, float, numpy.ndarray, str]

			Preset type are appended to TypeList.

	Motivation
	------------------------
	Created for interacting with DataContainer class and similar entities.
	This means that its logic favors "data" attributes rather than callable attributes.
	There is not a certain way to do that.
	IncludeCallable is a possible flag.
	Attributes starting with '__' are automatically excluded.
	For listing all the attributes, one should do explicit coding.

	If one wants to implement recursive search... still to be defined
	'''
	from numpy import ndarray
	Presets = {'math' :[int, float, ndarray],
					'math' :[int, float, str, ndarray]}

	# callable attributes are included (less common use)
	if IncludeCallable:
		strAttr = [iAttr for iAttr in dir(x) if not iAttr.startswith("__")]
	# callable attributes are excluded (more common use)
	else:
		strAttr = [iAttr for iAttr in dir(x) if not callable(getattr(x,iAttr)) and not iAttr.startswith("__")]

	# The function will return both attribute names and the respective object
	if ReturnObject:
		objAttr = [getattr(x,iAttr) for iAttr in strAttr]
	else:
		objAttr = None
	strAttrOut  = []
	objAttrOut  = []

	if Preset is not None:
		try:
			TypeList = Presets[Preset]
		except:
			pass

	# If Type is specified, it filters...
	if TypeList is not None:
     # force cast to list if not...
		TypeList = TypeList if type(TypeList)== list else [TypeList]
        # seleziona solo i tipi di TypeList
		for i, Obj in enumerate(objAttr):
			if any([type(Obj) == Type for Type in TypeList]):
				strAttrOut.append(strAttr[i])
				if ReturnObject:
					objAttrOut.append(objAttr[i])
	# Does not use filtering if not.
	else:

			strAttrOut = strAttr
			objAttrOut = objAttr

	if ReturnObject:
		return strAttrOut, objAttrOut
	else:
		return strAttrOut

#==============================================================================
#  FUN: ListAttributes
#==============================================================================
def ListAttrRecursive(x, TypeList = None, Preset = None,
					  RecursionTypeList = type, RecursionDepth = 3,
					  Sep = '/'):
	'''
	Magnificient and brilliant function that recursively lists the attributes of an object,
	inspecting also the child object whose type is specified in the RecursionTypeList.

	The function was designed in order to use classes as data container, and subsequently
	to use data container together with WISErLab functions for Saving HDF5 files.

	This is a typical example.
	>>>
		class DataCont():
			pass

		Pippo = DataCont()
		Pippo.x = 12
		Pippo.y = 120
		Pippo.w=DataCont()
		Pippo.w.ww = DataCont()
		Pippo.w.info = 'ciao'
		Pippo.w.ww.xx =  555

		a,b = ListAttrRecursive(Pippo, TypeList = None, Preset = None,   RecursionTypeList = DataCont, RecursionDepth = 3)

		print(a)


	'''

	# Force cast of data type
	if type(RecursionTypeList) is not list:
		RecursionTypeList = [RecursionTypeList]

	if type(TypeList) is not list:
		TypeList = TypeList

	AttrStr0, AttrObj0 = ListAttr(x, TypeList, Preset, True)

	for i, Obj in enumerate(AttrObj0):
		Str = AttrStr0[i]
		if any([type(Obj) == Type for Type in RecursionTypeList ]):

			AttrStr1, AttrObj1 = ListAttrRecursive(Obj, TypeList, Preset, RecursionTypeList)
			# pre-pend DataStr to each AttrStr1
			AttrStr1 = [Str + Sep + _ for _ in AttrStr1] # concatenate string
			AttrStr0 = AttrStr0 + AttrStr1  # append to list
			AttrObj0 = AttrObj0 + AttrObj1  # append to list

			del(AttrStr0[i])
			del(AttrObj0[i])

#
#	for i, DataObj in enumerate(DataAttrObj):
#		DataStr = DataAttrStr[i]
#		AttrStr1, AttrObj1 = ListAttr(DataObj, TypeList, Preset, ReturnObject = True)

	return AttrStr0, AttrObj0
	#force to list



#==============================================================================
#  FUN: ListClassProps
#==============================================================================
def ListClassProps(myClass, strOwnerClass = ''):
    strAttr = [iAttr for iAttr in dir(myClass) if not callable(iAttr) and not iAttr.startswith("__")]
    objAttr = [getattr(myClass,iAttr) for iAttr in strAttr]
    return strAttr, objAttr


#==============================================================================
#  FUN: ListClassPropsStr
#==============================================================================
def ListClassPropsStr(myClass, strOwnerClass = ''):
    strAttr = [iAttr for iAttr in dir(myClass) if not callable(iAttr) and not iAttr.startswith("__")]
    # objAttr = [getattr(myClass,iAttr) for iAttr in strAttr]
    return strAttr

#==============================================================================
#  FUN: ListClassObjects
#==============================================================================
def ListClassObjects(myClass, strOwnerClass = ''):
    strAttr = [iAttr for iAttr in dir(myClass) if not callable(iAttr) and not iAttr.startswith("__")]
    objAttr = [getattr(myClass,iAttr) for iAttr in strAttr]
    return objAttr


#SetAttr(a, 'b.c.d',  11)