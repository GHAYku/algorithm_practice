{"filter":false,"title":"test.py","tooltip":"/test.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":18,"column":0},"end":{"row":18,"column":1},"action":"insert","lines":[" "],"id":153}],[{"start":{"row":12,"column":1},"end":{"row":12,"column":2},"action":"insert","lines":[" "],"id":154}],[{"start":{"row":13,"column":1},"end":{"row":13,"column":2},"action":"insert","lines":[" "],"id":155}],[{"start":{"row":14,"column":1},"end":{"row":14,"column":2},"action":"insert","lines":[" "],"id":156}],[{"start":{"row":15,"column":2},"end":{"row":15,"column":3},"action":"insert","lines":[" "],"id":157}],[{"start":{"row":15,"column":2},"end":{"row":15,"column":3},"action":"remove","lines":[" "],"id":158}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":2},"action":"remove","lines":["  "],"id":162}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":1},"action":"insert","lines":[" "],"id":163},{"start":{"row":15,"column":1},"end":{"row":15,"column":2},"action":"insert","lines":[" "]},{"start":{"row":15,"column":2},"end":{"row":15,"column":3},"action":"insert","lines":[" "]}],[{"start":{"row":18,"column":22},"end":{"row":18,"column":23},"action":"remove","lines":["0"],"id":164},{"start":{"row":18,"column":21},"end":{"row":18,"column":22},"action":"remove","lines":["0"]},{"start":{"row":18,"column":20},"end":{"row":18,"column":21},"action":"remove","lines":["0"]},{"start":{"row":18,"column":19},"end":{"row":18,"column":20},"action":"remove","lines":["6"]}],[{"start":{"row":18,"column":19},"end":{"row":18,"column":23},"action":"insert","lines":["8192"],"id":165}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":1},"action":"insert","lines":[" "],"id":166}],[{"start":{"row":17,"column":1},"end":{"row":17,"column":2},"action":"insert","lines":[" "],"id":167}],[{"start":{"row":18,"column":1},"end":{"row":18,"column":2},"action":"insert","lines":[" "],"id":168},{"start":{"row":18,"column":2},"end":{"row":18,"column":3},"action":"insert","lines":[" "]}],[{"start":{"row":10,"column":1},"end":{"row":10,"column":2},"action":"insert","lines":[" "],"id":169}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":2},"action":"remove","lines":["  "],"id":170}],[{"start":{"row":15,"column":2},"end":{"row":15,"column":3},"action":"remove","lines":[" "],"id":175}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":1},"action":"insert","lines":[" "],"id":176}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":1},"action":"remove","lines":[" "],"id":177}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":2},"action":"remove","lines":["  "],"id":178}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":1},"action":"insert","lines":[" "],"id":179},{"start":{"row":14,"column":1},"end":{"row":14,"column":2},"action":"insert","lines":[" "]}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":2},"action":"remove","lines":["  "],"id":180}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":1},"action":"insert","lines":[" "],"id":181}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":2},"action":"remove","lines":["  "],"id":182}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"insert","lines":[" "],"id":183}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":2},"action":"remove","lines":["  "],"id":184}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":1},"action":"insert","lines":[" "],"id":185}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":2},"action":"remove","lines":["  "],"id":186}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":1},"action":"insert","lines":[" "],"id":187}],[{"start":{"row":0,"column":0},"end":{"row":18,"column":29},"action":"remove","lines":["import math, itertools","","def foo(n):"," max_area = 2 * n","return sum([[[a, b, int(math.sqrt(a**2 + b**2))] \\"," for b in range(1, math.ceil(max_area / a)) \\"," if math.sqrt(a**2 + b**2).is_integer()] \\"," for a in range(1, max_area + 1)], [])","","def bar(lst):","newLst = []"," while lst != []:"," elm = lst[0]"," lst = [i for i in lst if not tuple(i) in itertools.permutations(elm)]"," newLst += [elm]"," return newLst","","  if __name__ == '__main__':","   print(len(bar(foo(8192))))"],"id":188}],[{"start":{"row":0,"column":0},"end":{"row":9,"column":56},"action":"insert","lines":["import math","","list_abc=[]","for b in range(1,12001):","    for a in range(1,b+1):","        if a*b > 12000: break","        c = math.sqrt(a**2+b**2)","        if c == int(c): list_abc.append((a,b,int(c)))","","print(\"The number of combinations = %d\" % len(list_abc))"],"id":189}],[{"start":{"row":9,"column":56},"end":{"row":9,"column":57},"action":"insert","lines":["）"],"id":190},{"start":{"row":9,"column":57},"end":{"row":9,"column":58},"action":"insert","lines":["）"]}],[{"start":{"row":9,"column":57},"end":{"row":9,"column":58},"action":"remove","lines":["）"],"id":191},{"start":{"row":9,"column":56},"end":{"row":9,"column":57},"action":"remove","lines":["）"]}],[{"start":{"row":9,"column":56},"end":{"row":9,"column":57},"action":"insert","lines":[")"],"id":192}],[{"start":{"row":0,"column":0},"end":{"row":9,"column":57},"action":"remove","lines":["import math","","list_abc=[]","for b in range(1,12001):","    for a in range(1,b+1):","        if a*b > 12000: break","        c = math.sqrt(a**2+b**2)","        if c == int(c): list_abc.append((a,b,int(c)))","","print(\"The number of combinations = %d\" % len(list_abc)))"],"id":203}],[{"start":{"row":0,"column":0},"end":{"row":18,"column":27},"action":"insert","lines":["import math","","def foo(n):","　max_area = 2 * n","　return sum([[[a, b, int(math.sqrt(a**2 + b**2))] \\","　　　　for b in range(1, math.ceil(max_area / a)) \\","　　　　if math.sqrt(a**2 + b**2).is_integer()] \\","　　　　for a in range(1, max_area + 1)], [])","","def bar(lst):","　newLst = []","　while lst != []:","　　elm = lst[0]","　　lst = [i for i in lst if sum(elm) != sum(i)]","　　newLst += [elm]","　return newLst","","if __name__ == '__main__':","　print(len(bar(foo(6000))))"],"id":204}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"remove","lines":["　"],"id":205}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"insert","lines":[" "],"id":206}],[{"start":{"row":0,"column":0},"end":{"row":18,"column":27},"action":"remove","lines":["import math","","def foo(n):"," max_area = 2 * n","　return sum([[[a, b, int(math.sqrt(a**2 + b**2))] \\","　　　　for b in range(1, math.ceil(max_area / a)) \\","　　　　if math.sqrt(a**2 + b**2).is_integer()] \\","　　　　for a in range(1, max_area + 1)], [])","","def bar(lst):","　newLst = []","　while lst != []:","　　elm = lst[0]","　　lst = [i for i in lst if sum(elm) != sum(i)]","　　newLst += [elm]","　return newLst","","if __name__ == '__main__':","　print(len(bar(foo(6000))))"],"id":207}],[{"start":{"row":0,"column":0},"end":{"row":17,"column":16},"action":"insert","lines":["import math","","a = 1","list = []","while a**2/2 < 6000:","　　b = a + 1","　　while a*b/2 <= 6000:","　　　　cs = a**2 + b**2","　　　　c = math.floor(math.sqrt(cs) + 0.001)","　　　　if c**2 == cs:","　　　　　　list.append((a, b, c))","　　　　　　print(a, b, c)","　　　　b += 1","　　a += 1","","","print(list)","print(len(list))"],"id":208}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":1},"action":"remove","lines":["　"],"id":209}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":1},"action":"remove","lines":["　"],"id":210}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":1},"action":"insert","lines":[" "],"id":211}],[{"start":{"row":6,"column":1},"end":{"row":6,"column":2},"action":"remove","lines":["　"],"id":212},{"start":{"row":6,"column":0},"end":{"row":6,"column":1},"action":"remove","lines":["　"]}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":1},"action":"insert","lines":[" "],"id":213},{"start":{"row":6,"column":1},"end":{"row":6,"column":2},"action":"insert","lines":[" "]}],[{"start":{"row":7,"column":3},"end":{"row":7,"column":4},"action":"remove","lines":["　"],"id":214},{"start":{"row":7,"column":2},"end":{"row":7,"column":3},"action":"remove","lines":["　"]},{"start":{"row":7,"column":1},"end":{"row":7,"column":2},"action":"remove","lines":["　"]},{"start":{"row":7,"column":0},"end":{"row":7,"column":1},"action":"remove","lines":["　"]}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":1},"action":"insert","lines":[" "],"id":215},{"start":{"row":7,"column":1},"end":{"row":7,"column":2},"action":"insert","lines":[" "]},{"start":{"row":7,"column":2},"end":{"row":7,"column":3},"action":"insert","lines":[" "]}],[{"start":{"row":8,"column":3},"end":{"row":8,"column":4},"action":"remove","lines":["　"],"id":216},{"start":{"row":8,"column":2},"end":{"row":8,"column":3},"action":"remove","lines":["　"]},{"start":{"row":8,"column":1},"end":{"row":8,"column":2},"action":"remove","lines":["　"]},{"start":{"row":8,"column":0},"end":{"row":8,"column":1},"action":"remove","lines":["　"]}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":1},"action":"insert","lines":[" "],"id":217},{"start":{"row":8,"column":1},"end":{"row":8,"column":2},"action":"insert","lines":[" "]},{"start":{"row":8,"column":2},"end":{"row":8,"column":3},"action":"insert","lines":[" "]},{"start":{"row":8,"column":3},"end":{"row":8,"column":4},"action":"insert","lines":[" "]}],[{"start":{"row":9,"column":3},"end":{"row":9,"column":4},"action":"remove","lines":["　"],"id":218},{"start":{"row":9,"column":2},"end":{"row":9,"column":3},"action":"remove","lines":["　"]},{"start":{"row":9,"column":1},"end":{"row":9,"column":2},"action":"remove","lines":["　"]},{"start":{"row":9,"column":0},"end":{"row":9,"column":1},"action":"remove","lines":["　"]}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":1},"action":"insert","lines":[" "],"id":219},{"start":{"row":9,"column":1},"end":{"row":9,"column":2},"action":"insert","lines":[" "]},{"start":{"row":9,"column":2},"end":{"row":9,"column":3},"action":"insert","lines":[" "]},{"start":{"row":9,"column":3},"end":{"row":9,"column":4},"action":"insert","lines":[" "]},{"start":{"row":9,"column":4},"end":{"row":9,"column":5},"action":"insert","lines":[" "]}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":6},"action":"remove","lines":["　　　　　　"],"id":220}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":1},"action":"insert","lines":[" "],"id":221},{"start":{"row":10,"column":1},"end":{"row":10,"column":2},"action":"insert","lines":[" "]},{"start":{"row":10,"column":2},"end":{"row":10,"column":3},"action":"insert","lines":[" "]},{"start":{"row":10,"column":3},"end":{"row":10,"column":4},"action":"insert","lines":[" "]},{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"insert","lines":[" "]},{"start":{"row":10,"column":5},"end":{"row":10,"column":6},"action":"insert","lines":[" "]}],[{"start":{"row":11,"column":0},"end":{"row":11,"column":6},"action":"remove","lines":["　　　　　　"],"id":222}],[{"start":{"row":11,"column":0},"end":{"row":11,"column":1},"action":"insert","lines":[" "],"id":223},{"start":{"row":11,"column":1},"end":{"row":11,"column":2},"action":"insert","lines":[" "]},{"start":{"row":11,"column":2},"end":{"row":11,"column":3},"action":"insert","lines":[" "]},{"start":{"row":11,"column":3},"end":{"row":11,"column":4},"action":"insert","lines":[" "]},{"start":{"row":11,"column":4},"end":{"row":11,"column":5},"action":"insert","lines":[" "]},{"start":{"row":11,"column":5},"end":{"row":11,"column":6},"action":"insert","lines":[" "]},{"start":{"row":11,"column":6},"end":{"row":11,"column":7},"action":"insert","lines":[" "]}],[{"start":{"row":12,"column":3},"end":{"row":12,"column":4},"action":"remove","lines":["　"],"id":224},{"start":{"row":12,"column":2},"end":{"row":12,"column":3},"action":"remove","lines":["　"]},{"start":{"row":12,"column":1},"end":{"row":12,"column":2},"action":"remove","lines":["　"]},{"start":{"row":12,"column":0},"end":{"row":12,"column":1},"action":"remove","lines":["　"]},{"start":{"row":11,"column":21},"end":{"row":12,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":11,"column":21},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":225},{"start":{"row":12,"column":0},"end":{"row":12,"column":7},"action":"insert","lines":["       "]}],[{"start":{"row":12,"column":6},"end":{"row":12,"column":7},"action":"remove","lines":[" "],"id":226}],[{"start":{"row":13,"column":1},"end":{"row":13,"column":2},"action":"remove","lines":["　"],"id":227},{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"remove","lines":["　"]},{"start":{"row":12,"column":12},"end":{"row":13,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":12,"column":12},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":228},{"start":{"row":13,"column":0},"end":{"row":13,"column":6},"action":"insert","lines":["      "]},{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"insert","lines":[" "]}],[{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"remove","lines":[" "],"id":229},{"start":{"row":13,"column":4},"end":{"row":13,"column":6},"action":"remove","lines":["  "]}],[{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"insert","lines":[" "],"id":230}],[{"start":{"row":0,"column":0},"end":{"row":17,"column":16},"action":"remove","lines":["import math","","a = 1","list = []","while a**2/2 < 6000:"," b = a + 1","  while a*b/2 <= 6000:","   cs = a**2 + b**2","    c = math.floor(math.sqrt(cs) + 0.001)","     if c**2 == cs:","      list.append((a, b, c))","       print(a, b, c)","      b += 1","     a += 1","","","print(list)","print(len(list))"],"id":231}],[{"start":{"row":0,"column":0},"end":{"row":17,"column":16},"action":"insert","lines":["import math","","a = 1","list = []","while a**2/2 < 6000:","　　b = a + 1","　　while a*b/2 <= 6000:","　　　　cs = a**2 + b**2","　　　　c = math.floor(math.sqrt(cs) + 0.001)","　　　　if c**2 == cs:","　　　　　　list.append((a, b, c))","　　　　　　print(a, b, c)","　　　　b += 1","　　a += 1","","","print(list)","print(len(list))"],"id":232}],[{"start":{"row":5,"column":1},"end":{"row":5,"column":2},"action":"remove","lines":["　"],"id":233},{"start":{"row":5,"column":0},"end":{"row":5,"column":1},"action":"remove","lines":["　"]}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":1},"action":"insert","lines":[" "],"id":234}],[{"start":{"row":6,"column":1},"end":{"row":6,"column":2},"action":"remove","lines":["　"],"id":235},{"start":{"row":6,"column":0},"end":{"row":6,"column":1},"action":"remove","lines":["　"]}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":1},"action":"insert","lines":[" "],"id":236}],[{"start":{"row":7,"column":3},"end":{"row":7,"column":4},"action":"remove","lines":["　"],"id":237},{"start":{"row":7,"column":2},"end":{"row":7,"column":3},"action":"remove","lines":["　"]},{"start":{"row":7,"column":1},"end":{"row":7,"column":2},"action":"remove","lines":["　"]},{"start":{"row":7,"column":0},"end":{"row":7,"column":1},"action":"remove","lines":["　"]}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":1},"action":"insert","lines":[" "],"id":238},{"start":{"row":7,"column":1},"end":{"row":7,"column":2},"action":"insert","lines":[" "]},{"start":{"row":7,"column":2},"end":{"row":7,"column":3},"action":"insert","lines":[" "]}],[{"start":{"row":8,"column":3},"end":{"row":8,"column":4},"action":"remove","lines":["　"],"id":239},{"start":{"row":8,"column":2},"end":{"row":8,"column":3},"action":"remove","lines":["　"]},{"start":{"row":8,"column":1},"end":{"row":8,"column":2},"action":"remove","lines":["　"]},{"start":{"row":8,"column":0},"end":{"row":8,"column":1},"action":"remove","lines":["　"]}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":1},"action":"insert","lines":[" "],"id":240},{"start":{"row":8,"column":1},"end":{"row":8,"column":2},"action":"insert","lines":[" "]},{"start":{"row":8,"column":2},"end":{"row":8,"column":3},"action":"insert","lines":[" "]}],[{"start":{"row":9,"column":3},"end":{"row":9,"column":4},"action":"remove","lines":["　"],"id":241},{"start":{"row":9,"column":2},"end":{"row":9,"column":3},"action":"remove","lines":["　"]},{"start":{"row":9,"column":1},"end":{"row":9,"column":2},"action":"remove","lines":["　"]},{"start":{"row":9,"column":0},"end":{"row":9,"column":1},"action":"remove","lines":["　"]}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":1},"action":"insert","lines":[" "],"id":242},{"start":{"row":9,"column":1},"end":{"row":9,"column":2},"action":"insert","lines":[" "]},{"start":{"row":9,"column":2},"end":{"row":9,"column":3},"action":"insert","lines":[" "]}],[{"start":{"row":10,"column":5},"end":{"row":10,"column":6},"action":"remove","lines":["　"],"id":243},{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"remove","lines":["　"]},{"start":{"row":10,"column":3},"end":{"row":10,"column":4},"action":"remove","lines":["　"]},{"start":{"row":10,"column":2},"end":{"row":10,"column":3},"action":"remove","lines":["　"]},{"start":{"row":10,"column":1},"end":{"row":10,"column":2},"action":"remove","lines":["　"]},{"start":{"row":10,"column":0},"end":{"row":10,"column":1},"action":"remove","lines":["　"]},{"start":{"row":9,"column":17},"end":{"row":10,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":9,"column":17},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":244},{"start":{"row":10,"column":0},"end":{"row":10,"column":5},"action":"insert","lines":["     "]}],[{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"remove","lines":[" "],"id":245},{"start":{"row":10,"column":2},"end":{"row":10,"column":4},"action":"remove","lines":["  "]},{"start":{"row":10,"column":0},"end":{"row":10,"column":2},"action":"remove","lines":["  "]}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":1},"action":"insert","lines":[" "],"id":246},{"start":{"row":10,"column":1},"end":{"row":10,"column":2},"action":"insert","lines":[" "]},{"start":{"row":10,"column":2},"end":{"row":10,"column":3},"action":"insert","lines":[" "]},{"start":{"row":10,"column":3},"end":{"row":10,"column":4},"action":"insert","lines":[" "]},{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"insert","lines":[" "]}],[{"start":{"row":11,"column":5},"end":{"row":11,"column":6},"action":"remove","lines":["　"],"id":247},{"start":{"row":11,"column":4},"end":{"row":11,"column":5},"action":"remove","lines":["　"]},{"start":{"row":11,"column":3},"end":{"row":11,"column":4},"action":"remove","lines":["　"]},{"start":{"row":11,"column":2},"end":{"row":11,"column":3},"action":"remove","lines":["　"]},{"start":{"row":11,"column":1},"end":{"row":11,"column":2},"action":"remove","lines":["　"]},{"start":{"row":11,"column":0},"end":{"row":11,"column":1},"action":"remove","lines":["　"]}],[{"start":{"row":11,"column":0},"end":{"row":11,"column":1},"action":"insert","lines":[" "],"id":248},{"start":{"row":11,"column":1},"end":{"row":11,"column":2},"action":"insert","lines":[" "]},{"start":{"row":11,"column":2},"end":{"row":11,"column":3},"action":"insert","lines":[" "]},{"start":{"row":11,"column":3},"end":{"row":11,"column":4},"action":"insert","lines":[" "]},{"start":{"row":11,"column":4},"end":{"row":11,"column":5},"action":"insert","lines":[" "]}],[{"start":{"row":12,"column":3},"end":{"row":12,"column":4},"action":"remove","lines":["　"],"id":249},{"start":{"row":12,"column":2},"end":{"row":12,"column":3},"action":"remove","lines":["　"]},{"start":{"row":12,"column":1},"end":{"row":12,"column":2},"action":"remove","lines":["　"]},{"start":{"row":12,"column":0},"end":{"row":12,"column":1},"action":"remove","lines":["　"]}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":1},"action":"insert","lines":[" "],"id":250},{"start":{"row":12,"column":1},"end":{"row":12,"column":2},"action":"insert","lines":[" "]},{"start":{"row":12,"column":2},"end":{"row":12,"column":3},"action":"insert","lines":[" "]}],[{"start":{"row":13,"column":1},"end":{"row":13,"column":2},"action":"remove","lines":["　"],"id":251},{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"remove","lines":["　"]}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"insert","lines":[" "],"id":252},{"start":{"row":13,"column":1},"end":{"row":13,"column":2},"action":"insert","lines":[" "]}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":2},"action":"remove","lines":["  "],"id":253}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"insert","lines":["　"],"id":254}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"remove","lines":["　"],"id":255},{"start":{"row":12,"column":9},"end":{"row":13,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":12,"column":9},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":256},{"start":{"row":13,"column":0},"end":{"row":13,"column":3},"action":"insert","lines":["   "]}],[{"start":{"row":13,"column":2},"end":{"row":13,"column":3},"action":"remove","lines":[" "],"id":257}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":2},"action":"remove","lines":["  "],"id":258}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"insert","lines":[" "],"id":259}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":1},"action":"insert","lines":["e"],"id":260},{"start":{"row":14,"column":1},"end":{"row":14,"column":2},"action":"insert","lines":["n"]},{"start":{"row":14,"column":2},"end":{"row":14,"column":3},"action":"insert","lines":["d"]}],[{"start":{"row":14,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":261}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":1},"action":"insert","lines":[" "],"id":262},{"start":{"row":14,"column":1},"end":{"row":14,"column":2},"action":"insert","lines":["e"]},{"start":{"row":14,"column":2},"end":{"row":14,"column":3},"action":"insert","lines":["n"]},{"start":{"row":14,"column":3},"end":{"row":14,"column":4},"action":"insert","lines":["d"]}],[{"start":{"row":15,"column":2},"end":{"row":15,"column":3},"action":"remove","lines":["d"],"id":263},{"start":{"row":15,"column":1},"end":{"row":15,"column":2},"action":"remove","lines":["n"]},{"start":{"row":15,"column":0},"end":{"row":15,"column":1},"action":"remove","lines":["e"]},{"start":{"row":14,"column":4},"end":{"row":15,"column":0},"action":"remove","lines":["",""]},{"start":{"row":14,"column":3},"end":{"row":14,"column":4},"action":"remove","lines":["d"]},{"start":{"row":14,"column":2},"end":{"row":14,"column":3},"action":"remove","lines":["n"]},{"start":{"row":14,"column":1},"end":{"row":14,"column":2},"action":"remove","lines":["e"]}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":1},"action":"remove","lines":[" "],"id":264},{"start":{"row":13,"column":7},"end":{"row":14,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":16,"column":16},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":265},{"start":{"row":17,"column":0},"end":{"row":17,"column":1},"action":"insert","lines":[")"]}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":1},"action":"remove","lines":[")"],"id":266},{"start":{"row":16,"column":16},"end":{"row":17,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":4,"column":18},"end":{"row":4,"column":19},"action":"remove","lines":["0"],"id":267},{"start":{"row":4,"column":17},"end":{"row":4,"column":18},"action":"remove","lines":["0"]},{"start":{"row":4,"column":16},"end":{"row":4,"column":17},"action":"remove","lines":["0"]},{"start":{"row":4,"column":15},"end":{"row":4,"column":16},"action":"remove","lines":["6"]}],[{"start":{"row":4,"column":15},"end":{"row":4,"column":19},"action":"insert","lines":["8192"],"id":268}],[{"start":{"row":6,"column":16},"end":{"row":6,"column":20},"action":"remove","lines":["6000"],"id":269}],[{"start":{"row":6,"column":16},"end":{"row":6,"column":20},"action":"insert","lines":["8192"],"id":270}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":6,"column":20},"end":{"row":6,"column":20},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1636335887502,"hash":"807fab3ddb14be773508b079d80b0f2c0678e6f3"}