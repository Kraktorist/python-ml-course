import argparse
import json
import os
import tempfile
parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--val")
args = parser.parse_args()

if args.key:
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    if os.path.exists(storage_path):
        with open(storage_path, 'r') as f:
            config = json.load(f)
    else:
        config = {}
    value = config.setdefault(args.key,list())
    if args.val:
        value.append(args.val)
        config.update({args.key: value})
        with open(storage_path, 'w+') as f:  
            json.dump(config, f)
    else:
        print(', '.join(value))
    
    

