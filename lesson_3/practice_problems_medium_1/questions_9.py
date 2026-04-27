def foo(param="no"):
    return "yes"

def bar(param="no"):
    return (param == "no") and (foo() or "no")

bar(foo()) # This invocation returns: False
# bar("yes")
# return False and ("yes" or "no")
# return False (the 2nd half of the 'and' expression above isn't evaluated,
#               because it isn't necessary)