# 스택 활용
import DS04_stack as st
import webbrowser # 웹 사이트 띄우기 위한 모듈
import time

st.SIZE = 100
st.stack = [None for _ in range(st.SIZE)]
st.top = -1

if __name__ == '__main__':
    urls = ['www.naver.com','www.daum.net','www.google.com','www.nate.com']

    for url in urls:
        st.push(url)
        webbrowser.open(f'https://{url}')
        print(url,end='-->')
        time.sleep(1) # 
    
    print('방문 종료')
    time.sleep(5)

    while True:
        url = st.pop()
        if url == None:
            break
        webbrowser.open(f'https://{url}')
        print(url,end='-->')
        time.sleep(1)
    print('방문 종료')
