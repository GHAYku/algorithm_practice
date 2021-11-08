puts "数列の何項目を表示しますか？"
n = gets.to_i

a, b, c = 1, 0, 5
(n - 1).times { a, b, c = b, c, a + b + c }
p a

#50番目の項を算出する。

def tribonacci(n)
  result = []
  return   if n < 1
  a, b, c = 1, 3 ,7
  (n).times { a, b, c = b, c, a + b + c, result << a }
  result
end

puts "数列を何項目まで表示しますか？"
n = gets.to_i

puts "#{tribonacci(n)}"
