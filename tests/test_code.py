import pytest
from src.guessFact.code import main_function, category_choice_validation, fact_choice_validation, Coffee, Music

#Test for main_function
def test_main_function_case1(monkeypatch: pytest.MonkeyPatch, capfd: pytest.CaptureFixture) -> None:
    inputs = iter(["1","1","1"])
    monkeypatch.setattr("builtins.input",lambda _: next(inputs))
    main_function()
    captured = capfd.readouterr()
    expected_output_segments = [
        "Welcome to the Guess the Fact Game!",
        "In this game, you'll be presented with two statements about a chosen topic.",
        "Your task is to guess which statement is true.",
        "Let's get started",
        "Please choose a category:",
        "1: Music",
        "2: Coffee",
        "3: Food",
        "Please choose a sub-category:",
        "1: Classical",
        "2: Jazz",
        "3: Pop"
    ]
    output = captured.out
    for segment in expected_output_segments:
        assert segment in output

def test_main_function_case2(monkeypatch: pytest.MonkeyPatch, capfd: pytest.CaptureFixture) -> None:
    inputs = iter(["4","1","a","1","1"])
    monkeypatch.setattr("builtins.input",lambda _: next(inputs))
    main_function()
    captured = capfd.readouterr()
    expected_output_segments = [
        "Welcome to the Guess the Fact Game!",
        "In this game, you'll be presented with two statements about a chosen topic.",
        "Your task is to guess which statement is true.",
        "Let's get started",
        "Please choose a category:",
        "1: Music",
        "2: Coffee",
        "3: Food",
        "Please choose a sub-category:",
        "1: Classical",
        "2: Jazz",
        "3: Pop"
    ]
    output = captured.out
    for segment in expected_output_segments:
        assert segment in output

def test_main_function_case3(monkeypatch: pytest.MonkeyPatch, capfd: pytest.CaptureFixture) -> None:
    inputs = iter(["1","3","1"])
    monkeypatch.setattr("builtins.input",lambda _: next(inputs))
    main_function()
    captured = capfd.readouterr()
    expected_output_segments = [
        "Welcome to the Guess the Fact Game!",
        "In this game, you'll be presented with two statements about a chosen topic.",
        "Your task is to guess which statement is true.",
        "Let's get started",
        "Please choose a category:",
        "1: Music",
        "2: Coffee",
        "3: Food",
        "Please choose a sub-category:",
        "1: Classical",
        "2: Jazz",
        "3: Pop"
    ]
    output = captured.out
    for segment in expected_output_segments:
        assert segment in output

#Test for fact_choice_validation function
def test_fact_choice_validation_case1() -> None:
    assert fact_choice_validation("1") == True

def test_fact_choice_validation_case2() -> None:
    assert fact_choice_validation("2") == True
    
def test_fact_choice_validation_case3() -> None:
    assert fact_choice_validation(" 2") == False
    
def test_fact_choice_validation_case4() -> None:
    assert fact_choice_validation(" ") == False

def test_fact_choice_validation_case5() -> None:
    assert fact_choice_validation("3") == False

#Test for category_choice_validation function
def test_category_choice_validation_case1() -> None:
    assert category_choice_validation("1") == True

def test_category_choice_validation_case2() -> None:
    assert category_choice_validation("2") == True
    
def test_category_choice_validation_case3() -> None:
    assert category_choice_validation("3") == True

def test_category_choice_validation_case4() -> None:
    assert category_choice_validation("") == False
    
def test_category_choice_validation_case5() -> None:
    assert category_choice_validation("1") == True
    
def test_category_choice_validation_case6() -> None:
    assert category_choice_validation("4") == False


#test out put fact sub cat1
def test_Coffee_valid_output_choices1( monkeypatch: pytest.MonkeyPatch, capfd: pytest.CaptureFixture):#

    sub_choice = 1

    # Mock user input to be "1"

    monkeypatch.setattr("builtins.input", lambda _: "1")
    Coffee(sub_choice)

    # Capture printed output
    out = capfd.readouterr().out

    possible_outputs = [
        "1.According to legend, coffee was discovered when a goat herder noticed his 'goats' energy after eating coffee berries"\
            "\n2.In 15th-century Yemen, coffee beans were so valuable that merchants would trade them for gemstones", 

            "1.In medieval Ethiopia, coffee was once taxed under a 'wakefulness tax'"\
            "\n2.The Arabic root word for coffe -- qahwa -- originally refered to a type of wine"
    ]

    assert any(possible_output in out for possible_output in possible_outputs)

#test out put fact sub cat2
def test_Coffee_valid_output_choices2( monkeypatch: pytest.MonkeyPatch, capfd: pytest.CaptureFixture):#

    sub_choice = 2

    # Mock user input to be "1"

    monkeypatch.setattr("builtins.input", lambda _: "1")
    Coffee(sub_choice)

    # Capture printed output
    out = capfd.readouterr().out

    possible_outputs = [
        "1.According to global trade data, coffee is indeed one of the most traded commodities, second only to oil”\
            \n2.In a remote mountain village in Nepal, monks practice “coffee meditation", 
            
        "1.Finland consistently ranks first in coffee consumption per capita"\
        "\n2.In a small town in France, it’s customary to clink coffee mugs before every sip. Local folklore says it helps people “toast” the spirit of the coffee bean for good energy" 
            
    ]

    assert any(possible_output in out for possible_output in possible_outputs)

