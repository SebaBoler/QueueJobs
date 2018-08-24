import requests

def run_query(query): 
    request = requests.post('http://localhost:4466', json={'query': query})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed  {}. {}".format(request.status_code, query))
     
query = """
{
  queueJobses{
    id
    status
    params
    dataIn
    createdAt
    jobInfo { jobType jobGroup}
  }
}
"""

result = run_query(query) 
print result
