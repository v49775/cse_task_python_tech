jobs=[
{"id":1, "status":"pending", "priority":3},
{"id":2, "status":"completed", "priority":5},
{"id":1, "status":"pending", "priority":3},
{"id":3, "status":"pending", "priority":1},	
{"id":4, "status":"pending", "priority":0}]

#Return only jobs with status pending
def pending_jobs(jobs):
     pending_jobs=[]
     for i in jobs:
         if i['status'] == "pending":
             pend_jobs.append(i)
     return pending_jobs



#Return unique and remoce Dublicate ids
def remoce_dub(jobs):
    un_ids=[]
    for i in jobs:
        if i['id'] not in un_ids:
            un_ids.append(i)
    return un_ids


#Exclude jobs whose priority is not positive integer
def positive_priority(jobs):
    positive_priority=[]
    for i in jobs:
        if type(i['priority']) == int and i['priority'] >=0 :
            positive_priority.append(i)
    return positive_priority


#Sort the Result by priority - heighest first
def sort_priority(jobs):
    sorted_jobs=[]
    for i in range(len(jobs)):
        print(jobs[i].get('priority'))
        for j in range(i,i-len(jobs)-1):
            print(jobs[i])
            if jobs[i].get('priority') > jobs[j].get('priority'):
                jsorted_jobs.append(jobs[j])
                sorted_jobs.append(jobs[i])

    return sorted_jobs
        

print(sort_priority(jobs))


#--------------------------------------------------------------------------------
# Django admin
#user - admin
#pass - 1234         





