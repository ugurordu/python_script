
#Anagram
string_1 = input('write a string1:').replace(' ','').lower()
string_2 = input('write a string2:').replace(' ','').lower()

def sort_and_check(a,b):

    sorted_string_1 = sorted(string_1)
    a_count = 0
    for item in sorted_string_1:
        if 'a' in item:
            a_count = a_count + 1

    b_count = 0
    sorted_string_2 = sorted(string_2)
    for item in sorted_string_2:
        if 'b' in item:
            b_count = b_count + 1
    
    if a_count > 1:
        print('first string must contain only one **a**')
    elif b_count > 1:
        print('second string must contain only one **b**')
    else:
        if sorted_string_1 == sorted_string_2:
            print("they are anagrams")
        else:
            print('they are not anagrams')
        
    
    
        def Diff(list1, list2):
            list1_dif = [i for i in list1 + list2 if i not in list1]
            return list1_dif
                
        def Diff2(list1, list2):
            list2_dif = [i for i in list2 + list1 if i not in list2]
            return list2_dif

        
        list1 = string_1
        list2 = string_2 
        diffrent_1 = Diff(list1,list2)
        diffrent_2 = Diff2(list1,list2)
        if len(diffrent_1) >= 1 or len(diffrent_2) >= 1:
            print("remove", len(diffrent_1), "characters from ",'"{}"'.format(string_1), "and",len(diffrent_2),"characters from", '"{}"'.format(string_2))
            print("removed letters for first string: ", diffrent_1)
            print("removed letters for second string: ",diffrent_2)


sort_and_check(string_1,string_2) 

