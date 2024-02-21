from data_structures.hashtable import Hashtable

def left_join(synonyms, antonyms):
  
    result = []
    
    for key in synonyms.keys():
        synonym_value = synonyms.get(key)
        antonym_value = antonyms.get(key)
        
        if antonym_value is not None:
            result.append([key, synonym_value, antonym_value])
        else:
            result.append([key, synonym_value, "None"])  
    
    return sorted(result)  
