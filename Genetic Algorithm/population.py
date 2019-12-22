from dna import dna
from random import random
class population:
    def __init__(self,population_size,target_word):
        self.population=[dna(len(target_word)) for i in range(population_size)]
        self.generation=0
        self.population_size=population_size
        self.target_word=[w for w in target_word]
        self.target=target_word
        self.__perfect=False
    def natural_selection(self):
        return [entity.calculate_fitness(self.target_word) for entity in self.population]
    def reproduction(self,mutation_per=0.01):
        weights=self.natural_selection()
        best=None
        best_fitness=0
        for i in range(self.population_size):
            parent_1=self.__random_element_with_weights(self.population,weights)
            parent_2=self.__random_element_with_weights(self.population,weights)
            child=parent_1.crossover(parent_2)
            child=child.mutation(child,mutation_per)
            self.population[i]=child
            fitness=child.calculate_fitness(self.target_word)
            if fitness>best_fitness:
                best=child
                best_fitness=fitness
            if best is None:
                best=child
                best_fitness=fitness
            if self.check_perfect(child.genes):
                self.__perfect=True
                break
        yield best
    def evolution(self,stats=True):
        while not self.__perfect:
            self.generation+=1
            for best_child in self.reproduction():
                if stats:
                    print("Generation= ",self.generation)
                    word=""
                    for character in best_child.genes:
                        word+=character
                    print(f"TARGET WORD: {self.target} | BEST WORD GENERATED: {word} | FITNESS: {best_child.fitness}")
    def check_perfect(self,word):
        return word==self.target_word
    @staticmethod
    def __random_element_with_weights(iterable,weights):
        if len(iterable)==len(weights):
            weight_sum=sum(weights)
            rand_weight=weight_sum*random()
            for i in range(len(weights)):
                rand_weight=rand_weight-weights[i]
                if rand_weight <= 0:
                    return iterable[i]
        else:
            raise ValueError("Passed Iterable and Weights should be of same size")
            
            
        
