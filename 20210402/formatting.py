# print("{0} and". format("computer","information
# print("{item2} and {item1}".format(item1="computer", item2="information"))
dic = {"item1":"컴퓨터", "item2":"information"}
#print("{0[item2]} and {0[item1]}, {1}".format(dic,"jj"))
print("{item1!s} and {item2!s}".format(**dic)) 
print("{item1!r} and {item2!r}".format(**dic))
print("{item1!a} and {item2!a}".format(**dic))