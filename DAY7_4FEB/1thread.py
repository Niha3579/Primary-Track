#FEB 4, 2026

#with threading
# import threading

# def say_hello():
#     print("Hello World!\n")

# t=threading.Thread(target=say_hello)
# t.start()

# print("Main Thread")




#without threading
# import time
# def task():
#     print("Task started")
#     time.sleep(2)
#     print("Task completed")

# task()
# print("Program finished")






# import threading

# def greet(name):
#     print(f"Hello,{name}")
# t=threading.Thread(target=greet, kwargs=("Alice",))
# t.start()








# import urllib.request
# import threading
# import time
# import ssl


# def download_file():
#     url="https://files.eric.ed.gov/fulltext/EJ1172284.pdf'"
#     filename="downloaded_test.txt"

#     print("Starting download for file")

#     urllib.request.urlretrieve(url,"filename")
#     print("Completted download for file")


# t=threading.Thread(target=download_file)
# t.start()
# print("main thread contains execution")







# import urllib.request
# import threading
# import time
# import json
# import ssl
# def download_json():
#     try:
#         print("connecting to api")
#         time.sleep(2) 
#         url='https://fakestoreapi.com/products'
#         headers={
#             "User_Agent":"Mozilla/5.0" 
#         }
#         req=urllib.request.Request(url,headers=headers)
#         context=ssl._create_unverified_context()
#         with url.request.urlopen(req,context=context)as response:
#             data=response.read()
#         print("Data downloaded")
#     # data=urllib.request.urlopen(url).read()
#     # data=urllib.request.urlretrieve(url,'filename')
#     # time.sleep(2)
#         posts=json.loads(data)
#         with open('posts.json','w')as f:
#             json.dump(posts,f,indent=4)

#         print("download complete")
#     except Exception as e:
#         print("Error:",e)

# t=threading.Thread(target=download_json)
# t.start()
# print("Main thread continues execution")






# from multiprocessing import Process,Pool
# import time
# # def worker():
# #     print("worker  is running")
# # if __name__ =='__main__':
    

# #     p=Process(target=worker)
# #     p.start()
# #     p.join()
# #     print("Main process finished")

# def square(n):
#         return n*n
# if __name__ =='__main__':
#     numbers=[10**7,10**2,10**3,10**4,10**5]
#     start=time.time()
#     with Pool() as p:
#        results= p.map(square,numbers)
#     end=time.time()
#     print("Squares:",results)
#     print("TI me taken",end-start)






# from multiprocessing import Pool
# import time

# def analyzie_logs(chunk):
#     print(f"Analysize chunk for {chunk}..")
#     time.sleep(2)
