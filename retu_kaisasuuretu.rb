def d(ary)
  ary.each_cons(2).map{|i| i[1] - i[0]}
end

ary0 = (0..10).map{|i| i ** 3}
ary1 = [2, 3, 5, 7, 11, 13]
p d(ary0)
p d(ary1)