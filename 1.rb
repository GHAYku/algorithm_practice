def divisors(num)
  result = []
  (1..num).each do |i|
    if num % i == 0
      result << i
    end
  end
  result
end

puts "約数を算出したい整数を入力してください"
num = gets.to_i
r = divisor(num)

puts r