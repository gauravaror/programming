class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        maped_thing = {}
        for fol in folder:
            all_subpaths = fol.split('/')[1:]
            this_map = maped_thing
            for sp in all_subpaths:
                #print(this_map)
                if 'END' in this_map:
                    break
                else:
                    if not sp in this_map:
                        this_map[sp] = {}
                    this_map = this_map[sp]
            this_map.clear()
            this_map['END'] = True
        print(maped_thing)
        return_answer = []
        def decode_paths(answer, node):
            for i, j in node.items():
                if 'END' in node:
                    return_answer.append(answer)
                else:
                    decode_paths(answer + '/'+i, j)
        decode_paths('', maped_thing)
        return return_answer
