
  integer = [1000, 900, 500, 400, 100,  90,  50,  40,  10,   9,   5,   4,   1]
  roman   = [ "M","CM", "D","CD", "C","XC", "L","XL", "X","IX", "V", "IV","I"]
  result = ""
  integer.length.times do |i|
    while num >= integer[i]
      result += roman[i]
      num -= integer[i]
    end
  end
  return result
