import justpy as jp


class About:
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tilwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the about page", classes="text-4xl m2")
        jp.Div(a=div, text=""" An online dictionary is a dictionary that is accessible via the Internet through a web browser.
         They can be made available in a number of ways: free, free with a paid subscription for extended or more professional content,
          or a paid-only service. Many dictionaries have been digitized from their print versions and are available at online libraries.
           Some online dictionaries are organized as lists of words, similar to a glossary, while others offer search features,
            reverse lookups, and additional language tools and content such as verb conjugations,
             grammar references, and discussion forums. The variety of online dictionaries for specialized topics is enormous,
              covering a wide range of fields such as computing, business and investing, along with almost any other class of trade,
               science, art, or common interest with its own terminology. """, classes="text-lg")
        return wp

