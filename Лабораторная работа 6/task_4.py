import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', new_line='\n'):
    with open(filename) as f:
        heads = []
        res = []
        for index, line in enumerate(f):
            dict_ = {}
            if index == 0:
                l_str = line.strip(new_line)
                l_spl = l_str.split(delimiter)
                for word in l_spl:
                    heads.append(word)
            else:
                l_str = line.strip(new_line)
                l_spl = l_str.split(delimiter)
                for i in range(len(heads)):
                    dict_[heads[i]] = l_spl[i]
                res.append(dict_)
    return res


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
