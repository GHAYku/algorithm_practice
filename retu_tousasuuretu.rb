a, b = gets.split(" ").map(&:to_i)
array = []
10.times {|i|
    array[i] = a + b * i
}
puts array.join(" ")
puts array.sum

#何項目を表示するか
puts "数列の何項目を表示しますか？"
n = gets.to_i
p a + b * (n - 1)