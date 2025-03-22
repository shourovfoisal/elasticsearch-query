import json
from elasticsearchquerygenerator.elasticsearchquerygenerator import ElasticSearchQuery

def main():
    helper = ElasticSearchQuery(size=100, BucketName="MyBuckets")
    print(json.dumps(helper.baseQuery, indent=3))

main()

'''
Use the generated code like this:

GET <index_name>/_search
<generated_code>

'''