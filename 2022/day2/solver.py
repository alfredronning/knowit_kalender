print((lambda g:sum(max(2,len([t for t in g[:i]if"alv"not in t]))for i in range(len(g))))(open("gaver.txt").readlines()))
