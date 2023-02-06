""" Authenticate with boto3 """
# Ref: ttps://www.gormanalysis.com/blog/connecting-to-aws-s3-with-python/
#import os
import boto3
#import pandas as pd


class DataStorage:
    """This moduel provides functionality to upload stock data
    into the Amazon S3 bucket named stock-market-data7
    """
    # default constructor

    def __init__(self):
        self.s3 = boto3.resource(
            service_name='s3',
            region_name='ca-central-1',
            aws_access_key_id='AKIAQLIFTMJPM5O3Y4DU',
            aws_secret_access_key='nsCD0P6rzcgkGLY8jUvwUpKop4zRNl66gh0JhT8W'
        )

    def list_bucket(self):
        """This function is listing the buckets accessbile by your account"""
        print('These are the buckets accessbile by your account:')
        for bucket in self.s3.buckets.all():
            print(bucket.name)

    def upload_file(self):
        """Read and Write files into S3 bucket"""
        self.s3.Bucket(
            'stock-market-data7').upload_file(Filename='fetched.csv', Key='fetched.csv')
        print('The file has been uploaded into S3!')


ds = DataStorage()
ds.list_bucket()