#test out put fact sub cat1 & unvalid input
def test_Coffee_valid_output_choices3( monkeypatch: pytest.MonkeyPatch, capfd: pytest.CaptureFixture):#

    sub_choice = 3

    # Mock user input to be "3"then"1"
    inputs = iter(["a","4", "1"])
    monkeypatch.setattr("builtins.input",lambda _: next(inputs))
   # monkeypatch.setattr("builtins.input", lambda _: "1")
    Coffee(sub_choice)

    # Capture printed output
    out = capfd.readouterr().out

    possible_outputs = [
       "1.In the highlands of Peru, there is a rare coffee plant that only blooms at midnight on full moons, releasing an unusually sweet aroma. The coffee from these “Lunar Beans” is said to have a mellow, caramel flavor"\
            "\n2.Coffee is one of the richest sources of antioxidants in the average diet, even more than some fruits and vegetables", 
            
        "1.Studies have found that just holding a warm cup of coffee can affect your perception and behavior."\
        "\n2.In a lab experiment, researchers in Iceland developed coffee beans that change color according to the drinker’s mood. These “Mood Beans” are still in development but are said to go from green (calm) to red (excited) as you take a sip"
            
    ]

    assert any(possible_output in out for possible_output in possible_outputs)

#test result sub cat1
def test_Coffee_valid_result1( monkeypatch: pytest.MonkeyPatch, capfd: pytest.CaptureFixture):#

    sub_choice = 1

    # Mock user input to be "3"then"1"
    monkeypatch.setattr("builtins.input",lambda _: "1")

    Coffee(sub_choice)

    # Capture printed output
    out = capfd.readouterr().out


    output1 = "1.According to legend, coffee was discovered when a goat herder noticed his 'goats' energy after eating coffee berries"\
            "\n2.In 15th-century Yemen, coffee beans were so valuable that merchants would trade them for gemstones"
    
    if output1 in out:
        assert "You are right," in out
    else:
        assert "You are wrong," in out

#test result sub cat2
def test_Coffee_valid_result2( monkeypatch: pytest.MonkeyPatch, capfd: pytest.CaptureFixture):#

    sub_choice = 2

    # Mock user input to be "3"then"1"
    monkeypatch.setattr("builtins.input",lambda _: "1")

    Coffee(sub_choice)

    # Capture printed output
    out = capfd.readouterr().out

    output1 = "1.According to global trade data, coffee is indeed one of the most traded commodities, second only to oil”\
            \n2.In a remote mountain village in Nepal, monks practice “coffee meditation"
    
    if output1 in out:
        assert "You are right," in out
    else:
        assert "You are right," in out

#test result sub cat3
def test_Coffee_valid_result3( monkeypatch: pytest.MonkeyPatch, capfd: pytest.CaptureFixture):#

    sub_choice = 3

    # Mock user input to be "3"then"1"
    monkeypatch.setattr("builtins.input",lambda _: "1")

    Coffee(sub_choice)

    # Capture printed output
    out = capfd.readouterr().out


    output1 = "1.In the highlands of Peru, there is a rare coffee plant that only blooms at midnight on full moons, releasing an unusually sweet aroma. The coffee from these “Lunar Beans” is said to have a mellow, caramel flavor"\
            "\n2.Coffee is one of the richest sources of antioxidants in the average diet, even more than some fruits and vegetables"
    
    if output1 in out:
        assert "You are wrong," in out
    else:
        assert "You are right," in out

def test_Music_valid_result1( monkeypatch: pytest.MonkeyPatch, capfd: pytest.CaptureFixture):
    # input user choice
    monkeypatch.setattr("builtins.input",lambda _: "1")

    Music(1)

    # compare output with expected result
    out = capfd.readouterr().out
    assert "You are right!" in out

def test_Music_valid_result2( monkeypatch: pytest.MonkeyPatch, capfd: pytest.CaptureFixture):
    # input user choice
    monkeypatch.setattr("builtins.input",lambda _: "1")

    Music(2)

    # compare output with expected result
    out = capfd.readouterr().out
    output1 = "Fact 1: Louis Armstrong’s influential trumpet playing helped shape modern jazz.\nFact 2: Jazz originated in London during the 19th century.\n"
    output2 = "Fact 1: Duke Ellington was primarily known as a classical pianist and rarely performed jazz.\nFact 2: Louis Armstrong, one of the most influential figures in jazz, was also known for his distinctive gravelly voice and popularized scat singing.\n"
    print("------------------------------------") # TEST
    print(out) # TEST
    if output1 in out:
        assert "You are right!" in out
    else:
        assert "You are wrong!" in out