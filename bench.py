import requests 
import argparse 
import time 
import re 

def server(url, count):
    
    success = 0
    failed = 0 
    errors = 0
    times = []

    for _ in range(count):
        try:
            start_time = time.time()
            response = requests.get(url)
            response_time = time.time() - start_time
            times.append(response_time)
            host == response
            

            if response.status_code == 200:
                success += 1
            else:
                failed += 1
        except requests.exceptions.RequestException:
            errors += 1
        

    return success, failed, errors, times  


def test_data(url):
    patterns = re.compile(
        r'^(?:http|ftp)s?://'  
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  
        r'localhost|'  
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  
        r'(?::\d+)?'  
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    
    if re.fullmatch(patterns,url):
            return True
    else:
            print("Wrong data!")
            return False
    

        
    
    








def server_print(url,success,failed,errors,times):

    if times:

        min_t = min(times)
        max_t = max(times)
        avg_t = sum(times)/len(times)
    else:

        min_t = max_t = avg_t = 0

    print(f"Host: {url}")
    print(f"Success: {success}")
    print(f"Failed: {failed}")
    print(f"Errors: {errors}")
    print(f"Min: {min_t:.2f} seconds")
    print(f"Max: {max_t:.2f} seconds")
    print(f"Avg: {avg_t:.2f} seconds\n")




parser = argparse.ArgumentParser()
parser.add_argument("-H", "--hosts", required=True, help="List of hosts")
parser.add_argument("-C", "--count", type=int, default=1, help="Num of requests")


args = parser.parse_args()

hosts = args.hosts.split(',')
count = args.count



for host in hosts:
    if test_data(host.strip()):
        success, failed, errors, times = server(host.strip(), count)
        server_print(host.strip(), success, failed, errors, times)
        