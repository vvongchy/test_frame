import json
import os
import config
from config import CONFIGS_DIR



class WriteReadJson(object):
    """docstring for WriteReadJson"""

    def __init__(self, dir_):
        super(WriteReadJson, self).__init__()
        self.dir_ = dir_
        self.store = {}

    def load(self):
        with open(self.dir_, 'rb') as f:
            try:
                bitFileRead2Str = f.read().decode('utf-8')
                self.store = json.loads(bitFileRead2Str)
            except Exception as e:
                raise e
        return self.store

    def save(self, store):
        with open(self.dir_, 'wb') as f:
            jsonBitBuffer = json.dumps(store).encode('utf-8')
            f.write(jsonBitBuffer)


def safe_argvs():
    paras = os.listdir(CONFIGS_DIR)
    return [p.split('.')[0] for p in paras if p.split('.')[-1] == 'json']


SAFE_ARGVS = safe_argvs()


def update_config_by_json(module, json_dir):
    j = WriteReadJson(json_dir)
    d = j.load()
    [setattr(module, k.decode('utf-8'), v) for k, v in d.items()]


def update_config_by_name(name="static"):
    if name not in SAFE_ARGVS:
        raise ValueError("safe argvs error {} {}:\n".format(name, SAFE_ARGVS) + " ".join(SAFE_ARGVS))
    json_dir = CONFIGS_DIR + name + ".json"
    update_config_by_json(config, json_dir)
    str_dict_keys = [k for k in dir(config) if k[0].isupper()]
    str_dict = {k: config.__dict__[k] for k in str_dict_keys}
    strs = ["=>{}:{}".format(k, v) for k, v in str_dict.items()]
    strs_info = "\n" + json_dir + ":\n    " + "\n    ".join(strs)
    return strs_info
