a, b = gets.split(" ").map(&:to_i)
array = []

10.times {|i|
    array[i] = a
    a *= b
}
puts array.join(" ")
puts array.sum

puts "数列の何項目を表示しますか？"
n = gets.to_i
p n *= b