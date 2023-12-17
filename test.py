from hdfs import InsecureClient

def upload_to_hdfs(local_path, hdfs_path):
    client = InsecureClient('http://127.0.0.1:9870', user='namnt')
    client.upload(hdfs_path, local_path)

if __name__ == "__main__":
    local_file_path = 'requirements.txt'
    hdfs_file_path = './requirements2.txt'
    upload_to_hdfs(local_file_path, hdfs_file_path)
