'''
26.05.11

[user1@mgmt test05_dynamo_init]$ aws dynamodb scan --table-name terraform-lo
ck
{
    "Items": [],
    "Count": 0,
    "ScannedCount": 0,
    "ConsumedCapacity": null
}

[user1@mgmt test06_dynamodb]$ aws dynamodb put-item \
> --table-name members \
> --item '{"num":{"N":"1"},"name":{"S":"kim"}}'
[user1@mgmt test06_dynamodb]$ aws dynamodb scan --table-name members
{
    "Items": [
        {
            "name": {
                "S": "kim"
            },
            "num": {
                "N": "1"
            }
        }
    ],
    "Count": 1,
    "ScannedCount": 1,
    "ConsumedCapacity": null
}

[user1@mgmt test06_dynamodb]$ aws dynamodb get-item \
> --table-name members \
> --key '{"num":{"N":"1"}}'
{
    "Item": {
        "name": {
            "S": "kim"
        },
        "num": {
            "N": "1"
        }
    }
}

[user1@mgmt test06_dynamodb]$ aws dynamodb delete-item \
> --table-name members \
> --key '{"num":{"N":"1"}}'
[user1@mgmt test06_dynamodb]$ aws dynamodb scan --table-name members
{
    "Items": [
        {
            "name": {
                "S": "park"
            },
            "num": {
                "N": "2"
            }
        }
    ],
    "Count": 1,
    "ScannedCount": 1,
    "ConsumedCapacity": null
}

partiQL: dynamodb 클라이언트 프로그램에서 익숙한 QL언어처럼 사용할수있다.
NoSQL Workbench: aws에서 제공하는 클라이언트 프로그램
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.settingup.html

INSERT INTO "members" VALUE {
	'num':5,
    'name':'cat',
    'info':{'height':100, 'weight':50, 'nick':'superman'}
};

# partition key -> hash_key
# sort key -> range_key

sort key를 지정했기 때문에 ORDER BY를 사용할수있다.
SELECT * FROM "posts"
WHERE "writer" = 'kimgura'
ORDER BY "created_at" ASC;

key를 writer, created_at으로 지정했기때문에
DELETE FROM posts
WHERE "writer" = 'kimgura' AND "created_at" = '2026-01-01';

UPDATE "posts"
SET	"title"='수정한 NoSQL 2?'
WHERE "writer"='kimgura' AND "created_at"='2026-01-02';
'''