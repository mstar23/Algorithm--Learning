def solution(babbling):
    answer = 0
    sounds = ["aya", "ye", "woo", "ma"]
    
    def can_pronounce(word):
        for sound in sounds:
            if word.count(sound) > 1:
                return False
            
            else:
                word = word.replace(sound, "1")
        return all(char == '1' for char in word)
    
    for i in babbling:
        if(can_pronounce(i)):
            answer+=1
            
            
    return answer