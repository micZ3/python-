def count_words(filename):

    try:
        with open(filename) as f_obj:
            contents = f_obj.read
    except FileNotFoundError:
        msg = "Sorry,the file" + "dose not exist."
        print(msg)
    else:
    #计算文件大致包含多少个单词
        words = contents.split()#split 把字符串列表，实际num-1,即正确输出为
        num_words = len(words)
        print("The file" + filename + "has about" + str(num_words) + " words.")
    filename = 'alice.txt'
    count_words(filename)
