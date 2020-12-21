"""
一、创建一个新的文件夹 命名为 旧文件夹_new
    1.新文件夹目录位置，可以选择

二、获取旧文件夹内的所有内容
    1.旧文件夹位置放在与程序同一目录下
    2.旧文件夹的名称可以手动输入

三、多进程的copy文件夹内容

"""
from multiprocessing import Manager
from multiprocessing import Pool
import os

# 拷贝文件功能
def copyFiletask(queue, files, old_file_name, new_file_name):
    fr = open(old_file_name+'/'+files)
    fw = open(new_file_name+'/'+files, 'w')
    content = fr.read()
    fw.write(content)
    fr.close()
    fw.close()
    queue.put(files)

def main():
    # os.chdir('./')  # 将操作目录切换到当前目录下
    # now_file = os.getcwd()
    # print("当前操作目录是%s"%now_file)
    #
    file_name = input('请输入要copy的文件名')
    file_name = str(file_name)
    # if file_name not in os.listdir(now_file):
    #     print('输入的文件名%s有误，请检查！'%file_name)
    # else:
    old_file = os.listdir(file_name)  # 获得旧文件夹内的全部东西
        # print(old_file)
    new_file_name = file_name + "_副本"
    # if new_file_name not in os.listdir(now_file):
    os.mkdir(new_file_name)
    print("创建文件夹%s 成功"%new_file_name)

    q = Manager().Queue() # 创建通信队列
    pool = Pool(3)
    # pool.apply_async(getFile, (q, old_file))
    for files in old_file:
        pool.apply_async(copyFiletask, (q, files, file_name, new_file_name))

    num = 0
    allNum = len(old_file)
    while True:
        q.get()
        num += 1
        copyRate = num/allNum
        print("\r copy的进度是:%.2f%%"%(copyRate*100), end="")
        if num == allNum:
            break

    pool.close()
    pool.join()
    print("拷贝完成")

if __name__=='__main__':
    main()
