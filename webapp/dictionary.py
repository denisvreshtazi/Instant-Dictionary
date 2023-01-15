import justpy as jp
from definition import Definition
from webapp import layout, page


class Dictionary(page.Page):
    path = "/dictionary"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="Instant Dictionary", classes="text-4xl m-2")
        jp.Div(a=div, text="Get the definition of any English word instantly as you type", classes="text-lg")

        input_div = jp.Div(a=div, classes="grid grid-cols-2")
        output_div = jp.Div(a=div, classes="m-2 p-2 text-lg border-2 border-gray-300 h-40")

        input_box = jp.Input(a=input_div, placeholder="Type in a word gere...", outputdiv=output_div,
                             classes="m-2 bg-gray-180 border-2 border-gray-300 rounded w-64 focus:outline-none focus:bg-white focus:border-purple-500 "
                                     "py-2 px-4")

        input_box.on('input', cls.get_definition)

        # If you want to add a button for translation
        # output_div = jp.Div(a=div, classes="m-2 p-2 text-lg border-2 border-gray-300 h-40")
        # jp.Button(a=input_div, text="Get Definition", classes="border-2 border-gray-300 text-grey-500",
        #          click=cls.get_definition, outputdiv=output_div, inputbox=input_box)

        return wp

    @staticmethod
    def get_definition(widget, msg):
        if len(Definition(widget.value).get()) != 0:
            widget.outputdiv.text = " ".join(Definition(widget.value).get())
        else:
            widget.outputdiv.text = "Definition not found ..."
