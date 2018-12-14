from lxml import etree


root = etree.HTML("<li><a onclick=\"st(this,'web2ww','wenwen')\" href=\"https://wenwen.sogo.u.com/?ch=websearch\" uigs-id=\"nav_wenwen\" id=\"index_more_wenwen\">问问</a></li>")


print(root.find(".//a").attrib['href'])




