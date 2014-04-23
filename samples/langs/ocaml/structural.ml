class cowboy =
    object (self)
        method draw =
            print_string "Drawing a gun"
    end

class pen = 
    object (self) 
        method draw =
         print_string "Drawing a line"
    end

let draw_something o =
    o#draw
