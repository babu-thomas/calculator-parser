from appJar import gui
from _parser import Parser

app = gui()
app.setTitle('Calculator Parser')
app.setGeometry(800, 600)
app.setExpand('column')
app.setFont(25, "Courier")
app.addLabelEntry('Expression', 0, 0)

def on_parse_click(button):
    expr = app.getEntry('Expression')
    app.disableEntry('Expression')
    app.disableButton('Parse')
    parser = Parser(expr)
    print(parser.parse())

app.addButton('Parse', on_parse_click, 0, 1)

app.go()