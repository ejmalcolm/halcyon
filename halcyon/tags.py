import pickle

with open('tags_file.pickle', 'rb') as handle:
    superlist = pickle.load(handle)
MATERIAL_TAGS = superlist[0]
STRUCTURE_TAGS = superlist[1]
FUNCTION_TAGS = superlist[2]

def add_tags(self, tags_list):
    for tag in tags_list:
        if tag in MATERIAL_TAGS:
            self.tags['Material'].append(tag)
        elif tag in STRUCTURE_TAGS:
            self.tags['Structure'].append(tag)
        elif tag in FUNCTION_TAGS:
            self.tags['Function'].append(tag)
        else:
            print("Tag '%s' does not exist" % tag)
            continue
    #check if any extra methods need to be added
    self.add_client_methods()
