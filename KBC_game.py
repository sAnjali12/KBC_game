question_list = [
    "1.How many continents are there?",
    "2.What is the capital of madhya pradesh?",
    "3.NG mei kaun se course padhaya jaata hai?"]
options_list = [
    
    ["1. Four", "2. Nine", "3. Seven", "4. Eight"],
    ["1. Chandigarh", "2. delhi", "3. Chennai", "4. Bhopal"],
    ["1. Software Engineering", "2. Counseling", "3. Tourism", "4. Agriculture"]]
answer_list = [1,4,1]  
index = 0
ans_index1 = 0
life_line = 5050
more_index = 0
while index<len(question_list):
    print  question_list[index]
    j = 0
    while j<=len(options_list):
        print options_list[index][j]
        j =j+1
    user_input = int(raw_input("enter your answre"))
    if user_input == answer_list[ans_index1]:
        print "VERRY GOOD YOU ARE RIGHT:).......","\n"
    elif user_input == life_line and more_index == 0:
   	again_options_list = [["1. four","2. seven"],["1. bhopal","2.delhi"],["1. tourism","2. software Engineerinng"]]
	again_option_answer_list = [1,2,2]
        again_ans_index = 0 
        again_index = 0
	while again_index<len(question_list):
		print question_list[index]
		again_index = index
		again_ans_index = ans_index1
		j2 = 0
		while j2<len(again_options_list)-1:	
			print again_options_list[again_index][j2]
			j2  = j2+1
		again_user_input = int(raw_input("enter your answer"))
		if again_user_input == again_option_answer_list[again_ans_index]:
			print "IT IS RIGHT BUT YOU USE LIFE LINE IT'S NOT GOOD.........","\n"
			break
		else:
			print "YOU ARE RONG"
			break    		
		again_ans_index = again_ans_index+1
		again_index = again_index+1
	more_index = more_index+1
    else:
        print "SO BAD YOU ARE RONG:(....."
        print "\n"
	break
    index = index+1
    ans_index1 = ans_index1+1
    
