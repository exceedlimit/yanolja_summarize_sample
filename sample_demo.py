# 그냥 사용하면 안되고 래핑 필요

'''원본 파일
import gradio as gr

def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
)

demo.launch()
'''

import gradio as gr

# 숫자만큼 단순히 느낌표 갯수 추가
def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

# 이부분 래핑
def run_demo():
    demo = gr.Interface(
        fn=greet,
        inputs=["text", "slider"],
        outputs=["text"],
    )

    demo.launch()

if __name__=='__main__':
    run_demo()