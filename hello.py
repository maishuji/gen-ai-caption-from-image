import gradio as gr

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")

# You can specify the server port as well
demo.launch(server_name="127.0.0.1") #