max = 1000

class Pythagoras
  def initialize(a, b, c)
    @a = a
    @b = b
    @c = c
  end

  def array
    [@a, @b, @c]
  end
end

array = []

(1..max).each do |a|
  (1..a).each do |b|
    (1..b).each do |c|
      if a*a == b*b + c*c 
        array << Pythagoras.new(a, b, c)
      end
    end
  end
end

p array.map{|x| x.array}