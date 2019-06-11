def to_lower(data):
    result = []
    for x in data:
        result.append(x.lower())
    return result
    
print(to_lower(['I','am','Deepa']))