{"filter":false,"title":"pitagorasu.rb","tooltip":"/pitagorasu.rb","undoManager":{"mark":7,"position":7,"stack":[[{"start":{"row":0,"column":0},"end":{"row":24,"column":3},"action":"insert","lines":["max = 1000","","class Pythagoras","  def initialize(a, b, c)","    @a = a","    @b = b","    @c = c","  end","","  def array","    [@a, @b, @c]","  end","end","","array = []","","(1..max).each do |a|","  (1..a).each do |b|","    (1..b).each do |c|","      if a*a == b*b + c*c","        array << Pythagoras.new(a, b, c)","      end","    end","  end","end"],"id":1}],[{"start":{"row":24,"column":3},"end":{"row":25,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":25,"column":0},"end":{"row":26,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":26,"column":0},"end":{"row":26,"column":24},"action":"insert","lines":["p array.map{|x| x.array}"],"id":3}],[{"start":{"row":26,"column":24},"end":{"row":27,"column":0},"action":"insert","lines":["",""],"id":4}],[{"start":{"row":26,"column":24},"end":{"row":27,"column":0},"action":"remove","lines":["",""],"id":5}],[{"start":{"row":19,"column":25},"end":{"row":19,"column":26},"action":"insert","lines":[" "],"id":6}],[{"start":{"row":19,"column":26},"end":{"row":19,"column":27},"action":"insert","lines":["<"],"id":7}],[{"start":{"row":19,"column":26},"end":{"row":19,"column":27},"action":"remove","lines":["<"],"id":8}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":19,"column":26},"end":{"row":19,"column":26},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1636335140253,"hash":"7f67e3746df736421aec5e27617ac66195c38b66"}