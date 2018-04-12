#!/usr/bin/env python3

"""
a simple script can run and test your html rendering classes.

Uncomment the steps as you add to your rendering.

"""

from io import StringIO

# importing the html_rendering code with a short name for easy typing.
import html_render as hr


# writing the file out:
def render_page(page, filename):
    """
    render the tree of elements

    This uses StringIO to render to memory, then dump to console and
    write to file -- very handy!
    """

    f = StringIO()
    page.render(f, "    ")

    print(f.getvalue())
    with open(filename, 'w') as outfile:
        outfile.write(f.getvalue())


# # Step 1
# #########

# page = hr.Element()

# page.append("Here is a paragraph of text -- there could be more of them, "
#             "but this is enough  to show that we can do some text")

# page.append("And here is another piece of text -- you should be able to add any number")

# render_page(page, "test_html_output1.html")

# # The rest of the steps have been commented out.
# #  Uncomment them as you move along with the assignment.

# # Step 2
# ##########

# page = hr.HtmlElement()

# body = hr.BodyElement()

# body.append(hr.ParagraphElement("Here is a paragraph of text -- there could be"
#                                 " more of them, but this is enough  to show "
#                                 "that we can do some text"))

# body.append(hr.ParagraphElement("And here is another piece of text -- you "
#                                 "should be able to add any number"))

# page.append(body)

# render_page(page, "test_html_output2.html")

# # Step 3
# ##########

# page = hr.HtmlElement()

# head = hr.HeadElement()
# head.append(hr.TitleElement("PythonClass = Revision 1087:"))

# page.append(head)

# body = hr.BodyElement()

# body.append(hr.ParagraphElement("Here is a paragraph of text -- there could be"
#                                 " more of them, but this is enough  to show "
#                                 "that we can do some text"))
# body.append(hr.ParagraphElement("And here is another piece of text -- you "
#                                 "should be able to add any number"))

# page.append(body)

# render_page(page, "test_html_output3.html")

# # Step 4
# ##########

# page = hr.HtmlElement()

# head = hr.HeadElement()
# head.append(hr.TitleElement("PythonClass = Revision 1087:"))

# page.append(head)

# body = hr.BodyElement()

# body.append(hr.ParagraphElement("Here is a paragraph of text -- there could be"
#                                 " more of them, but this is enough to show "
#                                 "that we can do some text",
#                                 style="text-align: center; font-style: oblique;"))

# page.append(body)

# render_page(page, "test_html_output4.html")

# # Step 5
# #########

# page = hr.HtmlElement()

# head = hr.HeadElement()
# head.append(hr.TitleElement("PythonClass = Revision 1087:"))

# page.append(head)

# body = hr.BodyElement()

# body.append(hr.ParagraphElement("Here is a paragraph of text -- there could be "
#                                 "more of them, but this is enough  to show that "
#                                 "we can do some text",
#                                 style="text-align: center; font-style: oblique;"))

# body.append(hr.HrElement())

# page.append(body)

# render_page(page, "test_html_output5.html")

# # Step 6
# #########

# page = hr.HtmlElement()

# head = hr.HeadElement()
# head.append(hr.TitleElement("PythonClass = Revision 1087:"))

# page.append(head)

# body = hr.BodyElement()

# body.append(hr.ParagraphElement("Here is a paragraph of text -- there could be "
#                                 "more of them, but this is enough  to show that "
#                                 "we can do some text",
#                                 style="text-align: center; font-style: oblique;"))

# body.append(hr.HrElement())

# body.append("And this is a ")
# body.append(hr.AnchorElement("http://google.com", "link"))
# body.append("to google")

# page.append(body)

# render_page(page, "test_html_output6.html")

# # Step 7
# #########

# page = hr.HtmlElement()

# head = hr.HeadElement()
# head.append(hr.TitleElement("PythonClass = Revision 1087:"))

# page.append(head)

# body = hr.BodyElement()

# body.append(hr.HeaderElement(2, "PythonClass - Class 6 example"))

# body.append(hr.ParagraphElement("Here is a paragraph of text -- there could be more of them, "
#                  "but this is enough  to show that we can do some text",
#               style="text-align: center; font-style: oblique;"))

# body.append(hr.HrElement())

# list = hr.UlElement(id="TheList", style="line-height:200%")

# list.append(hr.LiElement("The first item in a list"))
# list.append(hr.LiElement("This is the second item", style="color: red"))

# item = hr.LiElement()
# item.append("And this is a ")
# item.append(hr.AnchorElement("http://google.com", "link"))
# item.append("to google")

# list.append(item)

# body.append(list)

# page.append(body)

# render_page(page, "test_html_output7.html")

# Step 8
########

page = hr.HtmlElement()


head = hr.HeadElement()
head.append(hr.MetaElement(charset="UTF-8"))
head.append(hr.TitleElement("PythonClass = Revision 1087:"))

page.append(head)

body = hr.BodyElement()

body.append(hr.HeaderElement(2, "PythonClass - Example"))

body.append(hr.ParagraphElement("Here is a paragraph of text -- there could be more of them, "
                 "but this is enough  to show that we can do some text",
                 style="text-align: center; font-style: oblique;"))

body.append(hr.HrElement())

list = hr.UlElement(id="TheList", style="line-height:200%")

list.append(hr.LiElement("The first item in a list"))
list.append(hr.LiElement("This is the second item", style="color: red"))

item = hr.LiElement()
item.append("And this is a ")
item.append(hr.AnchorElement("http://google.com", "link"))
item.append("to google")

list.append(item)

body.append(list)

page.append(body)

render_page(page, "test_html_output8.html")
