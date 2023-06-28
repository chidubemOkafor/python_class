def kelvinToFahrenheit(value):
    assert value >= 0, "colder than absolute zero"
    print((value - 273.15) * 9/5 + 32)    
kelvinToFahrenheit(22)