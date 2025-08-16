s3_bucket_list = ["david_s3_bucket", "john_s3-bucket", "greg_s3_bucket", "jim_s3_bucket"]
print(len(s3_bucket_list))

s3_bucket_list.append("doug_s3_bucket")
print(s3_bucket_list)
print(len(s3_bucket_list))

s3_bucket_list.remove("jim_s3_bucket")
print(s3_bucket_list)
print(len(s3_bucket_list))


new_s3_bucket_list = s3_bucket_list[1:2]
print(new_s3_bucket_list)
print(len(new_s3_bucket_list))
