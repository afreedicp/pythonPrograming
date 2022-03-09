import testing 
def testSame():
             ret=testing.freq("abcfffgggggk")
             assert ret=={"a":1,"b":1,"c":1,"f":3,"g":5,"k":1}
def testMultiple():
          ret=testing.freq("abcfffgggggktttttt")
          assert ret=={"a":1,"b":1,"c":1,"f":3,"g":5,"k":1,"t":6}
def testEmpty():
          ret=testing.freq("")
          assert ret=={} 
def testpangrm():
             ret=testing.panagram("qwertyuiopasdfghjklzxcvbnm")
             assert ret 
def testpangrm_fail():
     assert not testing.panagram("qwertyuiopasdfghjklzxcbnm")

def test_avrg_postive():
     ret= testing.avrg([1,3,45,56,89]) 
     assert ret==38.8
def test_avrg_negative():
     ret= testing.avrg([-2,12,-34,-1,0]) 
     assert ret==-5
def test_avrg_empty():
    ret= testing.avrg([])  
    assert ret ==None         
    
"writer a function to find the avarage of a list of numbers"