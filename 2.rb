def divisor_sum(num, limit)
(1..limit).select{ |i| num % i == 0 }.sum
end

puts divisor_sum(1_234_567_890, 1_000_000_0)