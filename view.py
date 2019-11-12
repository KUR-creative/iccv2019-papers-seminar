from pprint import pprint
import yaml
with open('summary.yml') as inp:
    pprint(yaml.load(inp))
