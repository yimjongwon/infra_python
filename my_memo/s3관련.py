'''

[ec2-user@ip-10-0-1-186 ~]$ aws configure list
NAME       : VALUE                    : TYPE             : LOCATION
profile    : <not set>                : None             : None
access_key : ****************Y6HF     : iam-role         : 
secret_key : ****************Pewf     : iam-role         : 
region     : ap-northeast-2           : imds             : 
[ec2-user@ip-10-0-1-186 ~]$ aws s3 ls
2026-04-30 02:31:26 ktcloud-bucket-b3e2dbb3

[ec2-user@ip-10-0-1-186 ~]$ aws s3 ls s3://ktcloud-bucket-b3e2dbb3
2026-04-30 02:39:59     535569 image.png
[ec2-user@ip-10-0-1-186 ~]$ echo "hello s3 bucket" -> message.txt
[ec2-user@ip-10-0-1-186 ~]$ aws s3 cp message.txt s3://ktcloud-bucket-b3e2dbb3
upload: ./message.txt to s3://ktcloud-bucket-b3e2dbb3/message.txt 
[ec2-user@ip-10-0-1-186 ~]$ aws s3 ls s3://ktcloud-bucket-b3e2dbb3
2026-04-30 02:39:59     535569 image.png
2026-04-30 02:43:13         18 message.txt
[ec2-user@ip-10-0-1-186 ~]$
[ec2-user@ip-10-0-1-186 ~]$ aws s3 cp s3://ktcloud-bucket-b3e2dbb3/image.png ./copied_image.png
download: s3://ktcloud-bucket-b3e2dbb3/image.png to ./copied_image.png
[ec2-user@ip-10-0-1-186 ~]$ aws s3 rm s3://ktcloud-bucket-b3e2dbb3/image.png
delete: s3://ktcloud-bucket-b3e2dbb3/image.png


s3안에 파일들 지울때
[ec2-user@ip-10-0-1-186 ~]$ aws s3 rm s3://ktcloud-bucket-b3e2dbb3/ --recurs
ive
delete: s3://ktcloud-bucket-b3e2dbb3/message.txt


'''