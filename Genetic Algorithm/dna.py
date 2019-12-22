from random import randint,random
class dna:
    def __init__(self,length):
        self.fitness=0
        self.length=length
        self.genes=[self.get_random_char() for i in range(length)]
    def calculate_fitness(self,target_word):
        score=0
        for i in range(self.length):
            if self.genes[i]==target_word[i]:
                score+=1
        self.fitness=score/len(target_word)
        return score
    def crossover(self,parent):
        rnd_index=randint(0,self.length-1)
        child=dna(self.length)
        for i in range(child.length):
            if i<rnd_index:
                child.genes[i]=self.genes[i]
            else:
                child.genes[i]=parent.genes[i]
        return child
    def mutation(self,mutate_dna,mutation_per=0.01):
        for i in range(mutate_dna.length):
            rnd_num=random()
            if rnd_num<mutation_per:
                mutate_dna.genes[i]=self.get_random_char()
        return mutate_dna
    @staticmethod
    def get_random_char():
        start=32
        end=126
        rnd_num=randint(start,end)
        return chr(rnd_num)
