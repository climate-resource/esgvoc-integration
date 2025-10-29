import json

from esgvoc.apps.jsg import json_schema_generator as jsg

json_schema = jsg.generate_json_schema("cmip7")
with open("stac-schema.json", "w") as fh:
    json.dump(json_schema, fh, indent=4, sort_keys=True)
    fh.write("\n")
