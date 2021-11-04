def fizz_buzz(input)
 if input % 15 == 0
  puts "FizzBuzz"
 elsif input % 5 ==0
  puts "Buzz"
 elsif input % 3 == 0
  puts "Fizz"
 else
  puts input
 end
end

puts "数字を入力してください。"

input = gets.to_i

puts "結果は..."
puts fizz_buzz(input)