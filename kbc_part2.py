question_list = [
    "1.How many continents are there?",
    "2.What is the capital of India?",
    "3.NG mei kaun se course padhaya jaata hai?"]
options_list = [
    
    ["1. Four", "2. Nine", "3. Seven", "4. Eight"],
    ["1. Chandigarh", "2. Bhopal", "3. Chennai", "4. Delhi"],
    ["1. Software Engineering", "2. Counseling", "3. Tourism", "4. Agriculture"]]
answer_list = [1,4,1]  
index = 0
ans_index1 = 0
while index<len(question_list):
    print  question_list[index]
    j = 0
    while j<=len(options_list):
        print options_list[index][j]
        j =j+1
    user_input = int(raw_input("enter your answre"))
    if user_input == answer_list[ans_index1]:
        print "VERRY GOOD YOU ARE RIGHT:).......","\n"
   
    else:
        print "SO BAD YOU ARE RONG:(....."
        print "\n"
	break
    index = index+1
    ans_index1 = ans_index1+1
    
