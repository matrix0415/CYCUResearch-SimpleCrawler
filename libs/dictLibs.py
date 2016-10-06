# -*- coding: utf-8-*-

def compareDictKeyBool(dic1, dic2):
	rs =False
	dict1Set =set(dic1)
	dict2Set =set(dic2)
	
	if len(dict1Set & dict2Set) is len(dict1Set | dict2Set):	# same key
		rs =True
	
	return rs
	
	
def compareDictKeyAndValBool(dic1, dic2):
	rs =True
	
	if compareDictKeyBool(dic1, dic2):
		for key in set(dic1):
			if dic1[key] is not dic2[key]:
				rs =False
				break;
				
	else:
		rs =False
		
	return rs
	