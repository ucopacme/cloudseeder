#!/usr/bin/env python3
"""
get me a bucket

Usage:
  bucket.py

Arguments:

Option:
  -h        Show this screen.
  -v --version        Show version.
"""

from troposphere import (
    GetAtt,
    Output,
    Ref,
)

from troposphere.s3 import (
    Bucket,
    PublicAccessBlockConfiguration,
    VersioningConfiguration
)


def add_bucket(tags, template, versioning):
    template.add_resource(
        Bucket(
            "GetMeABucket",
            DeletionPolicy="Retain",
            PublicAccessBlockConfiguration=PublicAccessBlockConfiguration(
                BlockPublicAcls=True,
                BlockPublicPolicy=True,
                IgnorePublicAcls=True,
                RestrictPublicBuckets=True,
            ),
            Tags=tags,
            VersioningConfiguration=VersioningConfiguration(
                Status=versioning,
            )
        )
    )
    template.add_output(
        Output(
            "BucketName",
            Description="Bucket name",
            Value=Ref("GetMeABucket")
        )
    )
    template.add_output(
        Output(
            "BucketNameARN",
            Description="Bucket name Arn",
            Value=GetAtt("GetMeABucket", "Arn")
        )
    )
