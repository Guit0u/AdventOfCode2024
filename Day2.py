import os

def check_report(report):
    return ((all(report[i] <= report[i+1] for i in range(len(report) - 1)) 
            or all(report[i] >= report[i+1] for i in range(len(report) - 1)))
            and all(abs(report[i] - report[i+1]) > 0 and abs(report[i] - report[i+1]) < 4 for i in range(len(report) - 1)))
            
input_file = os.path.join('inputs', 'input_2.txt')

sum=0
with open(input_file,"r") as outfile:
    data = outfile.readlines()
    for line in data:
        report = list(map(int,line.split(' ')))
        if(check_report(report)): sum+=1

print("day one result is ",sum)


sum=0
with open(input_file,"r") as outfile:
    data = outfile.readlines()
    for line in data:
        report = list(map(int,line.split(' ')))
        report_is_ok=False
        print("report complet = ", report)
        for i in range(len(report)):
            trunc = report.pop(i)
            print("trunc report",report)
            if(check_report(report)):report_is_ok = True
            report.insert(i, trunc)
        print(report_is_ok)
        if(report_is_ok): sum+=1

print("day two result is",sum)