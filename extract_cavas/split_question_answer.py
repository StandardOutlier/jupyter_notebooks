import subprocess

def get_clipboard_text():
    # 使用 subprocess 模块调用 pbpaste 命令获取剪贴板文本
    pbpaste_process = subprocess.Popen(["pbpaste"], stdout=subprocess.PIPE)
    pbpaste_output = pbpaste_process.communicate()[0]
    # 将字节字符串解码为普通字符串并返回
    return pbpaste_output.decode("utf-8")

def split_question_and_answers(text):
    # 默认的分隔符
    delimiter = "Group of answer choices"
    
    # 检查文本中是否存在分隔符
    if delimiter in text:
        # 分割文本成问题和答案
        question, answers = text.split(delimiter, 1)
        # 移除问题末尾的空白字符
        question = question.strip()
        # 移除答案开头和末尾的空白字符
        answers = answers.strip()
        return question, answers
    else:
        # 如果找不到分隔符，将整个文本作为问题，答案为空字符串
        return text.strip(), ""

def main():
    # 从剪贴板中获取文本
    clipboard_text = get_clipboard_text()
    # 分割问题和答案
    question, answers = split_question_and_answers(clipboard_text)
    # 打印结果
    print("Question:", question)
    print("Answers:", answers)
    # 将结果复制到剪贴板
    pbcopy_process = subprocess.Popen(["pbcopy"], stdin=subprocess.PIPE)
    pbcopy_process.communicate(input=(question + "\n\n" + answers).encode("utf-8"))

if __name__ == "__main__":
    main()
