""" Authenticate with boto3 """
import json
import boto3
class DataStorage:
    """This moduel provides functionality to upload stock data
    into the Amazon S3 bucket named stock-market-data7
    """
    def __init__(self):
        with open("DSCC-FP-MVP-Configuration.json", "r", encoding='utf-8') as jsonfile:
            data = json.load(jsonfile)
        self.s3_access_object = boto3.resource(
            service_name='s3',
            region_name='ca-central-1',
            aws_access_key_id=data["credentials"]["aws_access_key_id"],
            aws_secret_access_key=data["credentials"]["aws_secret_access_key"]
        )

    def list_bucket(self):
        """This function is listing the buckets accessbile by your account"""
        print('These are the buckets accessbile by your account:')
        for bucket in self.s3_access_object.buckets.all():
            print(bucket.name)

    def upload_file(self,bucket_name,filename):
        """Upload file from local system to the S3 bucket"""
        self.s3_access_object.Bucket(bucket_name).upload_file(Filename=filename, Key='fetched.csv')
        print('The file has been uploaded into S3!')

    def download_file(self,bucket_name,filename):
        """Download file from S3 bucket to local file system"""
        self.s3_access_object.Bucket(bucket_name).download_file(filename, 'fetched.csv')
        print('The file has been downloaded from S3!')

ds = DataStorage()
ds.download_file('stock-market-data7','fetched.csv')
